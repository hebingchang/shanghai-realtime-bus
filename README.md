# Shanghai Realtime Bus

「上海公交」APP 的 Python 实现

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

TODO

## The MIT License

Copyright 2019 hebingchang

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

