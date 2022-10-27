import requests

from shbus.protos import NameSet_pb2
from shbus.models import *

__NAMESET__ = NameSet_pb2.NameSet()
__NAMESET__.ParseFromString(requests.get('http://lbs.jt.sh.cn:8082/app/rls/names').content)
__ALL_LINES__ = __NAMESET__.names
