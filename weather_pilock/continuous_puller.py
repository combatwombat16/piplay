import sys, json, socket
sys.path.append("../")
from SenseHat_Data import Sensor
from helpers import get_datetime



def make_stat_dict(name, payload):
        return {"host": socket.gethostname().split(".")[0], "type": name, "data": payload, "timestamp": get_datetime()["epoch"]}

def dict_to_line_protocol(stat):
        "%s,host=%s %s" % (stat["type"], stat["host"], stat["epoch"])

stats = []
#stats.append(make_stat_dict("DateTime", get_datetime()))
#stats.append(make_stat_dict("Sense_Imperial", get_stats("imperial")))
#stats.append(make_stat_dict("Sense_Metric", get_stats("metric")))
#stats.append(make_stat_dict("System", get_sysinfo("imperial")))
#stats.append(make_stat_dict("System", get_sysinfo("metric")))

senseHat = Sensor("metric")

i = 0

while i < 100:
	#stats.append(make_stat_dict("Sense_Metric", get_stats("metric")))
	senseHat.add()
	i += 1

print(json.dumps(senseHat.data_dict))
