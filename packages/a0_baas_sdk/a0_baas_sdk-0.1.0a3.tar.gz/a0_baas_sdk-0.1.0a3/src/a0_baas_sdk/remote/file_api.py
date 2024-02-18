import os
import hashlib
import base64
from typing import Tuple, Union
import requests
import a0_baas_sdk.remote.auth as auth
from . import utils
from .config import get_baas_server_host, get_baas_file_resource_id
from urllib3.util import Retry
from requests import Session
from requests.adapters import HTTPAdapter


class File(object):
  id: str
  name: str
  size: int
  checksum_md5: str
  url: str
  def __init__(self, id, name, size, url) -> None:
    self.id=id
    self.name=name
    self.size=size
    self.url=url

class PresignResult(object):
  url:str
  file:File
  additional_header:dict
  def __init__(self, url, file, additional_header) -> None:
    self.url=url
    self.file=file
    self.additional_header=additional_header

def _get_upload_presign_url(resource_id:str):
  return f"{get_baas_server_host()}/v1/baas/data/file/api/resource/{resource_id}/put/presign"

def _get_delete_url(resource_id:str,file_id:str):
  return f"{get_baas_server_host()}/v1/baas/data/file/api/resource/{resource_id}/file/{file_id}"

def _get_get_url(resource_id:str,file_id:str):
  return f"{get_baas_server_host()}/v1/baas/data/file/api/resource/{resource_id}/file/{file_id}"

def presign_upload_file(data:bytes, name:str,resource_id:str, timeout:Union[float, Tuple[float]])->PresignResult:
  checksum = hashlib.md5(data).digest()
  checksum_base64 = base64.b64encode(checksum).decode('utf-8')
  url = _get_upload_presign_url(resource_id)
  print(url)
  resp = _get_baas_session().get(url, data={
    "Name": name,
    "Size": len(data),
    "CheckSumMD5":checksum_base64
  },headers=auth.get_auth_header(resource_id), timeout=_get_timeout(timeout))
  presign_resp = utils._parse_response(resp)
  print
  file_desc = presign_resp["File"]
  file = File(file_desc["ID"], file_desc["Name"], file_desc["Size"], file_desc["URL"])
  return PresignResult(presign_resp["URL"], file, presign_resp["AdditionalHeader"])

def delete(file_id:str,resource_id:str, timeout:Union[float, Tuple[float, float]]=10)->None:
  """
  删除文件
  """
  url = _get_delete_url(resource_id,file_id)
  resp = _get_baas_session().delete(url, headers=auth.get_auth_header(resource_id), timeout=_get_timeout(timeout))
  return utils._parse_response(resp)

def get_file_info(file_id:str,resource_id:str, timeout:Union[float, Tuple[float]])->File:
  """
  通过 file_id 下载文件
  """
  url = _get_get_url(resource_id, file_id)
  resp = _get_baas_session().get(url, headers=auth.get_auth_header(resource_id), timeout=_get_timeout(timeout))
  file_resp = utils._parse_response(resp)
  if file_resp is None:
    return None
  return File(file_resp["ID"], file_resp["Name"], file_resp["Size"], file_resp["URL"])

def get_s3_session()->Session:
  s = Session()
  return s
  # retries = Retry(
  #     total=3,
  #     backoff_factor=0.1,
  #     status_forcelist=[502, 503, 504],
  #     allowed_methods={'POST'},
  # )
  # s.mount('http://', HTTPAdapter(max_retries=retries))
  # s.mount('https://', HTTPAdapter(max_retries=retries))

def _get_baas_session()->Session:
  s = Session()
  return s

def _get_timeout(timeout):
  if isinstance(timeout, tuple):
    return timeout
  else:
    return (0.1, timeout)

def get_s3_timeout(timeout):
  if isinstance(timeout, tuple):
    return timeout
  else:
    return (0.1, timeout)
  