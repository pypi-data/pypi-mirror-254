import typing as _typing
from .remote import file_api as _api
from .remote.config import get_baas_file_resource_id as _get_baas_file_resource_id

def upload(name:str, file:_typing.Union[bytes, _typing.BinaryIO], timeout:_typing.Union[float, tuple]=10)->_api.File:
  """Upload file.

  :param file: bytes of a file content, or a file-like object, be aware of file size, if limits exceed, exception will be raised.
  :param timeout: (optional) timeout in seconds for the request. if it is a tuple, the first number will be connection timeout, 
    while the second will be read timeout.
  :return: :class:`_api <File>` object
  :rtype: _api.File
  """
  data = None
  if isinstance(file, str):  # 如果是文件名
    with open(file, 'rb') as f:
      data = f.read()
  elif isinstance(file, bytes): # 如果是字节流
    data = file
  elif hasattr(file, 'read'):  # 如果是文件对象
    data = file.read()
  else:
    raise Exception("file type not support")
  resp = _api.presign_upload_file(data, name, _get_baas_file_resource_id(), timeout)
  upload_resp = _api.get_s3_session().put(resp.url, data=data, headers=resp.additional_header, timeout=_api.get_s3_timeout(timeout))
  upload_resp.raise_for_status()
  return resp.file

def download(file_id:str, timeout:_typing.Union[float, tuple]=10):
  """Download file.

  :param file_id: File.id returned by upload function.
  :param timeout: (optional) timeout in seconds for the request. if it is a tuple, the first number will be connection timeout, 
    while the second will be read timeout.
  :return: None
  :rtype: None
  :raises FileNotFound: if provided file id is not found.
  """
  file_desc = _api.get_file_info(file_id, _get_baas_file_resource_id(), timeout)
  if file_desc is None:
    raise FileNotFound
  download_url = file_desc.url
  resp = _api.get_s3_session().get(download_url, timeout=_api.get_s3_timeout(timeout))
  return resp.content

def delete(file_id:str, timeout:_typing.Union[float, tuple]=10):
  """Delete file.

  :param file_id: File.id returned by upload function.
  :param timeout: (optional) timeout in seconds for the request. if it is a tuple, the first number will be connection timeout, 
    while the second will be read timeout.
  :return: None
  :rtype: None
  """
  return _api.delete(file_id, _get_baas_file_resource_id(), timeout)

class FileNotFound(Exception):...