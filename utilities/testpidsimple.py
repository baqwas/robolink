#!/usr/bin/env python3
"""
testpidsimple.py
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
                        # controller coefficients
Kp = 0.5                # proportional gain
Ki = 0.1                # integral gain
Kd = 0.05               # derivative gain
integral = 0.0
error_prev = 0.0

drone = Drone()         # instantiate a drone entity for use in script
drone.pair()            # pair controller with drone
print("Drone paired!")  # obligatory message

def pid_control(error):
    global integral, error_prev

    integral += error
    derivative = error - error_prev

    control_signal = Kp * error + Ki * integral + Kd * derivative
    error_prev = error

    return control_signal

try:
    while True:
        # Get current yaw (replace with your desired variable)
        yaw = drone.read_yaw()

        # Set desired yaw (replace with your desired value)
        desired_yaw = np.pi / 4  # 45 degrees

        # Calculate error
        error = desired_yaw - yaw

        # Get PID control signal
        control_signal = pid_control(error)

        # Apply control signal to drone (adjust based on your drone's API)
        drone.set_yaw(control_signal)

        time.sleep(0.01)  # Adjust sleep time as needed

except KeyboardInterrupt:
    drone.disconnect()
    print("Disconnected from drone.")

drone.close()
print("All done!")


