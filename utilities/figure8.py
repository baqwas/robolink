#!/usr/bin/env python3
"""
figure8.py
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
- land

@sa https://www.robolink.com/products/codrone-edu
"""
from codrone_edu.drone import *  # robolink package
import numpy as np
import time

                            # key points for the figure-8
start_altitude = 20         # starting altitude, cm
top_altitude = 1.0          # top altitude, cm
bottom_altitude = 10        # Bottom altitude, cm
horizontal_distance = 50    # Horizontal distance between top and bottom points, cm

drone = Drone()         # instantiate a drone entity for use in script
drone.pair()            # pair controller with drone
print("Drone paired!")  # obligatory message

try:
    # Take off
    drone.takeoff()

    # Fly to the starting position
    drone.move(x=0, y=0, z=start_altitude, speed=0.5)

    # Fly the figure-8
    while True:
        # Fly to the top point
        drone.move(x=horizontal_distance / 2, y=0, z=top_altitude, speed=0.5)
        time.sleep(1)

        # Fly to the bottom point
        drone.move(x=-horizontal_distance / 2, y=0, z=bottom_altitude, speed=0.5)
        time.sleep(1)

        # Fly back to the top point
        drone.move(x=horizontal_distance / 2, y=0, z=top_altitude, speed=0.5)
        time.sleep(1)

        # Fly back to the bottom point
        drone.move(x=-horizontal_distance / 2, y=0, z=bottom_altitude, speed=0.5)
        time.sleep(1)

except KeyboardInterrupt:
    drone.land()
    print("Landing initiated")

drone.close()
print("All done!")


