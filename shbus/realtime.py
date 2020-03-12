import requests, base64
from shbus.protos import Response_pb2, Request_pb2, NameSet_pb2
from Crypto.Cipher import AES
from google.protobuf.any_pb2 import Any
import shbus.utils, shbus.consts


class client:
    def __init__(self):
        r = requests.get('http://lbs.jt.sh.cn:8082/app/rls/names')
        target = NameSet_pb2.NameSet()
        target.ParseFromString(r.content)
        self.lines = target.names

    def getAllLines(self):
        return self.lines

    def __sendRequest(self, objs):
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

    def getRealtimeBus(self, line, sequence=1, direction=True, info=True):
        target = Request_pb2.Sequence()
        target.direction = direction
        target.info = info
        target.line = line
        target.sequence = sequence

        data = self.__sendRequest([target])

        response = Response_pb2.Response()
        response.ParseFromString(data)
        type, value = response.items[0].type_url, response.items[0].value

        if type == '/protoc.Response.Dispatch':
            dispatch = Response_pb2.Dispatch()
            dispatch.ParseFromString(value)
            return dispatch
        elif type == '/protoc.Response.Monitor':
            monitor = Response_pb2.Monitor()
            monitor.ParseFromString(value)
            return monitor
        elif type == '/protoc.Response.Error':
            error = Response_pb2.Error()
            error.ParseFromString(value)
            print(error.message)
            return error
        else:
            print(type)
            return None

    def batch(self, lines):
        # mostly same as getRealtimeBus
        targets = list()
        for line in lines:
            target = Request_pb2.Sequence()
            target.direction = line['direction']
            target.info = line['info']
            target.line = line['line']
            target.sequence = line['sequence']
            targets.append(target)

        data = self.__sendRequest(targets)

        response = Response_pb2.Response()
        response.ParseFromString(data)

        results = list()
        for item in response.items:
            type, value = item.type_url, item.value

            if type == '/protoc.Response.Dispatch':
                dispatch = Response_pb2.Dispatch()
                dispatch.ParseFromString(value)
                results.append(dispatch)
            elif type == '/protoc.Response.Monitor':
                monitor = Response_pb2.Monitor()
                monitor.ParseFromString(value)
                results.append(monitor)
            elif type == '/protoc.Response.Error':
                error = Response_pb2.Error()
                error.ParseFromString(value)
                print(error.message)
                results.append(error)
            else:
                print(type)

        return results
