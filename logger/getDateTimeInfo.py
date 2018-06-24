from datetime import datetime

def get_datetime():
	datetime_dict = {}
	dt = datetime.utcnow()
	datetime_dict["year"] = dt.year
	datetime_dict["month"] = dt.month
	datetime_dict["day"] = dt.day
	datetime_dict["hour"] = dt.hour
	datetime_dict["minute"] = dt.minute
	datetime_dict["second"] = dt.second
	datetime_dict["microsecond"] = dt.microsecond
	datetime_dict["timezone"] = 0
	return datetime_dict
