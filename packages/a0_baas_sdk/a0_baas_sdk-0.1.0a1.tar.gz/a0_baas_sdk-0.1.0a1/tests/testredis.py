import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"../src"))

import a0_baas_sdk.redis as redis_module
# from a0_baas_sdk.redis import redis as redis_module


# 调用方法
# result = redis_module.redis.hget("pythonsdk_hset002", "f04")
# result = redis_module.redis_clients["pysdk_resource_id_03"].hget("pythonsdk_hset002", "f02")

result = redis_module.redis_clients["pysdk_resource_id_02"].get("pythonsdk_get001")
# result = redis_module.redis_clients["pysdk_resource_id_02"].set("pythonsdk_get001", "val012")

# 打印结果
print("result", result)
