# Shanghai Realtime Bus

「上海公交」APP 的 Python 实现。

好用请 Star~

## Installation

`pip install shbus`

## Usage

### 线路查询

```
>>> import shbus.lineinfo
>>> basic_info = shbus.lineinfo.LineInfo('江川7路')
>>> print(basic_info)
Bus
东川路地铁站 交通大学(闵行校区) 06:00 20:30
交通大学(闵行校区) 东川路地铁站 06:10 20:40
```

### 实时公交

```
>>> import shbus.realtime
>>> client = shbus.realtime.client()
>>> response = client.getRealtimeBus('虹桥枢纽4路', 30).items[0]
>>> print('%s: 还剩%s站, 距离%s米, 还剩%s秒' % (response.vehicle, response.stops, response.distance, response.time))
沪D-D6957: 还剩2站, 距离1354米, 还剩153秒
```

具体参见 example 目录下的测试脚本。

## Principle

### 数据结构

「上海公交」APP 有两种数据结构，分别用于普通的线路查询以及实时公交查询。

1. 线路查询所返回的数据结构:

    貌似是项目组自己实现的二进制格式，需要逐比特位分析。
    
    - 字节: 1字节，通常转为10进制使用
    - 整型：4字节
    - 字符串：前4字节表示字符串的长度 n，后 2 * n 个字节是字符串的 UTF-16LE 编码表示
    - 浮点数：4字节。先转换为整型，再调用 Java 自带的 intBitsToFloat 转换为浮点数

2. 实时公交所返回的数据结构:
    
    是经过 AES CBC 加密的 Protobuf 结构化消息。解析起来有两个难点：如何找到 AES 的加密秘钥和初始向量；以及如何构造 Protobuf 消息的结构。这里不多赘述。

### 线路查询

「上海公交」的线路查询功能共有3个接口：

1. 搜索接口:
    `http://lbs.jt.sh.cn:8088/linePrompt`

    用于模糊查询公交线路名称。例如：`http://lbs.jt.sh.cn:8088/lineInfo?name=132`
    
    接口返回的数据需要先经过 base64 解码，如果返回的线路列表长度大于1，则需要再使用 zlib 解压缩，否则无需进一步处理。
    
    对于上一步返回的数据，需要逐字节解析：
    
    - 先读取一个整型，代表线路列表的长度 n
    - 再根据上一步获取的长度，连续读取 n 个字符串，即得线路列表

2. 线路基本信息:
    `http://lbs.jt.sh.cn:8088/lineInfo`
    
    用于查询线路的始末站以及首末班车时间。
    
    接口返回的数据同样需要经过 base64 解码后使用 zlib 解压缩。
    
    数据解析:
    
    - 先读取1个字节，代表该线路的类型 (0: 公交, 1: 地铁, 2: 轮渡)
    - 随后读取4个字符串，分别是：上行起始站、上行终点站、上行首班车时间、上行末班车时间。
    - 如果此时还有数据未读，则再读4个字符串，作为下行的信息。

3. 线路详细信息:
    `http://lbs.jt.sh.cn:8088/lineDetail`
    
    返回一条线路上行或下行的所有站点以及其位置。
    
    原理与上述类似，具体参见代码。

### 实时公交查询

`http://lbs.jt.sh.cn:8082/app/rls/monitor`

需要先用 Protobuf 构造一条请求消息，将其使用 AES 加密后 POST 到上述 URL，接收到信息后再使用 AES 解密后用 Protobuf 解包。具体详见代码。

## The MIT License

Copyright 2019

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

