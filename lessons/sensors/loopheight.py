#!/usr/bin/env python3
"""
loopheight.py
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

throttlepower = 10      # -100 - +100; -ve is down, +ve is up
moveperiod = 1.5        # seconds; duration of move
drone = Drone()         # instantiate a drone entity for use in script
drone.pair()            # pair controller with drone
print("Drone paired!")  # obligatory message

drone.reset_sensor()    # gyro angles = 0; roll, pitch and yaw
drone.set_trim(25, 15)  # roll, pitch; change as necessary
time.sleep(1)           # nominal delay so that any immediately following drone command is not skipped

height_data = [drone.get_height()]  # cm (default); using bottom range sensor
print(f"Takeoff height:  {height_data[0]} cm")
for i in range(3):      # may want to change this control to an indefinite loop
    drone.takeoff()     # time to rise and shine
    throttlepower += 10 # for the next iteration
    drone.set_throttle(throttlepower)   # -100 - +100; direction and power; -ve down, +ve up
    drone.move(moveperiod)  # move the drone based on previously set values
    height_data.append(drone.get_height())  # cm; others units are m, mm or in
    drone.land()        # stop all commands, flight motion variables = 0; soft landing
    time.sleep(5)       # time to reposition the drone as appropriate

print(height_data)      # how high did we go in each iteration

drone.close()
print("All done!")


