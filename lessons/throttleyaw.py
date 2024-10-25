#!/usr/bin/env python3
"""
throttleyaw.py
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
- Describe how roll, pitch, yaw, and throttle change the drone’s movement in the air.
- Use the roll, pitch, yaw, and throttle commands to make the drone navigate a path of your choosing.
- Incorporate your knowledge of creating a complete program from Island 1 to build a full flight path for the drone, including takeoff and landing.

Steps:
- pairing
- takeoff
- throttle and yaw
- land

@sa https://www.robolink.com/products/codrone-edu
"""
from codrone_edu.drone import *  # robolink package

pitchpower = 20         # 20% power
duration = 1          # period, seconds, to maintain current power settings
drone = Drone()         # instantiate a drone entity for use in scirpt
drone.pair()            # pair controller with drone
print("Drone paired!")  # obligatory message

drone.takeoff()         # time to rise and shine
print("Drone takeoff in progress")  # obligatory message

drone.set_pitch(pitchpower) # Moves the drone forward at 20% power
print(f"Applied pitch power at {pitchpower}%")
drone.move(duration)  # Moves for 1 second
print(f"Moving for {duration} second(s)")
drone.set_pitch(0)      # Resets the pitch power back to 0%
drone.set_roll(-pitchpower) # Moves the drone to the left at 20% power
print(f"Applied pitch power at {-pitchpower}%")
drone.move(2)           # Moves for 2 seconds

                        # fly in a circle

                        # follow a sine wave
speed = 40

drone.set_pitch(speed)
drone.set_throttle(speed)
drone.move(duration)
drone.set_throttle(-speed)
drone.move(duration)
drone.set_throttle(speed)
drone.move(duration)
drone.set_throttle(-speed)
drone.move(duration)

print("Landing initiated")
drone.land()
print("The Drone has landed")

drone.close()
print("All done!")


