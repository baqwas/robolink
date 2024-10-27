#!/usr/bin/env python3
"""
pressurealtitude.py
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
 - Describe how roll and pitch change the drone’s movement in the air.
 - Explain the difference between parameters and arguments when using functions.
 - Use the roll and pitch throttle commands to make the drone navigate a path of your choosing.
 - Incorporate your knowledge to build a full flight path for the drone, including takeoff and landing.

Steps:
- pairing
- set initial pressure
- manually change the height of the drone
- display the height based on barometric data
- hover
- land

@sa https://www.robolink.com/products/codrone-edu
"""
import keyboard
from codrone_edu.drone import *  # robolink package

drone = Drone()         # instantiate a drone entity for use in scirpt
drone.pair()            # pair controller with drone
print("Drone paired!")  # obligatory message

drone.set_initial_pressure()    # for use with height_from_pressure()
while True:
    print(f"Height from pressure {drone.height_from_pressure()}, mm")
    time.sleep(0.2)
    if keyboard.is_pressed('esc'):
        break

drone.close()
print("All done!")


