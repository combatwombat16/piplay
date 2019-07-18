#! /bin/python3
import sys, time, math
sys.path.append("../")
from sense_hat import SenseHat
from weather_pilock.helpers import * #convertCToF, convertmbToPSI
from helpers.helpers import *
   
class Reading(JsonSerializable):
    def __init__(self, value, min_value = 0.0, max_value = 1.0):
        self.value = value
        if isinstance(value, int) or isinstance(value, float):
            self.min_value = min(value, min_value)
            self.max_value = max(value, max_value)
        else:
            self.min_value = min_value
            self.max_value = max_value
        

class Sense(JsonSerializable):
    def __init__(self, sensor, system = "imperial"):
        self.system = system
        self.timestamp = get_datetime()["epoch"]
        self.humidity = Reading(sensor.get_humidity(), 0.0, 100.0)
        if (self.system == "imperial"):
            self.temperature_from_humidity = Reading(convertCToF(sensor.get_temperature_from_humidity()), -40.0, 150.0)
            self.temperature_from_pressure = Reading(convertCToF(sensor.get_temperature_from_pressure()), -40.0, 150.0)
            self.pressure = Reading(convertmbToPSI(sensor.get_pressure()), 13.0, 15.0)
        else:
            self.temperature_from_humidity = Reading(sensor.get_temperature_from_humidity(), 0.0, 65.0)
            self.temperature_from_pressure = Reading(sensor.get_temperature_from_pressure(), 0.0, 65.0)
            self.pressure = Reading(sensor.get_pressure(), 250.0, 1250.0)
        self.orientation_radians = Reading(sensor.get_orientation_radians(), {
            "pitch": 0.0,
            "roll": 0.0,
            "yaw": 0.0
        }, {
            "pitch": 2 * math.pi,
            "roll": 2 * math.pi,
            "yaw": 2 * math.pi
        })
        self.orientation_degress = Reading(sensor.get_orientation_degrees(), {
            "pitch": 0.0,
            "roll": 0.0,
            "yaw": 0.0
        }, {
            "pitch": 359.99999,
            "roll": 359.99999,
            "yaw": 359.99999
        })
        #magnetic intensity in microteslas
        self.compass_raw = Reading(sensor.get_compass_raw(), {
            "x": -25.82731819152832,
            "y": 2.236360549926758,
            "z": -8.055685043334961
        }, {
            "x": -25.82731819152832,
            "y": 2.236360549926758,
            "z": -8.055685043334961
        })
        #rotational intensity in radians per second
        self.gyroscope_raw = Reading(sensor.get_gyroscope_raw(), {
            "x": -0.0006318986415863037,
            "y": 0.0006402982398867607,
            "z": 0.001421196386218071
        }, {
            "x": -0.0006318986415863037,
            "y": 0.0006402982398867607,
            "z": 0.001421196386218071
        })
        #acceleration intensity in Gs
        self.accelerometer_raw = Reading(sensor.get_accelerometer_raw(), {
            "x": -8.0, 
            "y": -8.0, 
            "z": -8.0
        }, {
            "x": 8.0, 
            "y": 8.0, 
            "z": 8.0
        })
    def update(self, sensor):
        self.timestamp = get_datetime()["epoch"]
        self.humidity = Reading(sensor.get_humidity(), 
                                self.humidity.min_value, 
                                self.humidity.max_value
                               )
        self.temperature_from_humidity = Reading(convertCToF(sensor.get_temperature_from_humidity()), 
                                                 self.temperature_from_humidity.min_value, 
                                                 self.temperature_from_humidity.max_value
                                                )
        self.temperature_from_pressure = Reading(convertCToF(sensor.get_temperature_from_pressure()), 
                                                 self.temperature_from_pressure.min_value, 
                                                 self.temperature_from_pressure.max_value
                                                )
        self.pressure = Reading(sensor.get_pressure(), 
                                self.pressure.min_value, 
                                self.pressure.max_value
                               )
        self.orientation_radians = Reading(sensor.get_orientation_radians(), 
                                           self.orientation_radians.min_value, 
                                           self.orientation_radians.max_value
                                          )
        #magnetic intensity in microteslas
        self.compass_raw = Reading(sensor.get_compass_raw(), 
                                   self.compass_raw.min_value, 
                                   self.compass_raw.max_value
                                  )
        #rotational intensity in radians per second
        self.gyroscope_raw = Reading(sensor.get_gyroscope_raw(), 
                                     self.gyroscope_raw.min_value, 
                                     self.gyroscope_raw.max_value
                                    )
        #acceleration intensity in Gs
        self.accelerometer_raw = Reading(sensor.get_accelerometer_raw(), 
                                         self.accelerometer_raw.min_value, 
                                         self.accelerometer_raw.max_value
                                        )


class Sensor:
    """This class represents the sensors on the Sense Hat"""
    def __init__(self):
        self.sensor = SenseHat()
        self.clear_sensor()
        self.imperialOrMetric = "imperial"
        self.sense = Sense(self.sensor)
        self.data_dict = []
    def clear_sensor(self):
        self.sensor.clear()
        self.sensor.set_imu_config(True, True, True)
    def touch(self):
        self.sense.update(self.sensor)
    def clear_stats(self):
        self.data_dict.clear()
    def add_stats(self, data_points, delay):
        for call in range(data_points):
            self.touch()
            self.data_dict.append(self.sense)
            time.sleep(delay)
        
