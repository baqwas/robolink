#!/usr/bin/env python3
"""
rollpitch.py
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
- takeoff
- set roll movement
- set speed and direction of movement
- hover
- land

@sa https://www.robolink.com/products/codrone-edu
"""
from codrone_edu.drone import *  # robolink package

moveperiod = 1          # period, seconds, for drone movement
pitchpower = 30          # % power for movement to front (0->100) & to back (0->100)
rollpower = 30          # % power for movement to right (0->100) & to left (0->100)

drone = Drone()         # instantiate a drone entity for use in scirpt
drone.pair()            # pair controller with drone
print("Drone paired!")  # obligatory message

drone.takeoff()         # time to rise and shine
print("In the air!")    # obligatory
                        # 1st leg
drone.set_pitch(pitchpower) # set pitch with positive power
print(f"Pitch set to {pitchpower}")
drone.move(moveperiod)  # moving forward for 1 second
print(f"Move period is {moveperiod}")
drone.set_pitch(0)      # reset pitch
print(f"Pitch reset to {pitchpower}")
                        # 2nd leg
drone.set_roll(rollpower)   # roll with positive power
print(f"Roll set to {rollpower}")
drone.move(moveperiod)  # moving to the right for 1 second
print(f"Move period is {moveperiod}")
drone.set_roll(0)   # reset roll power
print(f"Roll reset to {rollpower}")
                        # 3rd leg
drone.set_pitch(-pitchpower) # set pitch with negative power
print(f"Pitch set to {-pitchpower}")
drone.move(moveperiod)  # moving backward for 1 second
print(f"Move period is {moveperiod}")
drone.set_pitch(0)      # reset pitch power
print(f"Pitch reset to {pitchpower}")
                        # 4th leg
drone.set_roll(-rollpower)   # set roll power with negative power
print(f"Roll set to {rollpower}")
drone.move(moveperiod)  # moving to the left for 1 second
print(f"Move period is {moveperiod}")
drone.set_roll(0)   # reset roll power
print(f"Roll reset to {rollpower}")
drone.land()
print("The Drone has landed")

drone.close()
print("All done!")


