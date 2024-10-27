#!/usr/bin/env python3
"""
testPID.py
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
import keyboard
from codrone_edu.drone import *  # robolink package


class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

        self.previous_error = 0
        self.integral = 0

    def calculate_output(self, error_calc, dt):
        self.integral += error_calc * dt
        derivative = (error_calc - self.previous_error) / dt
        output = self.Kp * error_calc + self.Ki * self.integral + self.Kd * derivative
        self.previous_error = error_calc
        return output

# Assuming you have a function to get the current pitch, roll, and yaw
def get_current_angles(drone):
    # X := roll, y := pitch, z := yaw
    pitch = drone.get_y_angle() # degrees
    roll = drone.get_x_angle()  # degrees
    yaw = drone.get_z_angle()   # degrees
    return pitch, roll, yaw

def clamp(value, lower_limit, upper_limit):
  """Clamps a value between a lower and upper limit.

  Args:
    value: The value to clamp.
    lower_limit: The lower limit.
    upper_limit: The upper limit.

  Returns:
    The clamped value.
  """

  return max(lower_limit, min(value, upper_limit))

# Assuming you have a function to set the desired pitch, roll, and yaw
def set_desired_power(drone, pitch, roll, yaw):
    drone.set_pitch = clamp(pitch, -100., 100.)
    drone.set_roll = clamp(roll, -100., 100.)
    drone.set_yaw = clamp(yaw, -100., 100.)

def low_pass_filter(x, y, dampening_factor):
  """
  Low-pass filter function.

  Args:
    x: Current input value.
    y: Previous filtered output value.
    dampening_factor: Filter coefficient (0 <= dampening_factor <= 1).

  Returns:
    Filtered output value.
  """

  return alpha * x + (1 - dampening_factor) * y


myDrone = Drone()         # instantiate a drone entity for use in script
myDrone.pair()            # pair controller with drone
print("Drone paired!")  # obligatory message

# Initialize PID controllers for each axis
Kp_pitch = 0.6
Ki_pitch = 3.5
Kd_pitch = 0.03
pid_pitch = PIDController(Kp_pitch, Ki_pitch, Kd_pitch)
Kp_roll = 0.6
Ki_roll = 3.5
Kd_roll = 0.03
pid_roll = PIDController(Kp_roll, Ki_roll, Kd_roll)
Kp_yaw = 2.
Ki_yaw = 12.
Kd_yaw = 0.
pid_yaw = PIDController(Kp_yaw, Ki_yaw, Kd_yaw)
alpha = 0.8
filtered_pitch = 0.0
filtered_roll = 0.0
filtered_yaw = 0.0

                        # level orientation
desired_pitch = 0.0
desired_roll = 0.0
desired_yaw = 0.0
                        # control algorithm step size
deltat = 0.01
                        # target altitude
# slot_elevation = 30.0

myDrone.takeoff()         # time to rise and shine
print("Drone takeoff in progress")  # obligatory message
sleep(3)      # need to work on the delay period
print("In the air!")    # obligatory

# Main control loop
while True:
                        # Get current angles
    current_pitch, current_roll, current_yaw = get_current_angles(myDrone)

                        # Calculate error for each axis
    error_pitch = desired_pitch - current_pitch
    error_roll = desired_roll - current_roll
    error_yaw = desired_yaw - current_yaw

                        # Calculate control output for each axis
    control_pitch = pid_pitch.calculate_output(error_pitch, deltat)
    control_roll = pid_roll.calculate_output(error_roll, deltat)
    control_yaw = pid_yaw.calculate_output(error_yaw, deltat)

                        # use a filter function to dampen sensor noise
    filtered_pitch = low_pass_filter(control_pitch, filtered_pitch, alpha)
                        # Set the desired angles to the drone
    set_desired_power(myDrone, control_pitch, control_roll, control_yaw)

    time.sleep(deltat)  # may need to adjust the time step as needed
    if keyboard.is_pressed('esc'):
        break

print("Landing initiated")
myDrone.land()
print("The Drone has landed")

myDrone.close()
print("All done!")