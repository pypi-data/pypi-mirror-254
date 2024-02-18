import requests
import json
import os
import a0_baas_sdk.remote.auth as auth
from . import utils
from typing import Union as _Union,Tuple as _Tuple


def _get_redis_basic_url(host: str, resource_id: str):
  return f"{host}/v1/baas/data/redis/cmd/{resource_id}/"


_SYSTEM_ERROR_CODE = "1220002"


def _parse_redis_response(resp:requests.Response):
  res = utils._parse_response(resp)
  try:
    if "JSONStr" not in res:
      raise utils.RemoteError(_SYSTEM_ERROR_CODE, resp.status_code, f"unexpected response, status code: {resp.status_code}, message: {resp.text}", None)
    json_val = json.loads(res["JSONStr"])
    return json_val
  except:
    raise utils.RemoteError(_SYSTEM_ERROR_CODE, resp.status_code, f"unexpected response, status code: {resp.status_code}, message: {resp.text}", None)

def redis_query(host: str, resource_id: str, timeout: _Union[float, _Tuple[float, float]], redis_method: str, args):
  args = [str(arg) for arg in args]
  json_data = json.dumps({"Args": args})
  auth_header = auth.get_auth_header(resource_id)
  headers = {
    "Content-Type": "application/json"
  }
  headers.update(auth_header)
  resp = requests.post(_get_redis_basic_url(host, resource_id)+redis_method, json_data, headers=headers, timeout=_get_timeout(timeout))
  return _parse_redis_response(resp)


def _get_timeout(timeout: _Union[float, _Tuple[float, float]]):
  if isinstance(timeout, tuple):
    return timeout
  else:
    return (5, timeout)

