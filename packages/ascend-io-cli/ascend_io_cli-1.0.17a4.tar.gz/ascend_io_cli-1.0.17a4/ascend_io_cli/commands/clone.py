#!/usr/bin/env python3
import importlib.util
import json
import logging
import os
import re
import tempfile
from datetime import datetime
from pathlib import Path

import ascend.protos.ascend.ascend_pb2 as ascend
import ascend.protos.connection.connection_pb2 as connection
import typer
from ascend.protos.io.io_pb2 import Credentials as ContainerCredentials
from ascend.sdk import definitions
from ascend.sdk.applier import DataflowApplier, DataServiceApplier, ComponentApplier
from ascend.sdk.definitions import DataService, Credential, Connection, ReadConnector, WriteConnector, Transform, ComponentUuidType
from ascend.sdk.render import download_dataflow, TEMPLATES_V2, download_data_service

from ascend_io_cli.support import get_client, print_response

app = typer.Typer(name='clone', help='Clone data services and dataflows', no_args_is_help=True)


## helper functions
def _to_ascend_value(v):
  if type(v) == dict:
    return ascend.Value(struct_value=ascend.Struct(fields=_dict_to_ascend_values(v)))
  elif type(v) == list:
    return ascend.Value(list_value=ascend.Values(values=_list_to_ascend_values(v)))
  types = {
      bool: "bool_value",
      int: "int_value",
      str: "string_value",
  }
  return ascend.Value(**{types[type(v)]: v})


def _dict_to_ascend_values(d):
  return {k: _to_ascend_value(d[k]) for k in d}


def _list_to_ascend_values(d):
  return [_to_ascend_value(k) for k in d]


def _load_json_str(details):
  if os.path.isfile(details):
    with open(details, 'r') as f:
      details = f.read()
  return json.loads(details)


def _hydrate_credential(credential_id: str, credential_type: str, credential_details: str):
  credential_details = _load_json_str(credential_details)

  return Credential(
      id=credential_id,
      name=credential_id,
      credential=ContainerCredentials(
          connection=connection.Credentials(type_id=connection.Type.Id(value=credential_type, ), details=_dict_to_ascend_values(credential_details))))


def _hydrate_connection(connection_id: str, connection_type: str, connection_details: str, credential_id: str):
  """We can accept config as either a string, or a file path. details are usually as follows:
  {
    'host': 'YOUR_HOSTNAME',
    'database': 'YOUR_DATABASE_NAME'
  }
  """
  connection_details = _load_json_str(connection_details)

  return Connection(
      id=connection_id,
      name=connection_id,
      type_id=connection_type,
      credential_id=credential_id,
      details=_dict_to_ascend_values(connection_details),
      access_mode=connection.AccessMode(read_only=connection.AccessMode.ReadOnly(), ),
  )


def _hydrate_component(data_service_id: str, dataflow_id: str, component_id: str, base_dir: str):
  v2_name = Path(base_dir).resolve().joinpath(f'{component_id}.py')
  file = next(filter(lambda x: os.path.exists(x), [v2_name]), None)
  if not file:
    raise Exception(f"component file for {data_service_id}.{dataflow_id}.{component_id} not found at {base_dir}")
  logging.debug(f'Loading at {file}')
  spec = importlib.util.spec_from_file_location("local", file)
  module_d = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(module_d)
  return vars(module_d)['component']


def _hydrate_dataflow(data_service_id: str, dataflow_id: str, new_data_service_id, new_dataflow_id: str, base_dir: str):
  v2_name = Path(base_dir).resolve().joinpath(f'{dataflow_id}.py')
  file = next(filter(lambda x: os.path.exists(x), [v2_name]), None)
  if not file:
    raise Exception(f"dataflow file for {data_service_id}.{dataflow_id} not found at {v2_name}")
  logging.debug(f'Loading at {file}')
  spec = importlib.util.spec_from_file_location("local", file)
  module_d = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(module_d)
  return vars(module_d)['construct_dataflow'](new_data_service_id, new_dataflow_id)


def _hydrate_data_service(data_service_id: str, new_data_service_id: str, base_dir: str):
  v2_name = Path(base_dir).resolve().joinpath(f'{data_service_id}.py')
  file = next(filter(lambda x: os.path.exists(x), [v2_name]), None)
  if not file:
    raise Exception(f"dataservice file for {data_service_id} not found at {base_dir}")
  logging.debug(f'Loading at {file}')
  spec = importlib.util.spec_from_file_location("local", file)
  module_d = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(module_d)
  return vars(module_d)['construct_data_service'](new_data_service_id)


@app.command()
def dataflow(
    ctx: typer.Context,
    from_service: str = typer.Argument("", help='Data Service id to copy from', show_default=False),
    from_dataflow: str = typer.Argument("", help='Dataflow id to clone', show_default=False),
    new_dataflow_id: str = typer.Argument("", help='Dataflow id to create', show_default=False),
    to_data_service: str = typer.Option(None, "--to-data-service", help='Data Service id to copy to or from-data-service if omitted', show_default=False),
    template_dir: str = typer.Option(TEMPLATES_V2, '--template_dir', show_default=False),
):
  """Clone an existing dataflow within the current data service or to a new one"""
  client = get_client(ctx)

  to_data_service = to_data_service if to_data_service else from_service

  existing_flow = [df for df in client.list_dataflows(data_service_id=to_data_service).data if df.id == new_dataflow_id]
  if existing_flow:
    logging.warning(f"Dataflow '{to_data_service}.{new_dataflow_id}' already exists")
    raise typer.Exit(101)

  with tempfile.TemporaryDirectory() as temp_dir:
    write_dir = Path(temp_dir).resolve().joinpath(f'{from_service}', f'{from_dataflow}')
    write_dir.mkdir(parents=True, exist_ok=True)
    download_dataflow(client, data_service_id=from_service, dataflow_id=from_dataflow, resource_base_path=str(write_dir), template_dir=template_dir)
    hydrated = _hydrate_dataflow(from_service, from_dataflow, to_data_service, new_dataflow_id, str(write_dir))
    DataflowApplier(client).apply(data_service_id=to_data_service, dataflow=hydrated, delete=True, dry_run=False)
    print_response(ctx, hydrated)


