import concurrent
import logging as log
import re
from concurrent.futures import ThreadPoolExecutor
from typing import List

import typer
from ascend.sdk.client import Client
from google.protobuf.json_format import MessageToDict
from ascend_io_cli.support import get_client, print_response

app = typer.Typer(help='Refresh read connectors', no_args_is_help=True)


def _refresh_connectors(ctx: typer.Context, data_service_id: str, dataflow_id: str, component_ids: [], reset_err: bool):
  """Actually call the refresh component method for read connectors"""

  def _refresh(sdk_client: Client, service_id: str, flow_id: str, c_id: str, reset: bool):
    return sdk_client.refresh_read_connector(service_id, flow_id, c_id, reset).data

  results = []
  with ThreadPoolExecutor(max_workers=int(ctx.obj.workers)) as executor:
    client = get_client(ctx)
    futures = [executor.submit(_refresh, client, data_service_id, dataflow_id, c, reset_err) for c in component_ids]

    for future in concurrent.futures.as_completed(futures, timeout=220.0):
      result = future.result(31.0)
      results.append(MessageToDict(result))

  return results


@app.command()
def component(
    ctx: typer.Context,
    data_service_id: str = typer.Argument(..., help='Data Service id', show_default=False),
    dataflow_id: str = typer.Argument(..., help='Dataflow id', show_default=False),
    component_id: List[str] = typer.Argument(..., help='List of component ids to resume', show_default=False),
    regex: bool = typer.Option(False, help='Connector list is a list of regular expressions to match with connector ids'),
    reset: bool = typer.Option(True, help='Reset errors automatically when refreshing the connector'),
):
  """Refresh a list of read connectors"""
  dataflow_components = get_client(ctx).list_dataflow_components(data_service_id, dataflow_id, deep=False, kind='source', state='').data

  if regex and component_id:
    # expand the list using the regex into the actual components to resume
    expanded = []
    for p in [re.compile(c) for c in component_id]:
      log.debug(f'Expanding component selection regex {p.pattern}')
      expanded.extend([c.id for c in dataflow_components if p.match(c.id)])
    component_id = expanded

  refreshed = _refresh_connectors(ctx, data_service_id, dataflow_id, component_id, reset)
  log.debug(f'Refreshed {len(refreshed)} connectors')
  print_response(ctx, refreshed)


@app.command()
def dataflow(
    ctx: typer.Context,
    data_service_id: str = typer.Argument(..., help='Data Service id', show_default=False),
    dataflow_id: str = typer.Argument(..., help='Dataflow id', show_default=False),
    reset: bool = typer.Option(True, help='Reset errors automatically when refreshing the connector'),
):
  """Refresh all components in a dataflow"""
  component(ctx, data_service_id, dataflow_id, ['.*'], regex=True, reset=reset)
