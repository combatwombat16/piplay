from getDateTimeInfo import get_datetime
from getSenseHatStats import get_stats
from getSystemInfo import get_sysinfo
import json
import socket

def make_stat_dict(name, payload):
	return {"host": socket.gethostname().split(".")[0], "type": name, "data": payload}

stats = []
stats.append(make_stat_dict("DateTime", get_datetime()))
stats.append(make_stat_dict("Sense", get_stats()))
stats.append(make_stat_dict("System", get_sysinfo()))

print(json.dumps(stats))
