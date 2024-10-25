#!/usr/bin/env python3
"""
calibratecolor.py
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
- Know the difference between HSV and RGB
- Describe how the CoDrone EDU classifies colors
- Calibrate my color sensor
- Predict colors with the CoDrone EDU

Steps:
- Color Sensor Calibration
- Color Sensor Prediction
- Color Piano
- Test case 1: Multiple Samples
- Test case 2: Color Piano – Extended

@sa https://learn.robolink.com/lesson/3-7-color-classifier-cde/
"""
from codrone_edu.drone import *  # robolink package
import time

dataset = "color_data"          # dataset label for use in autonomous
                                # the spectrum must have at least 3 colors enuemrated
colors = ["green", "purple", "red", "lightblue", "blue", "yellow", "black", "white"]
samples = 500  # number of samples for each color

drone = Drone()         # instantiate a drone entity for use in script
drone.pair()            # pair controller with drone
print("Drone paired!")  # obligatory message

for color in colors:
    data = []           # holding buffer for each color calibration data

    for i in range(1):  # loading bar
        print("Sample: ", i + 1)
        next = input("Press [Enter] to calibrate " + color) # DO NOT MOVE the drone
        print("0% ", end="")

        for j in range(samples):
            color_data = drone.get_color_data()[0:9]
            data.append(color_data)
            time.sleep(0.005)   # blink and you'll miss it
            if j % 10 == 0:
                print("-", end="")  # pseudo progress bar
        print(" 100%")

    drone.new_color_data(color, data, dataset) # create new color directory
    # drone.append_color_data(color, data, dataset) # if more appropriate than new

    print(f"New color directory for {color}")

print("Color calibration complete")

drone.close()
print("All done!")
