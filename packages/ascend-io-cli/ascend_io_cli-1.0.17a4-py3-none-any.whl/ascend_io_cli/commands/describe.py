import logging as log
import re
from typing import Optional

import glog
import typer
from google.protobuf.json_format import MessageToDict

from ascend_io_cli.commands.support.lineage_support import LineageSupport, OutputFormat
from ascend_io_cli.support import get_client, print_response, COMPONENT_STATE_METHODS, COMPONENT_PARTITIONS_METHODS

app = typer.Typer(help='Get data service, dataflow, and component details', no_args_is_help=True)


@app.command()
def component(
    ctx: typer.Context,
    data_service_id: Optional[str] = typer.Argument(..., help='Data Service id'),
    dataflow_id: Optional[str] = typer.Argument(..., help='Dataflow id'),
    component_id: Optional[str] = typer.Argument(..., help='Component id'),
):
  """Get component details"""
  client = get_client(ctx)
  data = [c for c in client.list_dataflow_components(data_service_id=data_service_id, dataflow_id=dataflow_id, deep=True).data if c.id == component_id]

  print_response(ctx, data[0])


def _component_states(ctx: typer.Context, data_service_id: str, dataflow_id: str, component_ids: [], regex: bool = False) -> {}:
  client = get_client(ctx)

  response = {}
  found_components = client.list_dataflow_components(
      data_service_id=data_service_id,
      dataflow_id=dataflow_id,
      deep=True,
  ).data

  if regex:
    extended = {}
    for p in [re.compile(c) for c in component_ids]:
      log.debug(f'Expanding component selection regex {p.pattern}')
      extended.update({c.id: c for c in found_components if p.match(c.id)})
    found_components = list(extended.values())

  # ignore groups
  for c in [fc for fc in found_components if fc.type not in ['group']]:
    method = getattr(client, COMPONENT_STATE_METHODS[c.type], None)
    if method:
      response.update({c.id: MessageToDict(method(data_service_id, dataflow_id, c.id).data)})
  return response


@app.command()
def component_state(
    ctx: typer.Context,
    data_service_id: str = typer.Argument(..., help='Data Service id'),
    dataflow_id: str = typer.Argument(..., help='Dataflow id'),
    component_id: str = typer.Argument(..., help='Component id'),
):
  """Get component state information"""

  response = _component_states(ctx, data_service_id, dataflow_id, [component_id])
  print_response(ctx, list(response.values())[0] if response else [])


@app.command()
def dataflow(
    ctx: typer.Context,
    data_service_id: str = typer.Argument(..., help='Data Service id'),
    dataflow_id: str = typer.Argument(..., help='Dataflow id'),
):
  """Get dataflow details"""
  client = get_client(ctx)
  data = [f for f in client.list_dataflows(data_service_id=data_service_id).data if f.id == dataflow_id]

  print_response(ctx, data[0])


@app.command()
def dataflow_state(
    ctx: typer.Context,
    data_service_id: str = typer.Argument(..., help='Data Service id'),
    dataflow_id: str = typer.Argument(..., help='Dataflow id'),
    summarize: bool = typer.Option(False, help='Produce a summary of the component composite states'),
):
  """Get dataflow details"""
  component_states = _component_states(ctx, data_service_id, dataflow_id, ['.*'], regex=True)

  if summarize:
    for k, v in component_states.items():
      component_states.update({k: {'upToDate': 'upToDate' in v['state']['compositeState'], 'uuid': v['uuid']}})
    print_response(ctx, component_states)
  else:
    print_response(ctx, component_states)


@app.command()
def data_service(
    ctx: typer.Context,
    data_service_id: str = typer.Argument(..., help='Data Service id'),
):
  """Get data service details"""
  client = get_client(ctx)
  data = [ds for ds in client.list_data_services().data if ds.id == data_service_id]

  print_response(ctx, data[0])


