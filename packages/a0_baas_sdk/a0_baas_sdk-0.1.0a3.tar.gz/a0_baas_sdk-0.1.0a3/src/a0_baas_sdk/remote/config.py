import os
import json
import traceback
from . import const

def get_baas_server_host():
  return os.environ.get("baas_host")

def get_baas_resource_conf():
  return os.environ.get(const.RESOURCE_ENVIRON_KEY)

def get_baas_file_resource_id():
  cnf = os.environ.get(const.RESOURCE_ENVIRON_KEY)
  resource = json.loads(cnf)
  for r in resource:
    if r["Type"]==const.RESOURCE_TYPE_FILE:
      return r["ResourceID"]
  return None

def get_baas_redis_resource_id_arr():
  cnf = os.environ.get(const.RESOURCE_ENVIRON_KEY)
  resource = json.loads(cnf)
  arr = []
  for r in resource:
    if r["Type"]==const.RESOURCE_TYPE_REDIS:
      arr.append(r["ResourceID"])
  return arr

def get_baas_api_timeout(api:str):
  try:
    cnf = os.environ.get("BaaSAPITimeout")
    timeouts = json.load(cnf)
    return timeouts[api]
  except Exception as e:
    # set default to 10s
    traceback.print_exc()
    return 10

def get_s3_connect_timeout()->int:
  return 10

def _init():
  global resource_info
  resource_info = []
  from . import config
  import json
  cnf = config.get_baas_resource_conf()
  resource_configs = json.loads(cnf)
  for resource in resource_configs:
    resource_info.append(_Resources(
      resource["Type"],
      resource["ResourceID"],
      resource["Secret"]
    ))
class _Resources(object):
  resource_type:str = None
  secret:str = None
  id:str = None

  def __init__(self, resource_type, id, secret) -> None:
    self.id = id
    self.secret = secret
    self.resource_type = resource_type

def get_resource_info_by_id(id:str)->_Resources:
  for resource in resource_info:
    if resource.id == id:
      return resource
  return None

_init()
