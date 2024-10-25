#!/usr/bin/env python3
"""
gyroangles.py
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
- Describe how a gyroscope works
- Explain how a gyroscope reports movements
- Explain the difference between displacement and angular rotation
- Describe how gyroscope values can be used to improve the accuracy of flight movements
- Create programs that use gyroscope values to control flight movements

Steps:
- Getting Gyroscope Angles
- Put it in a Loop!
- Turn 90 Degrees
- Gyro with LED
- Turn_degree()
- Challenge 1: A More Perfect Polygon

@sa https://learn.robolink.com/lesson/3-4-gyroscope-cde/
@sa https://youtu.be/wPpuBOSU7_w
"""
from codrone_edu.drone import *  # robolink package
import keyboard, math, time

def drone_turn(degrees, power):
    MAX_ANGLE = 180
    yaw_angle = degrees
    if yaw_angle < MAX_ANGLE:
        yaw_power = math.copysign(1, yaw_angle) * power
        while drone.get_z_angle() < yaw_angle:
            drone.set_yaw(yaw_power)
            drone.move()
    else:
        drone_turn(MAX_ANGLE, power)
        yaw_angle = degrees - MAX_ANGLE
        drone_turn(yaw_angle, power)

    drone.move(0)

drone = Drone()         # instantiate a drone entity for use in script
drone.pair()            # pair controller with drone
print("Drone paired!")  # obligatory message

while True:
    print(f"X, roll={drone.get_x_angle()}, Y, pitch={drone.get_y_angle()}, Z, yaw={drone.get_z_angle()}")
    time.sleep(1)

    if keyboard.is_pressed('esc'):
        break

drone.takeoff()         # time to rise and shine
print("Drone takeoff in progress")  # obligatory message

turn_angle = 90         # degrees; turn angle
turn_power = 20
drone_turn(turn_angle, turn_power)

print("Landing initiated")
drone.land()
time.sleep(3)
print("The Drone has landed")

drone.close()
print("All done!")


