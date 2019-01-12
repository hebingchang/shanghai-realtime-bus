import shbus.lineinfo

def printStations(stations):
    for index, station in enumerate(stations):
        print('%s. %s' % (index + 1, station.name))

options = shbus.lineinfo.linePrompt(input('线路名称: '))
if not len(options):
    print('未找到线路。')
    exit(-1)

for index, name in enumerate(options[1]):
    print('%s. %s' % (index + 1, name))
line_name = options[1][int(input('请选择线路 (%s-%s): ' % (1, len(options[1])))) - 1]
print('已选择: %s' % line_name)

basic_info = shbus.lineinfo.LineInfo(line_name)

print('上行:')
print('首末班车时间: %s-%s' % (basic_info.up.early_time, basic_info.up.last_time))
detail_info = shbus.lineinfo.LineDetail(line_name)
printStations(detail_info.stations)
print()

if basic_info.bidirection:
    print('下行:')
    print('首末班车时间: %s-%s' % (basic_info.down.early_time, basic_info.down.last_time))
    detail_info = shbus.lineinfo.LineDetail(line_name, up=False)
    printStations(detail_info.stations)
