#!/usr/bin/env python3
"""
controllerPID.py
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
class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

        self.previous_error = 0
        self.integral = 0

    def calculate_output(self, error, dt):
        self.integral += error * dt
        derivative = (error - self.previous_error) / dt
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.previous_error = error
        return output
