#!/usr/bin/env python3
"""
sensorreset.py
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
- Use the print() function and describe its value in debugging (finding and
fixing errors) in your code
- Add comments to your code and understand the importance of well
documented code
- Pair with your drone using the drone.pair() function
Understand how to use the drone.takeoff()and drone.land() functions

Steps:
- pairing
- takeoff
- measure height
- land

@sa https://learn.robolink.com/lesson/3-5-height-sensor-cde/
"""
from codrone_edu.drone import *  # robolink package

hoverperiod = 3         # how long should the drone stay in the air, seconds
settingyaw = 50         #
drone = Drone()         # instantiate a drone entity for use in script
drone.pair()            # pair controller with drone
print("Drone paired!")  # obligatory message

print(f"Before: X={drone.get_x_angle()}, Y={drone.get_y_angle()}, Z={drone.get_z_angle()}")
drone.takeoff()         # time to rise and shine
print("Drone takeoff in progress")  # obligatory message
sleep(hoverperiod)      # need to work on the delay period
print("In the air!")    # obligatory

drone.set_yaw(settingyaw)   # -100 - + 100; -ve is right, +ve is left
drone.set_trim(25, 15)  # roll & pitch; -100 - +100

print("Landing initiated")
drone.land()
print("The Drone has landed")

drone.close()
print("All done!")


