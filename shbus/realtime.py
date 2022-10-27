from typing import List

from shbus import __ALL_LINES__, utils
from shbus.models import LineSequence
from shbus.protos import Response_pb2, Request_pb2


def get_all_lines() -> List[str]:
    return __ALL_LINES__


def get_realtime_bus(lines: List[LineSequence]) -> List[
    Response_pb2.Dispatch | Response_pb2.Monitor | Response_pb2.Error]:
    targets = list()
    for line in lines:
        target = Request_pb2.Sequence()
        target.direction = line.direction
        target.info = line.info
        target.line = line.line
        target.sequence = line.sequence
        targets.append(target)

    data = utils.__proto_request(targets)

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
            results.append(error)
        else:
            pass

    return results
