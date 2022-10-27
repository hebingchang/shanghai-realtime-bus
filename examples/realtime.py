from shbus import realtime
from shbus import LineSequence

keyword = input('线路名称: ')

options = list(filter(lambda line: keyword in line, realtime.get_all_lines()))
if not len(options):
    print('线路不存在。')
    exit(-1)

for index, item in enumerate(options):
    print('%s. %s' % (index + 1, item))

line_name = options[int(input('请选择线路 (%s-%s): ' % (1, len(options)))) - 1]
responses = realtime.get_realtime_bus([LineSequence(line=line_name, info=True)])
assert len(responses) > 0
response = responses[0]

print('已选择: %s' % response.info.name)
if len(response.info.routes) > 1:
    for i in range(len(response.info.routes)):
        print('%s. %s->%s' % (i + 1, response.info.routes[i].names[0], response.info.routes[i].names[-1]))
    direction = not bool(int(input('请选择方向 (1/2): ')) - 1)

    for index, station in enumerate(response.info.routes[int(not direction)].names):
        print('%s. %s' % (index + 1, station))

    sequence = int(input('请选择站点 (%s-%s): ' % (1, len(response.info.routes[int(not direction)].names)))) - 1
    station_name = response.info.routes[int(not direction)].names[sequence]
    responses = realtime.get_realtime_bus(
        [LineSequence(line=line_name, sequence=int(sequence), direction=direction, info=False)])
    assert len(responses) > 0
    response = responses[0]

    print()
    print('%s站:' % station_name)
    for index, bus in enumerate(response.items):
        if hasattr(bus, 'stops'):
            print('%s. %s: 距离%s站, %s米, 还有%s分钟' % (
                index + 1, bus.vehicle, bus.stops, bus.distance, round(bus.time / 60)))
        elif hasattr(bus, 'time'):
            print(
                '%s. %s: %s发车' % (index + 1, bus.vehicle, bus.time))
        else:
            print('暂未发车')
