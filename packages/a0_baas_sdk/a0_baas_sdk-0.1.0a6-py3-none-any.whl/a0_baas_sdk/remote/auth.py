import os
from . import config
import typing
import time
import requests
from . import utils
import json
from . import const

tokens = {}

TOKEN_DECAY_SECONDS = 15*60

def get_auth_header(resource_id):
  """
  获取session
  """
  if os.environ.get("DEBUG") == "true":
    return {"X-Jwt-Data": "{"+f'"project_id":"project_a", "resource_id":"{config.get_baas_file_resource_id()}"'+"}"}
  else:
    if resource_id not in tokens or time.time()>tokens[resource_id][1]:
      refresh_token(resource_id)
    return {"X-Baas-Token": tokens[resource_id][0]}


@utils.retry(2, 0.1)
def refresh_token(resource_id):
  """
  刷新token
  """
  resource = config.get_resource_info_by_id(resource_id)
  resp = requests.post(_get_token_url(),json={
      "ResourceID": resource.id,
      "Secret": resource.secret
    },
    headers={
      "Content-Type": "application/json"
    },
    timeout=(1, 10))
  token = utils._parse_response(resp)
  expireAt = time.time()+token["ExpireSecond"] - TOKEN_DECAY_SECONDS
  tokens[resource_id] = (token["Token"], expireAt)

def _get_token_url():
  return f"{config.get_baas_server_host()}/v1/baas/control/get_token"