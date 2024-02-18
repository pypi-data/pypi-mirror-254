from typing import Union as _Union,List as _List,Tuple as _Tuple
# import sys
# sys.path.append(r"/cloudide/workspace/baas-sdk-python/src/")
from .remote.redis_api import redis_query as _redis_query
from .remote.config import get_baas_redis_resource_arr as _get_baas_redis_resource_arr,get_baas_server_host as _get_baas_server_host, get_baas_redis_server_host as _get_baas_redis_server_host


class _RedisClass:
  def __init__(self, host: str, resource_id: str):
    self.host = host
    self.resource_id = resource_id
    self.timeout = 10
  def set_timeout(self, timeout: _Union[float, _Tuple[float, float]]):
    self.timeout = timeout
  def delete(self, key: str, *other_keys: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "del", [key, *other_keys])
  def exists(self, key: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "exists", [key])
  def expire(self, key: str, seconds: int) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "expire", [key, seconds])
  def expireat(self, key: str, timestamp: int) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "expireat", [key, timestamp])
  def persist(self, key: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "persist", [key])
  def pexpire(self, key: str, milliseconds: int) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "pexpire", [key, milliseconds])
  def pexpireat(self, key: str, timestamp: int) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "pexpireat", [key, timestamp])
  def pttl(self, key: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "pttl", [key])
  def ttl(self, key: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "ttl", [key])
  def type(self, key: str) -> str:
    return _redis_query(self.host, self.resource_id, self.timeout, "type", [key])
  def append(self, key: str, value: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "append", [key, value])
  def bitcount(self, key: str, start: int, end: int) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "bitcount", [key, start, end])
  def decr(self, key: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "decr", [key])
  def decrby(self, key: str, num: int) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "decrby", [key, num])
  def get(self, key: str) -> _Union[str, None]:
    return _redis_query(self.host, self.resource_id, self.timeout, "get", [key])
  def getbit(self, key: str, offset: int) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "getbit", [key, offset])
  def getrange(self, key: str, start: int, end: int) -> str:
    return _redis_query(self.host, self.resource_id, self.timeout, "getrange", [key, start, end])
  def getset(self, key: str, new_value: str) -> str:
    return _redis_query(self.host, self.resource_id, self.timeout, "getset", [key, new_value])
  def incr(self, key: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "incr", [key])
  def incrby(self, key: str, num: int) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "incrby", [key, num])
  def incrbyfloat(self, key: str, num: float) -> float:
    return _redis_query(self.host, self.resource_id, self.timeout, "incrbyfloat", [key, num])
  def mget(self, key: str, *other_keys: str) -> _List[_Union[str, None]]:
    return _redis_query(self.host, self.resource_id, self.timeout, "mget", [key, *other_keys])
  def psetex(self, key: str, milliseconds: int, value: str) -> str:
    return _redis_query(self.host, self.resource_id, self.timeout, "psetex", [key, milliseconds, value])
  def set(self, key: str, value: str, set_type_or_expire_mode: _Union[str, None]=None, expire: _Union[int, None]=None, set_type: _Union[str, None] = None) -> _Union[str, None]:
    """
    usage:
    set(key: str, value: str)
    set(key: str, value: str, set_type: 'nx' | 'xx')
    set(key: str, value: str, expire_mode: 'ex' | 'px', expire: int)
    set(key: str, value: str, expire_mode: 'ex' | 'px', expire: int, set_type: 'nx' | 'xx')
    """
    input = tuple(filter(lambda x: x is not None, [key, value, set_type_or_expire_mode, expire, set_type]))
    return _redis_query(self.host, self.resource_id, self.timeout, "set", input)
  def mset(self, key: str, value: str, *key_or_value: str) -> str:
    return _redis_query(self.host, self.resource_id, self.timeout, "mset", [key, value, *key_or_value])
  def setbit(self, key: str, offset: int, value: int) -> str:
    """
    usage:
    setbit(key: str, offset: int, value: 0 | 1)
    """
    return _redis_query(self.host, self.resource_id, self.timeout, "setbit", [key, offset, value])
  def setex(self, key: str, seconds: int, value: str) -> str:
    return _redis_query(self.host, self.resource_id, self.timeout, "setex", [key, seconds, value])
  def setnx(self, key: str, value: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "setnx", [key, value])
  def setrange(self, key: str, offset: int, value: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "setrange", [key, offset, value])
  def strlen(self, key: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "strlen", [key])
  def hdel(self, key: str, value: str, *other_values: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "hdel", [key, value, *other_values])
  def hexists(self, key: str, field: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "hexists", [key, field])
  def hget(self, key: str, field: str) -> _Union[str, None]:
    return _redis_query(self.host, self.resource_id, self.timeout, "hget", [key, field])
  def hgetall(self, key: str) -> dict[str, str]:
    return _redis_query(self.host, self.resource_id, self.timeout, "hgetall", [key])
  def hincrby(self, key: str, field: str, increment: int) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "hincrby", [key, field, increment])
  def hincrbyfloat(self, key: str, field: str, increment: float) -> float:
    return _redis_query(self.host, self.resource_id, self.timeout, "hincrbyfloat", [key, field, increment])
  def hkeys(self, key: str) -> _List[str]:
    return _redis_query(self.host, self.resource_id, self.timeout, "hkeys", [key])
  def hlen(self, key: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "hlen", [key])
  def hmget(self, key: str, field: str, *other_field: str) -> _List[_Union[str, None]]:
    return _redis_query(self.host, self.resource_id, self.timeout, "hmget", [key, field, *other_field])
  def hmset(self, key: str, field:str, value:str, *field_or_value: str) -> str:
    """
    hmset(key: str, field1: str, value1: str, field2: str, value2: str, ...)
    """
    return _redis_query(self.host, self.resource_id, self.timeout, "hmset", [key, field, value, *field_or_value])
  def hset(self, key: str, field: str, value: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "hset", [key, field, value])
  def hsetnx(self, key: str, field: str, value: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "hsetnx", [key, field, value])
  def hvals(self, key: str) -> _List[str]:
    return _redis_query(self.host, self.resource_id, self.timeout, "hvals", [key])
  def lindex(self, key: str, index: int) -> _Union[str, None]:
    return _redis_query(self.host, self.resource_id, self.timeout, "lindex", [key, index])
  def llen(self, key: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "llen", [key])
  def lpop(self, key: str) -> _Union[str, None]:
    return _redis_query(self.host, self.resource_id, self.timeout, "lpop", [key])
  def lpush(self, key: str, field: str, *other_fields: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "lpush", [key, field, *other_fields])
  def lpushx(self, key: str, field: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "lpushx", [key, field])
  def lrange(self, key: str, start: int, end: int) -> _List[str]:
    return _redis_query(self.host, self.resource_id, self.timeout, "lrange", [key, start, end])
  def lset(self, key: str, index: int, value: str) -> str:
    return _redis_query(self.host, self.resource_id, self.timeout, "lset", [key, index, value])
  def ltrim(self, key: str, start: int, end: str) -> str:
    return _redis_query(self.host, self.resource_id, self.timeout, "ltrim", [key, start, end])
  def rpop(self, key: str) -> _Union[str, None]:
    return _redis_query(self.host, self.resource_id, self.timeout, "rpop", [key])
  def rpoplpush(self, source: str, destination: str) -> _Union[str, None]:
    return _redis_query(self.host, self.resource_id, self.timeout, "rpoplpush", [source, destination])
  def rpush(self, key: str, field: str, *other_fields: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "rpush", [key, field, *other_fields])
  def rpushx(self, key: str, field: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "rpushx", [key, field])
  def sadd(self, key: str, field: str, *other_fields: str) -> int:
    """
    if want key be in same slot
    sadd("\{pythonsdk_set002\}:somekey", "one","two","zero","two")
    """
    return _redis_query(self.host, self.resource_id, self.timeout, "sadd", [key, field, *other_fields])
  def sdiff(self, key: str, *other_keys: str) -> _List[str]:
    return _redis_query(self.host, self.resource_id, self.timeout, "sdiff", [key, *other_keys])
  def sdiffstore(self, destination: str, key: str, *other_keys: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "sdiffstore", [destination, key, *other_keys])
  def sinter(self, key: str, *other_keys: str) -> _List[str]:
    return _redis_query(self.host, self.resource_id, self.timeout, "sinter", [key, *other_keys])
  def sinterstore(self, destination: str, key: str, *other_keys: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "sinterstore", [destination, key, *other_keys])
  def sismember(self, key: str, member: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "sismember", [key, member])
  def smembers(self, key: str) -> _List[str]:
    return _redis_query(self.host, self.resource_id, self.timeout, "smembers", [key])
  def smove(self, source: str, destination: str, member: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "smove", [source, destination, member])
  def spop(self, key: str, count: _Union[int, None] = None) -> _List[str]:
    input = tuple(filter(lambda x: x is not None, [key, count]))
    return _redis_query(self.host, self.resource_id, self.timeout, "spop", input)
  def srandmember(self, key: str, count: _Union[int, None] = None) -> _List[str]:
    input = tuple(filter(lambda x: x is not None, [key, count]))
    return _redis_query(self.host, self.resource_id, self.timeout, "srandmember", input)
  def srem(self, key: str, field: str, *other_fields: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "srem", [key, field, *other_fields])
  def sunion(self, key: str, *other_keys: str) -> _List[str]:
    return _redis_query(self.host, self.resource_id, self.timeout, "sunion", [key, *other_keys])
  def sunionstore(self, destination: str, key: str, *other_keys: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "sunionstore", [destination, key, *other_keys])
  def zadd(self, key: str, score: float, member: str,*other_score_or_member: _Union[str, int]) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "zadd", [key, score, member, *other_score_or_member])
  def zcard(self, key: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "zcard", [key])
  def zcount(self, key: str, min: _Union[str, int], max: _Union[str, int]) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "zcount", [key, min, max])
  def zincrby(self, key: str, increment: float, member: str) -> float:
    return _redis_query(self.host, self.resource_id, self.timeout, "zincrby", [key, increment, member])
  def zrange(self, key: str, start: int, end: int, withscores: _Union[str, None] = None) -> _List[str]:
    """
    zrange(key: str, start: int, end: int, withscores: 'withscores')
    """
    input = tuple(filter(lambda x: x is not None, [key, start, end, withscores]))
    return _redis_query(self.host, self.resource_id, self.timeout, "zrange", input)
  def zrangebyscore(self, key: str, min: _Union[str, int], max: _Union[str, int]) -> _List[str]:
    return _redis_query(self.host, self.resource_id, self.timeout, "zrangebyscore", [key, min, max])
  def zrank(self, key: str, member: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "zrank", [key, member])
  def zrem(self, key: str, member: str, *other_members: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "zrem", [key, member, *other_members])
  def zremrangebyrank(self, key: str, start: int, end: int) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "zremrangebyrank", [key, start, end])
  def zremrangebyscore(self, key: str, min: _Union[str, int], max: _Union[str, int]) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "zremrangebyscore", [key, min, max])
  def zrevrange(self, key: str, start: int, end: int, withscores: _Union[str, None] = None) -> _List[str]:
    """
    zrevrange(key: str, start: int, end: int, withscores: 'withscores')
    """
    input = tuple(filter(lambda x: x is not None, [key, start, end, withscores]))
    return _redis_query(self.host, self.resource_id, self.timeout, "zrevrange", input)
  def zrevrangebyscore(self, key: str, max: _Union[str, int], min: _Union[str, int]) -> _List[str]:
    return _redis_query(self.host, self.resource_id, self.timeout, "zrevrangebyscore", [key, max, min])
  def zrevrank(self, key: str, member: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "zrevrank", [key, member])
  def zscore(self, key: str, member: str) -> float:
    return _redis_query(self.host, self.resource_id, self.timeout, "zscore", [key, member])
  def zinterstore(self, destination: str, key_num: int, key: str, *other_keys: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "zinterstore", [destination, key_num, key, *other_keys])
  def zunionstore(self, destination: str, key_num: int, key: str, *other_keys: str) -> int:
    return _redis_query(self.host, self.resource_id, self.timeout, "zunionstore", [destination, key_num, key, *other_keys])

