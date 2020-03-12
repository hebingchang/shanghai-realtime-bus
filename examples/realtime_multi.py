import shbus.realtime

client = shbus.realtime.client()
results = client.batch([
    {
        'line': '虹桥枢纽4路',
        'direction': True,
        'info': True,
        'sequence': 41
    },
    {
        'line': '虹桥枢纽4路',
        'direction': True,
        'info': False,
        'sequence': 40
    }
])

for result in results:
    print(result)