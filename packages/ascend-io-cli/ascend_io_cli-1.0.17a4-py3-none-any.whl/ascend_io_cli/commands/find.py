import json
from enum import Enum
from typing import Optional
from jsonpath_ng import jsonpath, parse
import typer
import glog as log

from ascend_io_cli.support import get_client, print_response, re_matcher, JSONDefinitionEncoder

app = typer.Typer(help='Find data-services, dataflows, and components', no_args_is_help=True)


class FindBy(str, Enum):
  FIELD = 'FIELD'
  NAME = 'NAME'
  METADATA = 'METADATA'
  SOURCE = 'SOURCE'
  ALL = 'ALL'


@app.command()
def components(
    ctx: typer.Context,
    criteria: str = typer.Argument(..., help='Find components with metadata containing this text'),
    find_by: FindBy = typer.Option(FindBy.FIELD, help='Narrow the search using this parameter'),
    data_service: str = typer.Option(
        None,
        '--data-service',
        help='Name of specific data-service to look within',
    ),
    dataflow: str = typer.Option(
        None,
        '--dataflow',
        help='Name of specific dataflow to look within',
    ),
    regex: Optional[bool] = typer.Option(False, help='Match names using regex expressions instead of simple contains string'),
    kind: Optional[str] = typer.Option('source,view,sink,pub,sub', help='Kinds of components to search one or more comma separated: source,view,sink,pub,sub)'),
):
  if not criteria:
    return []

  def _match_fields(comp, find_reg):
    fields = []
    if comp.schema:
      for field in comp.schema.map.field:
        fields.append(field)
    if comp.view:
      for field in comp.view.status.schema.map.field:
        fields.append(field)
    if comp.source:
      for field in comp.source.status.schema.map.field:
        fields.append(field)
    for field in fields:
      if find_reg.match(field.name):
        return comp

  def _match_source(comp, find_reg):
    # serialize to json to make the search simpler
    json_str = json.dumps(comp, cls=JSONDefinitionEncoder)
    jsonpath_expr = parse('*..inline')
    for match in jsonpath_expr.find(json.loads(json_str)):
      if find_reg.match(match.value):
        return comp
    return None

  client = get_client(ctx)
  data = {}
  find_re = re_matcher(criteria, regex)
  for ds in client.list_data_services().data:
    if not data_service or ds.id == data_service or ds.name == data_service:
      for df in client.list_dataflows(ds.id).data:
        if not dataflow or df.name == dataflow or df.id == dataflow:
          for df_component in client.list_dataflow_components(ds.id, df.id, deep=True, kind=kind).data:
            if find_by in [FindBy.FIELD, FindBy.ALL]:
              match_component = _match_fields(df_component, find_re)
              if match_component:
                data[match_component.uuid] = match_component
            if find_by in [FindBy.NAME, FindBy.ALL]:
              if find_re.match(df_component.name) or find_re.match(df_component.id):
                data[df_component.uuid] = df_component
            if find_by in [FindBy.SOURCE, FindBy.ALL]:
              if _match_source(df_component, find_re):
                data[df_component.uuid] = df_component
            if find_by in [FindBy.METADATA, FindBy.ALL]:
              if find_re.match(df_component.description):
                data[df_component.uuid] = df_component

  print_response(ctx, list(data.values()))