redis: _RedisClass
redis_clients: dict[str, _RedisClass] = {}

_resource_arr = _get_baas_redis_resource_arr()
_baas_host = _get_baas_server_host()
_inner_redis_host = _get_baas_redis_server_host()

_redis_host = ""
if _inner_redis_host is not None:
  _redis_host = _inner_redis_host
elif _baas_host is not None:
  _redis_host = _baas_host
else:
  print("[WARNING] Redis SDK: No BaaS Host Config found.")
  raise Exception("No BaaS Host Config found.")


for _resource in _resource_arr:
  redis_clients[_resource.id] = _RedisClass(_redis_host, _resource.id)

if len(_resource_arr) > 0:
  redis = redis_clients[_resource_arr[0].id]


def delete(key: str, *other_keys: str) -> int:
  return redis.delete(key, *other_keys)
def exists(key: str) -> int:
  return redis.exists(key)
def expire(key: str, seconds: int) -> int:
  return redis.expire(key, seconds)
def expireat(key: str, timestamp: int) -> int:
  return redis.expireat(key, timestamp)
def persist(key: str) -> int:
  return redis.persist(key)
def pexpire(key: str, milliseconds: int) -> int:
  return redis.pexpire(key, milliseconds)
def pexpireat(key: str, timestamp: int) -> int:
  return redis.pexpireat(key, timestamp)
