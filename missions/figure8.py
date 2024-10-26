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
- identify color

@sa https://www.robolink.com/products/codrone-edu
"""
from codrone_edu.drone import *             # robolink package

def figure_eight(height_top, height_bottom, horizontal_distance, speed):

    while True:
        # Move up to the top point
        drone.move(x=horizontal_distance/2, y=0, z=height_top, speed=speed)
        time.sleep(2)

        # Move down to the bottom point
        drone.move(x=-horizontal_distance/2, y=0, z=height_bottom, speed=speed)
        time.sleep(2)

        # Move up to the top point again
        drone.move(x=horizontal_distance/2, y=0, z=height_top, speed=speed)
        time.sleep(2)

        # Move down to the bottom point again
        drone.move(x=-horizontal_distance/2, y=0, z=height_bottom, speed=speed)
        time.sleep(2)

hoverperiod = 1                             # how long should the drone stay in the air, seconds

drone = Drone()                             # instantiate a drone entity for use in script
drone.pair()                                # pair controller with drone
print("Drone paired!")                      # obligatory message

drone.takeoff()                             # time to rise and shine
print("Drone takeoff in progress")          # obligatory message

                                            # paramters to tweak
height_top = 100                            # cm
height_bottom = 20                          # cm
horizontal_distance = 80                    # cm
speed = 20                                  # %, -100 - +100

drone.close()
print("All done!")


