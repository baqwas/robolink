#!/usr/bin/env python3
"""
rangefront.py
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

distance = 50           # centimeters
pitchpower = 30         # % power for pitch, -100 to +100
duration = 0
moveperiod = 0.2        # seconds, move duration

drone = Drone()         # instantiate a drone entity for use in script
drone.pair()            # pair controller with drone
print("Drone paired!")  # obligatory message

drone.takeoff()         # time to rise and shine
print("Drone takeoff in progress")  # obligatory message
while True:
    if drone.detect_wall(distance):
        print(f"Front obstacle <= {distance} cm; suspending forward movement.")
                        # basic backtrack
                        # assuming no obstacle from origination point
                        # will revisit logic later
        drone.set_pitch(-pitchpower)    # travel in reverse direction
        drone.move(duration)            # use accumulated time period
        break

    drone.set_pitch(pitchpower)         # maintain forward movement
    drone.move(moveperiod)              # fixed move increment
    duration += moveperiod              # accumulation duration

print("Landing initiated")
drone.land()
print("The Drone has landed")

drone.close()
print("All done!")