def pexpireat(key: str, timestamp: int) -> int:
  return redis.pexpireat(key, timestamp)
def pttl(key: str) -> int:
  return redis.pttl(key)
def ttl(key: str) -> int:
  return redis.ttl(key)
def type(key: str) -> str:
  return redis.type(key)
def append(key: str, value: str) -> int:
  return redis.append(key, value)
def bitcount(key: str, start: int, end: int) -> int:
  return redis.bitcount(key, start, end)
def decr(key: str) -> int:
  return redis.decr(key)
def decrby(key: str, num: int) -> int:
  return redis.decrby(key, num)
def get(key: str) -> _Union[str, None]:
  return redis.get(key)
def getbit(key: str, offset: int) -> int:
  return redis.getbit(key, offset)
def getrange(key: str, start: int, end: int) -> str:
  return redis.getrange(key, start, end)
def getset(key: str, new_value: str) -> str:
  return redis.getset(key, new_value)
def incr(key: str) -> int:
  return redis.incr(key)
def incrby(key: str, num: int) -> int:
  return redis.incrby(key, num)
def incrbyfloat(key: str, num: float) -> float:
  return redis.incrbyfloat(key, num)
def mget(key: str, *other_keys: str) -> _List[_Union[str, None]]:
  return redis.mget(key, *other_keys)
