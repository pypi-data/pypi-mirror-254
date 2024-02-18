from typing import Union as _Union
# import sys
# sys.path.append(r"/cloudide/workspace/baas-sdk-python/src/")
from .remote.redis_api import _redis_query
from .remote.config import get_baas_redis_resource_id_arr as _get_baas_redis_resource_id_arr,get_baas_server_host as _get_baas_server_host


class _RedisClass:
  def __init__(self, host: str, resource_id: str):
    self.host = host
    self.resource_id = resource_id
  def hget(self, key: str, field: str) -> _Union[str, None]:
    return _redis_query(self.host, self.resource_id, "hget", [key, field])
  def get(self, key: str) -> _Union[str, None]:
    return _redis_query(self.host, self.resource_id, "get", [key])
  def set(self, key: str, value: str) -> str:
    return _redis_query(self.host, self.resource_id, "set", [key, value])

redis: _RedisClass
redis_clients: dict[str, _RedisClass] = {}

_resource_id_arr = _get_baas_redis_resource_id_arr()
_redis_host = _get_baas_server_host()

for _resource_id in _resource_id_arr:
  redis_clients[_resource_id] = _RedisClass(_redis_host, _resource_id)

if len(_resource_id_arr) > 0:
  redis = redis_clients[_resource_id_arr[0]]

# # 调用方法
# result = redis.hget("pythonsdk_hset002", "f02")

# # 打印结果
# print("result", result)