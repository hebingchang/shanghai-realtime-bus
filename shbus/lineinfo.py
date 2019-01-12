import zlib, base64, requests, struct

def intBitsToFloat(b):
   s = struct.pack('>l', b)
   return struct.unpack('>f', s)[0]

class Reader:
    def __init__(self, buf):
        self.buf = buf
        self.offset = 0

    def readByte(self):
        buf = self.buf[self.offset]
        self.offset += 1
        return buf

    def readInt(self):
        buf = self.buf[self.offset] & 255 | self.buf[self.offset + 1] << 8 | self.buf[self.offset + 2] << 16 | self.buf[self.offset + 3] << 24
        self.offset += 4
        return buf

    def readString(self):
        length = self.readInt()
        buf = self.buf[self.offset:self.offset + 2 * length].decode('utf-16-le')

        self.offset += length * 2
        return buf

    def readFloat(self):
        accum = int(
            (int
             (int((int(int((int(self.buf[self.offset] & 255))
                  | ((int(self.buf[self.offset + 1] & 255)) << 8))))
                  | ((int(self.buf[self.offset + 2] & 255)) << 16))))
                  | ((int(self.buf[self.offset + 3] & 255)) << 24)
        )

        self.offset += 4
        return intBitsToFloat(accum)

class Direction:
    def __init__(self, reader):
        self.first_station, self.last_station, self.early_time, self.last_time = reader.readString(), reader.readString(), reader.readString(), reader.readString()

    def __str__(self):
        return ' '.join([self.first_station, self.last_station, self.early_time, self.last_time])

class Coord:
    def __init__(self, reader):
        self.longitude = reader.readFloat()
        self.latitude = reader.readFloat()

    def __str__(self):
        return '%s, %s' % (self.longitude, self.latitude)

class Station:
    def __init__(self, reader):
        self.name = reader.readString()
        self.coord = Coord(reader)

    def __str__(self):
        return " ".join([self.name, str(self.coord)])

class Section:
    def __init__(self, reader):
        self.count = reader.readInt()
        self.coords = []
        for i in range(self.count):
            self.coords.append(Coord(reader))

class LineInfo:
    _types = ['Bus', 'Metro', 'Ferry']

    def __init__(self, lineName):
        r = requests.get('http://lbs.jt.sh.cn:8088/lineInfo?name=' + lineName)
        if r.content == b'':
            raise ValueError('线路不存在。')

        data = base64.b64decode(r.content)
        self.buf = zlib.decompress(data)

        self.bidirection = False
        self.reader = Reader(self.buf)
        self.__parse__()

    def __parse__(self):
        self.type = self._types[self.reader.readByte()]
        self.up = Direction(self.reader)
        if self.reader.readByte() > 0:
            self.down = Direction(self.reader)
            self.bidirection = True

    def __str__(self):
        return '\n'.join([self.type, str(self.up), str(self.down)])

class LineDetail:
    def __init__(self, lineName, up=True):
        r = requests.get('http://lbs.jt.sh.cn:8088/lineDetail?name=%s&up=%s' % (lineName, {True: 'true', False: 'false'}[up]))
        if r.content == b'':
            raise ValueError('参数错误。')

        data = base64.b64decode(r.content)
        self.buf = zlib.decompress(data)
        self.reader = Reader(self.buf)

        self.__parse__()

    def __parse__(self):
        self.station_count = self.reader.readInt()
        self.stations = []
        for i in range(self.station_count):
            station = Station(self.reader)
            self.stations.append(station)

        self.section_count = self.reader.readInt()
        self.sections = []
        for i in range(self.section_count):
            self.sections.append(Section(self.reader))

def linePrompt(keyword):
    r = requests.get('http://lbs.jt.sh.cn:8088/linePrompt?key=' + keyword)
    data = base64.b64decode(r.content)
    try:
        data = zlib.decompress(data)
    except:
        pass
    reader = Reader(data)
    count = reader.readInt()
    results = []
    for i in range(count):
        results.append(reader.readString())

    return count, results
