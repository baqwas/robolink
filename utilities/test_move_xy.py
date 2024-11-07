#!/usr/bin/env python3
"""
test_move_xy.py
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

Key Points:
- Tuning the PID Gains:
    The Kp, Ki, and Kd gains need to be tuned carefully to achieve stable and
    responsive control.
- Time Step:
    The dt parameter in the calculate_output method represents the time interval
    between control cycles.
    It's important to choose an appropriate value to ensure accurate control.
- Saturation:
    To prevent excessive control signals, consider implementing saturation limits.
- Integration Windup:
    To avoid integral windup, you can limit the integral term or use anti-windup
    techniques.
    get_current_angles() is a placeholder for codrone_edu equivalent function
    set_desired_angles() should translate the control outputs into appropriate
    commands for codrone_edu methods
- Noise Filtering:
    If the sensor measurements are noisy, you can apply filtering techniques
    (e.g., low-pass filter) to reduce noise.
- Real-World Considerations:
    Real-world factors like wind, air resistance, and motor dynamics can affect the drone's behavior. You may need to adjust the PID gains and control strategy to compensate for these factors.



@sa https://oscarliang.com/pid/
"""

from codrone_edu.drone import *  # robolink package
import time

def move_delta_xy(target_flow_x, target_flow_y, Kp, Ki, Kd, landing):
    """
    move the drone horizontally in relative x and y distances from current position
    :param target_flow_x: distance to move in x-axis, cm unless otherwise specified
    :param target_flow_y: distance to move in y-axis, cm unless otherwise specified
    :param Kp: Proportional controller coefficient
    :param Ki: Integral controller coefficient
    :param Kd: Derivative controller coefficient
    :param landing: True to land drone after move, False do not land drone after move
    :return:
    """
                            # Differential component in PID controller equation
    prev_error_x = 0.
    prev_error_y = 0.
    sum_error_x = 0.
    sum_error_y = 0.


    myDrone = Drone()       # instantiate a drone entity for use in script
    myDrone.pair()          # pair controller with drone
    print("Drone paired!")  # obligatory message
                            # target altitude
                            # slot_elevation = 30.0, will need to lower drone after takeoff
    myDrone.reset_sensor()  # roll, pitch, yaw := zero
    sleep(1)                # to avoid next drone command to be skipped
    myDrone.set_initial_pressure() # initialized the pressure value
    print("Pressure sensor initialized")  # obligatory message
    sleep(1)                # playing it safe

    myDrone.takeoff()       # time to rise and shine
    print("Drone takeoff in progress")  # obligatory message
    sleep(3)                # need to work on the delay period
    print("In the air!")    # obligatory
                            # where am I?
                            # +x: forward, -x: backward
                            # +y: left, -y: right
                            # + +z: up, -z: down
    position_current = myDrone.get_position_data()
    position_target = [position_current[0] + target_flow_x, position_current[1] + target_flow_y, position_current[2]]

    while True:
        # Read current flow values
        position_current = myDrone.get_position_data()
        if (position_target[0] - position_current[0]) < 1.0 and (position_target[1] - position_current[1]) < 1.0:
            break

        # Calculate error
        error_x = target_flow_x - position_current[0]
        error_y = target_flow_y - position_current[1]
        sum_error_x += error_x
        sum_error_y += error_y

        # Calculate PID output
        output_x = Kp * error_x + Ki * sum_error_x + Kd * (error_x - prev_error_x)
        output_y = Kp * error_y + Ki * sum_error_y + Kd * (error_y - prev_error_y)

        # Set roll and pitch angles
        myDrone.set_roll(output_x)
        myDrone.set_pitch(output_y)

        # Update previous error
        prev_error_x = error_x
        prev_error_y = error_y

        # Adjust the loop time to control the movement rate
        time.sleep(0.01)

    if landing:
        print("Landing initiated")
        myDrone.land()
        print("The Drone has landed")

        myDrone.close()
        print("All done!")

    return True

if __name__ == "__main__":
                            # x, y distances are relative to current position
                            # PID coefficients: Kp, Ki, & Kd; tune as needed
                            # landing: True to land the drone after move completion
    move_delta_xy(50., 0., 0.5, 0.1, 0.01, True)