def psetex(key: str, milliseconds: int, value: str) -> str:
  return redis.psetex(key, milliseconds, value)
def set(key: str, value: str, set_type_or_expire_mode: _Union[str, None]=None, expire: _Union[int, None]=None, set_type: _Union[str, None] = None) -> _Union[str, None]:
  """
  usage:
  set(key: str, value: str)
  set(key: str, value: str, set_type: 'nx' | 'xx')
  set(key: str, value: str, expire_mode: 'ex' | 'px', expire: int)
  set(key: str, value: str, expire_mode: 'ex' | 'px', expire: int, set_type: 'nx' | 'xx')
  """
  input = tuple(filter(lambda x: x is not None, [key, value, set_type_or_expire_mode, expire, set_type]))
  return redis.set(input)
def mset(key: str, value: str, *key_or_value: str) -> str:
  return redis.mset(key, value, *key_or_value)
def setbit(key: str, offset: int, value: int) -> str:
  """
  usage:
  setbit(key: str, offset: int, value: 0 | 1)
  """
  return redis.setbit(key, offset, value)
def setex(key: str, seconds: int, value: str) -> str:
  return redis.setex(key, seconds, value)
def setnx(key: str, value: str) -> int:
  return redis.setnx(key, value)
def setrange(key: str, offset: int, value: str) -> int:
  return redis.setrange(key, offset, value)
def strlen(key: str) -> int:
  return redis.strlen(key)
def hdel(key: str, value: str, *other_values: str) -> int:
  return redis.hdel(key, value, *other_values)
def hexists(key: str, field: str) -> int:
  return redis.hexists(key, field)
def hget(key: str, field: str) -> _Union[str, None]:
  return redis.hget(key, field)
def hgetall(key: str) -> dict[str, str]:
  return redis.hgetall(key)
def hincrby(key: str, field: str, increment: int) -> int:
  return redis.hincrby(key, field, increment)
def hincrbyfloat(key: str, field: str, increment: float) -> float:
  return redis.hincrbyfloat(key, field, increment)
def hkeys(key: str) -> _List[str]:
  return redis.hkeys(key)
def hlen(key: str) -> int:
  return redis.hlen(key)
def hmget(key: str, field: str, *other_field: str) -> _List[_Union[str, None]]:
  return redis.hmget(key, field, *other_field)
def hmset(key: str, field:str, value:str, *field_or_value: str) -> str:
  """
  hmset(key: str, field1: str, value1: str, field2: str, value2: str, ...)
  """
  return redis.hmset(key, field, value, *field_or_value)
def hset(key: str, field: str, value: str) -> int:
  return redis.hset(key, field, value)
def hsetnx(key: str, field: str, value: str) -> int:
  return redis.hsetnx(key, field, value)
def hvals(key: str) -> _List[str]:
  return redis.hvals(key)
def lindex(key: str, index: int) -> _Union[str, None]:
  return redis.lindex(key, index)
def llen(key: str) -> int:
  return redis.llen(key)
def lpop(key: str) -> _Union[str, None]:
  return redis.lpop(key)
def lpush(key: str, field: str, *other_fields: str) -> int:
  return redis.lpush(key, field, *other_fields)
def lpushx(key: str, field: str) -> int:
  return redis.lpushx(key, field)
def lrange(key: str, start: int, end: int) -> _List[str]:
  return redis.lrange(key, start, end)
