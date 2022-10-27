import base64

import requests
from google.protobuf.any_pb2 import Any
from Crypto.Cipher import AES

import shbus.consts
from shbus.protos import Request_pb2


def unpad(s):
    if s[-1] != "\r":
        return s[0:-s[-1]]
    else:
        return s.rstrip()


def __proto_request(objs):
    items = []
    for obj in objs:
        request_any = Any()
        request_any.Pack(obj)
        items.append(request_any)

    request = Request_pb2.Request()
    request.items.extend(items)
    data = request.SerializeToString()

    length = 16 - (len(data) % 16)
    data += bytes([length]) * length

    aes = AES.new(shbus.consts.key, shbus.consts.aes_mode, shbus.consts.iv)
    data = aes.encrypt(data)

    payload = {'request': base64.b64encode(data)}
    r = requests.post(shbus.consts.MONITOR_URL, data=payload)

    aes = AES.new(shbus.consts.key, shbus.consts.aes_mode, shbus.consts.iv)
    return shbus.utils.unpad(aes.decrypt(r.content))
