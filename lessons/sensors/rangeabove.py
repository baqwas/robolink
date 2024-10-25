#!/usr/bin/env python3
"""
rangeabove.py
2014-10-24 0.1 Initial DRAFT
Copyright (C) 2024 ParkCircus Productions

Detection of physical objects in front

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

The front range sensor can detect an object upto a distance of 100 centimeters

Objectives:
- Check if the front distance is beyond a stipulated value
- Terminate flight if distance is less than the stipulated value

Steps:
- obtain wall distance
- evaluate options

@sa https://learn.robolink.com/lesson/3-6-front-range-sensor-1-cde/
"""

from codrone_edu.drone import *  # robolink package
import time

hoverperiod = 3         # hover period, seconds
drone = Drone()         # instantiate a drone entity for use in script
drone.pair()            # pair controller with drone
print("Drone paired!")  # obligatory message

height_takeoff = drone.get_height()   # base elevation, cm
print(f"Takeoff elevation {height_takeoff} cm")

drone.takeoff()         # time to rise and shine
print("Drone takeoff in progress")  # obligatory message

drone.hover(hoverperiod)          # hover for specified time, seconds
print(f"Hover for {hoverperiod} seconds")
height_hover = drone.get_height()    # current altitude, cm
print(f"Hover elevation {height_hover} cm")

print("Landing initiated")
drone.land()
time.sleep(hoverperiod)
print("The Drone has landed")
height_landing = drone.get_height()    # current altitude, cm
print(f"Landing elevation {height_landing} cm")

drone.close()
print("All done!")
