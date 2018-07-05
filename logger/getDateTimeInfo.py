#! /usr/bin/python3

from datetime import datetime
import pytz

def get_datetime():
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
	return datetime_dict

