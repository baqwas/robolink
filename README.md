# Introduction
Aerial drone examples for Mission 2025 Gravity  
## Table of Contents

## Features

## Usage
Use the following standard command format to run the scripts:  
`
python <script>
`  
## Files
Some files are scripts that are meant to be invoked as commands while other files are helper scripts that encapsulate key operations and controls for the drone.  
## References

## Matches
- Two 5-minute sessions
- Up to 3 Autonomous Flight Skills Mission runs
 - Team to decide how to use the allocated time 
- One reset during each Autonomous Flight Skills Mission run
- Color Mats are randomized
 - Two colors from Red, Green & Blue
 - Drone starting position is COLORMAT 1
 - If a drone is reset then it must be placed on COLORMAT 2 
## Autonomous Flight
    • [Take Off](#takeoff)
    • [Figure 8](#figure8)
    • [Under Arch Gate](#underarch)
    • [Fly through Hole](#flyhole)
        ◦ Large Hole
        ◦ Small Hole
    • [Fly through Keyhole Gate](#keyhole)
    • Landing Position
        ◦ Small Cube
        ◦ Large Cube
        ◦ Landing Pad
    • Identify Color
    • Fly Under arch
### <a name="takeoff">Take Off</a>
The two actions are:
- Take Off
- Color Identification
#### Take Off
The first takeoff from a mat will score 10 points:
 - Color Mat 1: once per match
 - Color Mat 2: once per match
#### Color Identification
The identification of the color of the mat will score 15 points:
 - Color Mat 1: once per match
 - Color Mat 2: once per match
 - Points for identifying Color Mat 2 are awarded only if completed before a reset. Teams cannot manually set the color.
### <a name="figure8">Figure 8</a>
The Figure 8 skill must be completed without performing any other mission within the Figure 8 mission. There are four steps in the mission:
- Step 1: Fly under the Red Arch Gate
- Step 2: Fly over the Blue Arch Gate
- Step 3: Fly under the Blue Arch Gate
- Step 4: Fly over the Red Arch Gate
This mission can be performed twice during the Autonomous Flight Skills Match. Each completed mission will earn 40 points. The flight must be over or under the letters on the Arch Gate.
### <a name="underarch">Under Arch Gate</a>
Fly under an Arch Gate for 5 points subject to the following conditions:
- Flight direction is from right to left based on operator stations
- The entire drone must clear the Arch Gate
- Only the first two successful flights will be awarded 5 points each
### <a name="flyhole">Fly through Hole</a>
There are two holws:
- Large
- Small
#### Large Hole
Flying through the Large Hole earns 10 points per traversal with a maximum of two flights per match.
- The drone must fly front to back
- The drone must clear the hole completely
#### Small Hole
### <a name="keyhole">KeyHole Gate</a>
Flying through the Keyhole Gate earns 15 points. A total of two times per Keyhole Gate is considered for points.
### Landing Position
There are options for landing at the end of the match:
- Pad
- Large Cube
- Small Cube
#### Small Cube
40 points
#### Large Cube
25 points
#### Landing Pad
15 points
### Identify Color
#### Preparation
- Enable control flight mode
- Press *P* or *S* button
- Ensure the controller displays the HSV page for Hue, Saturation and Value

| Attribute  | Min | Max |
|------------|-----|-----|
| Hue        | 0   | 360 |
| Saturation | 0   | 100 |
| Value      | 0   | 100 |

#### Color Sensor Calibration
##### Default Colors
white, black, red, yellow
green, teal,  blue, purple



# Sensor Data
| Index | Name              | Units      | Range          | Comments                         |
|-------|-------------------|------------|----------------|----------------------------------|
| 0     | Altitude          | time stamp |                | sensor                           |
| 1     | Temperature       | °C         |                |                                  |
| 2     | Pressure          | Pa         |                |                                  |
| 3     | Elevation         | m          |                | from barometer                   |
| 4     | Height            | m          |                | from bottom range sensor         |
| 5     | Motion            | time stamp |                | sensor                           |
| 6     | Acceleration X    | m/s * 10   | -156.8 ~ 156.8 | Int16 2 Byte -1568 ~ 1568        |
| 7     | Acceleration Y    | m/s * 10   | -156.8 ~ 156.8 | Int16 2 Byte -1568 ~ 1568        |
| 8     | Acceleration Z    | m/s * 10   | -156.8 ~ 156.8 | Int16 2 Byte -1568 ~ 1568        |   data[8] acceleration Z Int16 2 Byte -1568 ~ 1568 (-156.8 ~ 156.8) m/s2 x 10 Z
| 9     | gyroRoll          | °/sec      |                | Int16 2 Byte -2000 ~ 2000        |
| 10    | gyroPitch         | °/sec      |                | Int16 2 Byte -2000 ~ 2000        |
| 11    | gyroYaw           | °/sec      |                | Int16 2 Byte -2000 ~ 2000        |
| 12    | angleRoll         | °          |                | Int16 2 Byte -180 ~ 180          |
| 13    | anglePitch        | °          |                | Int16 2 Byte -180 ~ 180          |
| 14    | angleYaw          | °          |                | Int16 2 Byte -180 ~ 180 degree   |
| 15    | Position          | time stamp |                |                                  |
| 16    | x                 | m          |                | Float32 4 Byte - X axis          |                                |
| 17    | y                 | m          |                | Float32 4 Byte - Y axis          |                                  |
| 18    | z                 | m          |                | Float32 4 Byte - z axis          | 
| 19    | Range             | time stamp |                | sensor                           |
| 20    | Front range       | mm         |                |                                  |
| 21    | Bottom range      | mm         |                |
| 22    | Drone state       | time stamp |                |                                  |
| 23    | modeSystem        |            |                | system operating mode            |
| 24    | modeFlight        |            |                | flight controller operating mode |
| 25    | modeControlFlight |            |                | flight control mode              |
| 26    | modeMovement      |            |                | moving state                     |
| 27    | headless          |            |                | headless setting status          |
| 28    | sensorOrientation |            |                | sensor orientation               |
| 29    | battery level     | %          | 0 - 100        | will not takeoff if below 50     |
| 30    | speed             | %          | 0 - 100        | current setting                  |

# Steps for Success
- Complete Getting Started course
- Complete pre-flight checks.
 - Clean propellers before each match
- Follow all safety and flight rules
- Watch all videos
- Treat hardware with care and store it properly

# Motor Care Updates
- Severe impact or crash (accidents happen)
 - Keep extra motors on hand 
- Motor overheating without cooldown period
 - After a flight check battery status
 - Give the drone a break
- Motor stalling or not spinning
- Missing silicone bumpers
 - Inspect and replace if appropriate 
- Cracked frame
- Pinched motor wires
 - Check wires after any maintenance task 

# References
[Getting Started](https://learn.robolink.com/product/codrone-edu) 
[Python for Robolink](https://codrone.robolink.com/edu/python/) 
[New Documentation Site](https://docs.robolink.com/) 
[How to take care of your motors]() 
[User Manual] 
[Basecamp](https://learn.robolink.com/) 
[Support](mailto:support@robolink.com)
