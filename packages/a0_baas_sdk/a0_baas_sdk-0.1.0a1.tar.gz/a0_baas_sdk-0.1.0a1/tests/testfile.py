import sys
import os
sys.path = [os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))] + sys.path
import a0_baas_sdk.file as file
import a0_baas_sdk.remote.auth as auth
import a0_baas_sdk.remote.utils as utils
import requests

@utils.retry(0, 1)
def func():
  print("excuted")
  raise Exception()

if __name__ == "__main__":
  # fd = file.upload("test.txt", open("test.txt", "rb"), timeout=(1, 10))
  # print(fd.url)
  # print(fd.id)
  # resp = file.download(fd.id,timeout=(1, 10))
  # file.delete(fd.id,timeout=(1, 10))
  # try:
  #   file.download(fd.id, timeout=(1, 10))
  # except file.FileNotFound:
  #   print("can not download deleted file can not")
  func()