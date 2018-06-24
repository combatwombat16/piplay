from getDateTimeInfo import get_datetime
from getSenseHatStats import get_stats
from getSystemInfo import get_sysinfo
import json

stats = []
stats.append({"host": "", "type": "datetime", "data": get_datetime()})
stats.append({"host": "", "type": "sense", "data": get_stats()})
stats.append({"host": "", "type": "system", "data": get_sysinfo()})

print(json.dumps(stats))