@app.command()
def lineage(ctx: typer.Context,
            data_service_id: str = typer.Argument(..., help='Data service id containing the flow and component to analyze'),
            dataflow_id: str = typer.Argument(..., help='Dataflow id containing the component to analyze'),
            component_id: str = typer.Argument(..., help='The component to use when describing the lineage flowing from end to end'),
            upstream: bool = typer.Option(False, help='Describe upstream lineage relative to the context component'),
            downstream: bool = typer.Option(False, help='Describe downstream lineage relative to the context component'),
            readers: bool = typer.Option(False, help='Describe readers for the lineage passing through the context component'),
            writers: bool = typer.Option(False, help='Describe writers for the lineage starting with the context component'),
            details: bool = typer.Option(False, help='Include component details such as schema and query information'),
            output: OutputFormat = typer.Option(None, help='Output the [bold green]entire[/bold green] graph in the specified format')):
  """Discover upstream, downstream, or all lineage relative to a supplied component id."""
  lineage_support = LineageSupport(get_client(ctx))
  lineage_graph = lineage_support.build_graph(data_service_id, dataflow_id, component_id, details=details)

  if output:
    str_out = output.generate(lineage_graph.graph)
    # override any contex specified in the command
    ctx.obj.output = 'objects'
    print_response(ctx, str_out)
  else:
    if readers:
      glog.debug('Process readers only')
      print_response(ctx, lineage_graph.readers())
    elif writers:
      glog.debug('Process writers only')
      print_response(ctx, lineage_graph.writers())
    elif not (upstream or downstream):
      glog.debug('Process lineage end-to-end')
      print_response(ctx, lineage_graph.end_to_end())
    elif upstream:
      glog.debug('Process lineage upstream only')
      print_response(ctx, lineage_graph.upstream())
    elif downstream:
      glog.debug('Process lineage downstream only')
      print_response(ctx, lineage_graph.downstream())


@app.command()
def partitions(
    ctx: typer.Context,
    data_service_id: str = typer.Argument(..., help='Data Service id', show_default=False),
    dataflow_id: str = typer.Argument(..., help='Dataflow id', show_default=False),
    component_id: str = typer.Argument(..., help='Component id', show_default=False),
    batch_size: int = typer.Option(100, help='Adjust the number of partitions to fetch per batch', hidden=True),
    latest: bool = typer.Option(False, help='Return only the most recently updated partition'),
):
  """Return a list the partition details for a component or just the newest partition."""
  client = get_client(ctx)

  dataflow_components = client.list_dataflow_components(data_service_id, dataflow_id, deep=False, kind='source,view,sink').data
  found_components = [df for df in dataflow_components if df.id == component_id]
  if not found_components:
    log.warning(f"{data_service_id}.{dataflow_id}.{component_id} not found (must be read connector, transform, or write connector)")
    raise typer.Exit(code=1)

  found_component = found_components[0]
  offset = 0
  method = getattr(client, COMPONENT_PARTITIONS_METHODS[found_component.type])
  found_partitions = []
  # the number of partitions is unknown, fetch until there are none left
  parts = method(data_service_id, dataflow_id, component_id, offset=offset, limit=batch_size).data.data.metadata
  while len(parts):
    offset += len(parts)
    found_partitions.extend([MessageToDict(p) for p in parts])
    parts = method(data_service_id, dataflow_id, component_id, offset=offset, limit=batch_size).data.data.metadata

  if latest:
    time_dict = dict(
        sorted({
            v['statistics']['dimensions']['__last_updated__']['maximum']['timestampValue']: v
            for v in found_partitions
            if v.get('statistics', {}).get('dimensions', {}).get('__last_updated__', {}).get('maximum', {}).get('timestampValue', None)
        }.items()))
    if time_dict:
      print_response(ctx, [time_dict[list(time_dict.keys())[-1]]])
    else:
      raise ValueError(f'Could not find any up to date partitions in {data_service_id}.{dataflow_id}.{component_id}')
  else:
    print_response(ctx, found_partitions)
