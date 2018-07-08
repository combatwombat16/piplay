#! /bin/python3

from sense_hat import SenseHat
from helpers import convertCToF, convertmbToPSI

sense = SenseHat()
sense.clear()
sense.set_imu_config(True, True, True)

def get_stats(impOrMet):
	stat_dict = {}
	#% relative
	stat_dict["humidity"] = sense.get_humidity()
	if (impOrMet == "imperial"):
		stat_dict["temperature_from_humidity"] = convertCToF(sense.get_temperature_from_humidity())
		stat_dict["temperature_from_pressure"] = convertCToF(sense.get_temperature_from_pressure())
		stat_dict["pressure"] = convertmbToPSI(sense.get_pressure())
	else:
		stat_dict["temperature_from_humidity"] = sense.get_temperature_from_humidity()
		stat_dict["temperature_from_pressure"] = sense.get_temperature_from_pressure()
		stat_dict["pressure"] = sense.get_pressure()
	stat_dict["orientation_radians"] = sense.get_orientation_radians()
	stat_dict["orientation_degress"] = sense.get_orientation_degrees()
	#magnetic intensity in microteslas
	stat_dict["compass_raw"] = sense.get_compass_raw()
	#rotational intensity in radians per second
	stat_dict["gyroscope_raw"] = sense.get_gyroscope_raw()
	#acceleration intensity in Gs
	stat_dict["accelerometer_raw"] = sense.get_accelerometer_raw()
	#stat_dict["timestamp"] = get_datetime()["timestamp"]
	return stat_dict

