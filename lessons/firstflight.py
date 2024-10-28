#!/usr/bin/env python3
"""
firstflight.py
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

hoverperiod = 1         # how long should the drone stay in the air, seconds
drone = Drone()         # instantiate a drone entity for use in script
drone.pair()            # pair controller with drone (port_name='COM4') specific port name is optional
print("Drone paired!")  # obligatory message

drone.takeoff()         # time to rise and shine to 80 cm and hover; parameters cannot be modified
print("Drone takeoff in progress")  # obligatory message
drone.hover(hoverperiod) # at least 1 sec needed to stabilize takeoff and hover
                        # hover indefinitely if no parameter is specified
print("In the air!")    # obligatory

print("Landing initiated")
                        # need some "time" after takeoff before the subsequent command is processed
                        # if land() follows takeoff() immediately then land() may not be performed
drone.land()            # stop all commands, hover and perform a soft landing
print("The Drone has landed")

battery_level = drone.get_battery()
if battery_level < 90:
    drone.drone_buzzer(400, 300)    # (note, duration)
    drone.drone_buzzer(600, 300)    # (Hz, milliseconds)
else:
    print(f"Battery level is {battery_level}")

drone.close()
print("All done!")