def lset(key: str, index: int, value: str) -> str:
  return redis.lset(key, index, value)
def ltrim(key: str, start: int, end: str) -> str:
  return redis.ltrim(key, start, end)
def rpop(key: str) -> _Union[str, None]:
  return redis.rpop(key)
def rpoplpush(source: str, destination: str) -> _Union[str, None]:
  return redis.rpoplpush(source, destination)
def rpush(key: str, field: str, *other_fields: str) -> int:
  return redis.rpush(key, field, *other_fields)
def rpushx(key: str, field: str) -> int:
  return redis.rpushx(key, field)
def sadd(key: str, field: str, *other_fields: str) -> int:
  """
  if want key be in same slot
  sadd("\{pythonsdk_set002\}:somekey", "one","two","zero","two")
  """
  return redis.sadd(key, field, *other_fields)
def sdiff(key: str, *other_keys: str) -> _List[str]:
  return redis.sdiff(key, *other_keys)
def sdiffstore(destination: str, key: str, *other_keys: str) -> int:
  return redis.sdiffstore(destination, key, *other_keys)
def sinter(key: str, *other_keys: str) -> _List[str]:
  return redis.sinter(key, *other_keys)
def sinterstore(destination: str, key: str, *other_keys: str) -> int:
  return redis.sinterstore(destination, key, *other_keys)
def sismember(key: str, member: str) -> int:
  return redis.sismember(key, member)
def smembers(key: str) -> _List[str]:
  return redis.smembers(key)
def smove(source: str, destination: str, member: str) -> int:
  return redis.smove(source, destination, member)
def spop(key: str, count: _Union[int, None] = None) -> _List[str]:
  input = tuple(filter(lambda x: x is not None, [key, count]))
  return redis.spop(input)
def srandmember(key: str, count: _Union[int, None] = None) -> _List[str]:
  input = tuple(filter(lambda x: x is not None, [key, count]))
  return redis.srandmember(input)
def srem(key: str, field: str, *other_fields: str) -> int:
  return redis.srem(key, field, *other_fields)
def sunion(key: str, *other_keys: str) -> _List[str]:
  return redis.sunion(key, *other_keys)
def sunionstore(destination: str, key: str, *other_keys: str) -> int:
  return redis.sunionstore(destination, key, *other_keys)
def zadd(key: str, score: float, member: str,*other_score_or_member: _Union[str, int]) -> int:
  return redis.zadd(key, score, member, *other_score_or_member)
def zcard(key: str) -> int:
  return redis.zcard(key)
def zcount(key: str, min: _Union[str, int], max: _Union[str, int]) -> int:
  return redis.zcount(key, min, max)
def zincrby(key: str, increment: float, member: str) -> float:
  return redis.zincrby(key, increment, member)
def zrange(key: str, start: int, end: int, withscores: _Union[str, None] = None) -> _List[str]:
  """
  zrange(key: str, start: int, end: int, withscores: 'withscores')
  """
  input = tuple(filter(lambda x: x is not None, [key, start, end, withscores]))
  return redis.zrange(input)
def zrangebyscore(key: str, min: _Union[str, int], max: _Union[str, int]) -> _List[str]:
  return redis.zrangebyscore(key, min, max)
def zrank(key: str, member: str) -> int:
  return redis.zrank(key, member)
def zrem(key: str, member: str, *other_members: str) -> int:
  return redis.zrem(key, member, *other_members)
def zremrangebyrank(key: str, start: int, end: int) -> int:
  return redis.zremrangebyrank(key, start, end)
def zremrangebyscore(key: str, min: _Union[str, int], max: _Union[str, int]) -> int:
  return redis.zremrangebyscore(key, min, max)
def zrevrange(key: str, start: int, end: int, withscores: _Union[str, None] = None) -> _List[str]:
  """
  zrevrange(key: str, start: int, end: int, withscores: 'withscores')
  """
  input = tuple(filter(lambda x: x is not None, [key, start, end, withscores]))
  return redis.zrevrange(input)
def zrevrangebyscore(key: str, max: _Union[str, int], min: _Union[str, int]) -> _List[str]:
  return redis.zrevrangebyscore(key, max, min)
def zrevrank(key: str, member: str) -> int:
  return redis.zrevrank(key, member)
def zscore(key: str, member: str) -> float:
  return redis.zscore(key, member)
def zinterstore(destination: str, key_num: int, key: str, *other_keys: str) -> int:
  return redis.zinterstore(destination, key_num, key, *other_keys)
def zunionstore(destination: str, key_num: int, key: str, *other_keys: str) -> int:
  return redis.zunionstore(destination, key_num, key, *other_keys)