@app.command()
def data_service(
    ctx: typer.Context,
    from_id: str = typer.Argument("", help='Data Service id to copy from', show_default=False),
    new_id: str = typer.Argument("", help='Data Service id to create', show_default=False),
    include_dataflows: bool = typer.Option(False, '--include-dataflows', help='Set to true to additionally copy all dataflows', show_default=False),
):
  """Clone an existing data service to a new name"""
  client = get_client(ctx)

  try:
    svc = client.get_data_service(data_service_id=from_id)
    if not svc.success or not svc.data:
      logging.warning(f'service {from_id} you are copying from does not exist')
      raise typer.Exit(102)
  except Exception as e:
    logging.debug(e)
    logging.warning(f'exception while loading service {from_id}')
    raise typer.Exit(103)

  try:
    svc = client.get_data_service(data_service_id=new_id)
    if svc.success:
      logging.warning(f'service {new_id} already exists')
      raise typer.Exit(104)
  except Exception as e:
    logging.debug(e)
    logging.debug(f'the service name {from_id} is available')

  svc = client.create_data_service(DataService(id=new_id, name=new_id, description=f'Created by Ascend CLI').to_proto()).data
  logging.debug(f"created service '{svc.id}'")

  for conn in client.list_connections(data_service_id=from_id).data:
    if conn.id and conn.id.value:
      logging.info(f"sharing connection '{conn.name}' to new data service '{svc.id}'")
      client.share_connection(connection_id=conn.id.value, data_service_id=from_id, target_data_service_id=svc.id)
    else:
      logging.warning('connection did not have id value to share')

  if include_dataflows:
    with tempfile.TemporaryDirectory() as temp_dir:
      write_dir = Path(temp_dir).resolve().joinpath(f'{from_id}')
      write_dir.mkdir(parents=True, exist_ok=True)
      download_data_service(client, data_service_id=from_id, resource_base_path=str(write_dir), template_dir=TEMPLATES_V2)
      hydrated = _hydrate_data_service(from_id, svc.id, temp_dir)
      DataServiceApplier(client).apply(data_service=hydrated, delete=True, dry_run=False)
      print_response(ctx, hydrated)


ENDS_WITH = re.compile(r"_[0-9]+$")


@app.command()
def component(
    ctx: typer.Context,
    data_service_id: str = typer.Argument(..., help='Data Service id containing the component to clone', show_default=False),
    dataflow_id: str = typer.Argument(..., help='Dataflow id containing the component to clone', show_default=False),
    component_id: str = typer.Argument(..., help='The component as the source of the clone', show_default=False),
    paused: bool = typer.Option(True, help='Set the component in a paused state when creating the clone', show_default=True),
):
  """Clone a component. This is useful for making copies of components. A timestamp based postfix is automatically added to the name to
  make the component unique."""

  client = get_client(ctx)

  # grab the dataflow so we know it exists
  data_flow = client.get_dataflow(data_service_id=data_service_id, dataflow_id=dataflow_id).data
  if not data_flow:
    raise Exception(f'Could not find dataflow {data_service_id}.{dataflow_id}')

  components = client.list_dataflow_components(
      data_service_id,
      dataflow_id,
      deep=True,
  ).data
  target = [c for c in components if c.id == component_id]
  uuid_map = {c.uuid: c.id for c in components}
  id_map = {c.id: definitions.ComponentUuidType(type=c.type, uuid=c.uuid) for c in components}

  if not target:
    raise Exception(f'Could not find component {data_service_id}.{dataflow_id}.{component_id}')

  postfix = f'_{datetime.now().strftime("%Y%m%d%H%M%S")}'
  results = []
  for c in target:
    logging.debug(f'Cloning component {data_service_id}.{dataflow_id}.{c.id}')
    c.uuid = ''
    c.ComponentID = ''
    # postfix name with a timestamp to make it unique
    c.id = f'{c.id}{postfix}' if not ENDS_WITH.findall(c.id) else ENDS_WITH.sub(postfix, c.id)
    c.name = f'{c.name}{postfix}' if not ENDS_WITH.findall(c.name) else ENDS_WITH.sub(postfix, c.name)
    getattr(c, c.type).assigned_priority.paused = paused
    res = {}
    if c.type == 'source':
      res = ComponentApplier(client, id_map).apply(data_service_id, dataflow_id, ReadConnector.from_proto(c))
    elif c.type == 'sink':
      res = ComponentApplier(client, id_map).apply(data_service_id, dataflow_id, WriteConnector.from_proto(c, uuid_map))
    elif c.type == 'view':
      res = ComponentApplier(client, id_map).apply(data_service_id, dataflow_id, Transform.from_proto(c, uuid_map))
    else:
      logging.warning(f'Components of type {c.type} are not supported by cloning.')
    results.append(res)

  return print_response(ctx, results)
