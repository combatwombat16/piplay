import sys, json, socket
sys.path.append("../")
from getSenseHatStats import get_stats
from getSystemInfo import get_sysinfo
from helpers.helpers import get_datetime
import json
import socket

def make_stat_dict(name, payload):
	return {"host": socket.gethostname().split(".")[0], "type": name, "data": payload, "timestamp": get_datetime()["epoch"]}

def dict_to_line_protocol(stat):
	"%s,host=%s %s" % (stat["type"], stat["host"], stat["epoch"])

stats = []
#stats.append(make_stat_dict("DateTime", get_datetime()))
#stats.append(make_stat_dict("Sense_Imperial", get_stats("imperial")))
stats.append(make_stat_dict("Sense_Metric", get_stats("metric")))
#stats.append(make_stat_dict("System", get_sysinfo("imperial")))
stats.append(make_stat_dict("System", get_sysinfo("metric")))

print(json.dumps(stats))
