import sys, json
sys.path.append("../")

class JsonSerializable(object):
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    def __repr__(self):
        return self.toJson()

def convertCToF(tempInC):
	return (tempInC * 1.8) + 32

def convertmbToPSI(pressureInmb):
	return (0.0145037738 * pressureInmb)

def get_datetime():
	from datetime import datetime
	import pytz
	datetime_dict = {}
	dt = datetime.now(tz=pytz.utc)
	datetime_dict["year"] = dt.year
	datetime_dict["month"] = dt.month
	datetime_dict["day"] = dt.day
	datetime_dict["hour"] = dt.hour
	datetime_dict["minute"] = dt.minute
	datetime_dict["second"] = dt.second
	datetime_dict["microsecond"] = dt.microsecond
	datetime_dict["tz"] = 0
	datetime_dict["timezone"] = "UTC"
	datetime_dict["timestamp"] = dt.isoformat()
	datetime_dict["epoch"] = int(dt.timestamp() * 1000)
	return datetime_dict
