#!/usr/bin/env python3
"""
ambient.py
2014-10-24 0.1 Initial DRAFT
Copyright (C) 2024 ParkCircus Productions

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Objectives:
- Key sensors:
    Temperature
    Pressure
    Battery
    Gyroscope
    Range
        Forward
        Down

Steps:
- pairing
- takeoff
- land

@sa https://www.robolink.com/products/codrone-edu
"""
from codrone_edu.drone import *  # robolink package
import datetime
import json

json_string = """
{
  "drone_id": "device123",
  "timestamp": "2023-11-22T13:37:20Z",
  "temperature": 25.5,
  "pressure": 1013.25,
  "battery": 85,
  "gyro": {
    "x": 0.12,
    "y": -0.05,
    "z": 0.08
  },
  "range": {
    "front": 2.5, "bottom": 0.8
  },
}
"""
def log_data():
    data["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    data["temperature"] = drone.get_temperature()  # °F
    data["pressure"] = drone.get_pressure()  # Pa
    data["battery"] = drone.get_battery()
    data["gyro"]["x"] = drone.get_x_angle()
    data["gyro"]["y"] = drone.get_y_angle()
    data["gyro"]["z"] = drone.get_z_angle()
    data["range"]["front"] = drone.get_front_range()  # cm, max 150
    data["range"]["bottom"] = drone.get_height()  # cm
    print(data)

data = json.loads(json_string)
hoverperiod = 1         # how long should the drone stay in the air, seconds
data["drone_id"] = "codrone1"
drone = Drone()         # instantiate a drone entity for use in script
drone.pair()            # pair controller with drone
print("Drone paired!")  # obligatory message

log_data()

drone.takeoff()         # time to rise and shine
print("Drone takeoff in progress")  # obligatory message

drone.hover(hoverperiod)      # need to work on the delay period
print("In the air!")    # obligatory

log_data()
drone.hover(hoverperiod)
log_data()

print("Landing initiated")
drone.land()
print("The Drone has landed")

log_data()

drone.close()
print("All done!")


