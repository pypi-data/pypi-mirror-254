import requests
import json
import os


# baas-dev02.ap-southeast-1.elasticbeanstalk.com/v1/baas/data/redis/cmd/im_resource_id/hlen

def _get_redis_basic_url(host: str, resource_id: str):
  # resource_id = os.environ.get("BAAS_REDIS_RESOURCE_ID")
  # host = os.environ.get("BAAS_REDIS_SERVER_HOST")
  return f"{host}/v1/baas/data/redis/cmd/{resource_id}/"
  
class RemoteError(Exception):
  """
  远程服务器返回的错误
  """
  code = None
  http_status = None
  message = None
  data = None
  def __init__(self, code:str, http_code:str, message:str, data:dict, *args, **kwargs):
    self.code = code
    self.http_code = http_code
    self.message = message
    self.data = data
    super().__init__(*args, **kwargs)
  def __str__(self) -> str:
    return f"remote error, http_status: {self.http_code}, code: {self.code}, message: {self.message}"

_SYSTEM_ERROR_CODE = "1220002"


def _parse_redis_response(resp:requests.Response):
  if resp.status_code != 200:
    try:
      ret = resp.json()
      err = "unknown err"
      if "ResponseMetadata" in ret:
        err = ret["ResponseMetadata"]["Error"]
    except Exception:
      raise RemoteError(_SYSTEM_ERROR_CODE, resp.status_code, f"unexpected response, status code: {resp.status_code}, message: {resp.text}", None)
    raise RemoteError(err["Code"],resp.status_code, err["Message"], err["Data"])
  try:
    ret = resp.json()
    if "Result" not in ret:
      raise RemoteError(_SYSTEM_ERROR_CODE, resp.status_code, f"unexpected response, status code: {resp.status_code}, message: {resp.text}", None)
    json_val = json.loads(ret["Result"]["JSONStr"])
    return json_val
  except:
    raise RemoteError(_SYSTEM_ERROR_CODE, resp.status_code, f"unexpected response, status code: {resp.status_code}, message: {resp.text}", None)

def _redis_query(host: str, resource_id: str, redis_method: str, args):
  # 每个参数转成 string
  args = [str(arg) for arg in args]
  # 将数据转换为 JSON 格式
  json_data = json.dumps({"Args": args})
  # 设置请求头部信息
  headers = {
    "Content-Type": "application/json"
  }
  resp = requests.post(_get_redis_basic_url(host, resource_id)+redis_method, json_data, headers=headers)
  return _parse_redis_response(resp)

# redis_query(["pythonsdk_hset", "field001", "value001"])
# final_res = redis_query("hget",["pythonsdk_hset", "field001"])
# final_res = redis_query("set",["pythonsdk_set001", "v1"])
# final_res = redis_query("set",["pythonsdk_set002", "v2"])
# final_res = redis_query("get",["pythonsdk_set001"])
# final_res = redis_query("expire",["pythonsdk_set001", 10])
# final_res = redis_query("mget",["pythonsdk_set001", "pythonsdk_set002", "pythonsdk_set003"])
# final_res = redis_query("mget",[ "pythonsdk_set002"])
# final_res = redis_query("hset",[ "pythonsdk_hset002","f03","v03"])

# final_res = redis_query("hgetall",[ "pythonsdk_hset002"])


# print("final_res", final_res, final_res["f03"], final_res["f02"])
