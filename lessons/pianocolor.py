#!/usr/bin/env python3
"""
pianocolor.py
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
- Predict colors with the CoDrone EDU

Steps:
- Color Sensor Prediction

@sa https://learn.robolink.com/lesson/3-7-color-classifier-cde/
@sa https://courses.cs.washington.edu/courses/cse455/20sp/notes/Linda/2_Color_Texture_FIN_20.pdf
"""
from codrone_edu.drone import *  # robolink package
import time

dataset = "color_data"          # dataset label for use in autonomous
duration = 1000                 # milliseconds
interval = 0.2

drone = Drone()                 # instantiate a drone entity for use in script
drone.pair()                    # pair controller with drone
print("Drone paired!")          # obligatory message

drone.load_classifier(dataset)  # ensure correct value for dataset variable
print(f"Loaded color classifier {dataset}")

try:
    while True:
        color_data = drone.get_color_data()
        color = drone.predict_colors(color_data)
                                # green, red, yellow, black
        if color[0] == "green":
            drone.drone_buzzer(Note.B4, duration)   # buzz not play note
        elif color[0] == "red":
            drone.drone_buzzer(Note.A4, duration)
        elif color[0] == "yellow":
            drone.drone_buzzer(Note.C4, duration)
        elif color[0] == "black":
            drone.drone_buzzer(Note.G4, duration)
        else:
            drone.drone_buzzer(0,0)     # what color was that?
            print(f"Color {color} not implemented")

        print(f"The drone sees color {color}")
        time.sleep(interval)

except KeyboardInterrupt:
    print("KeyboardInterrupt raised!")

drone.close()
print("All done!")
