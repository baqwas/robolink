#!/usr/bin/env python3
"""
takeoff.py
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
@sa https://docs.robolink.com/docs/CoDroneEDU/Python/Function-Documentation#takeoff
@sa https://docs.robolink.com/docs/CoDroneEDU/Python/Function-Documentation#get_bottom_range
@sa https://docs.robolink.com/docs/CoDroneEDU/Python/Function-Documentation#move
"""

from codrone_edu.drone import *  # robolink package


class PIDcontroller:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

        self.previous_error = 0
        self.integral = 0

    def calculate_output(self, error_calc, deltat):
        self.integral += error_calc * deltat
        derivative = (error_calc - self.previous_error) / deltat
        output = self.Kp * error_calc + self.Ki * self.integral + self.Kd * derivative
        self.previous_error = error_calc
        return output


dataset = "color_data"  # dataset label for use in autonomous
hoverperiod = 1  # how long should the drone stay in the air, seconds
desiredFL = 10  # desired flight level
Kp_altitude = 0.15
Ki_altitude = 0.15
Kd_altitude = 0.05
dt = 0.01
pid_altitude = PIDcontroller(Kp_altitude, Ki_altitude, Kd_altitude)

drone = Drone()  # instantiate a drone entity for use in script
drone.pair()  # pair controller with drone
print("Drone paired!")  # obligatory message
drone.reset_move()  # reset the values of roll, pitch, yaw and throttle to 0
"""
This function makes the drone takeoff at an average height of 80 centimeters and hover. 
The drone will always hover for 1 second in order to stabilize before it executes the next command. 
The takeoff parameters or height cannot be modified.
"""
drone.takeoff()  # time to rise and shine to ~80 cm
print("Drone takeoff in progress")  # obligatory message
"""
hover for a given amount of time. 
If given no parameters, it will hover indefinitely until given a another command.
"""
drone.hover(hoverperiod)  # parameter in seconds
print("In the air!")  # obligatory
"""
for debugging purposes only
"""
# [3] elevation from barometer, m
# [4] height from bottom range sensor, m
# [16] x, m
# [17] y, m
# [18] z, m
sensor_data = drone.get_sensor_data()
print(f"{sensor_data[3]}, {sensor_data[4]}; {sensor_data[16]}, {sensor_data[17]}, {sensor_data[18]}")

drone.set_throttle(10)  # %, -100 - +100
current_bottom_range = drone.get_bottom_range("cm")  # m, mm and in also available; cm is default if omitted
print(f"Bottom range: {current_bottom_range}")
error_altitude = desiredFL - current_bottom_range
while error_altitude > 0.1:
    current_bottom_range = drone.get_bottom_range()  # current altitude
    error_altitude = desiredFL - current_bottom_range  # altitude error
    control_output = pid_altitude.calculate_output(error_altitude, dt)  # control output
    control_output = max(min(control_output, 100), -100)
    drone.set_throttle(control_output)  # set desired thrust to the drone
    drone.move()
    time.sleep(dt)
    print(f"Bottom range: {current_bottom_range}; error: {error_altitude}, {control_output}")

sensor_data = drone.get_sensor_data()
print(f"{sensor_data[3]}, {sensor_data[4]}; {sensor_data[16]}, {sensor_data[17]}, {sensor_data[18]}")

print("Landing initiated")
drone.land()  # land on mat to detect colors
print("The Drone has landed")
sensor_data = drone.get_sensor_data()
print(f"{sensor_data[3]}, {sensor_data[4]}; {sensor_data[16]}, {sensor_data[17]}, {sensor_data[18]}")

# drone.load_classifier(dataset)  # ensure correct value for dataset variable
# print(f"Loaded color classifier {dataset}")
color_data = drone.get_color_data()  # obtain sensor reading
color = drone.predict_colors(color_data)  # compare reading with custom dataset
print(f"The drone sees color {color}")
if color[0] == "red":
    drone.set_drone_LED(255, 0, 0, 100)
elif color[0] == "green":
    drone.set_drone_LED(0, 255, 0, 100)
elif color[0] == "blue":
    drone.set_drone_LED(0, 0, 255, 100)
else:
    drone.drone_LED_off()

drone.close()
print("All done!")
