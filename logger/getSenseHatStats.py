#! /bin/python3

from sense_hat import SenseHat
import json

sense = SenseHat()
sense.clear()
sense.set_imu_config(True, True, True)

def get_stats():
	stat_dict = {}
	stat_dict["humidity"] = sense.get_humidity()
	stat_dict["temperature_from_humidity"] = sense.get_temperature_from_humidity()
	stat_dict["pressure"] = sense.get_pressure()
	stat_dict["temperature_from_pressure"] = sense.get_temperature_from_pressure()
	stat_dict["orientation_radians"] = sense.get_orientation_radians()
	stat_dict["orientation_degress"] = sense.get_orientation_degrees()
	stat_dict["compass_raw"] = sense.get_compass_raw()
	stat_dict["gyroscope_raw"] = sense.get_gyroscope_raw()
	stat_dict["accelerometer_raw"] = sense.get_accelerometer_raw()
	return stat_dict
