# 2-Link-2D Planar Robotic Arm

Introduction to Robotic Arms
What is Kinematics?
Forward Kinematics Explained
Mathematical Derivation
Code Breakdown
Running the Simulation


# Introduction to Robotic Arms
## What is a Robotic Arm?
A robotic arm is a mechanical device designed to mimic the movement of a human arm. It consists of:

Links/length (segments/bones) - The rigid parts that don't rotate.

Joints/positions (connections) - The parts that rotate or move.

End Effector - The "hand" or tool at the end (gripper, welding torch, etc.).

## World Applications:

Manufacturing assembly lines (car production).

Surgical robots (precision operations).

Warehouse automation (picking and packing).

3D printing and CNC machines.

Space exploration (Mars rovers).

## Our 2-Link Planar Arm:
        * End Effector (EE) - "Hand"
       /
      /  Link 2 (L2 = 1.0 unit)
     /
    * Joint 2 (Elbow) - θ2
   /
  /  Link 1 (L1 = 1.5 units)
 /
* Joint 1 (Base) - θ1 (Fixed to ground)
Planar means it moves only in 2D space (X and Y), not 3D.

N/B: We took our convention sign anticlock-wise.

## What is Kinematics?
Kinematics is the study of motion without considering forces. For robots, it answers two key questions:
1. Forward Kinematics (FK)
Question: "If I know the joint angles, where does the end effector end up?"
Example: If shoulder is at 30° or 0° and elbow at 45°, where is my fingertip?
2. Inverse Kinematics (IK)
Question: "If I want the end effector at position (x, y), what should the joint angles be?"
Example: To reach point (2, 1.5), what angles do I set?

But this this project focuses on Forward Kinematics.

## Forward Kinematics Explained as follows by my instructor(BAKEL BAKEL).
### The Problem:
Given:

Link lengths: L1, L2
Joint angles: θ1, θ2

## Find:

Position of Joint 2 (elbow): (x1, y1)
Position of End Effector: (x2, y2)

## The Solution Uses Trigonometry:
When a line of length L rotates by angle θ from the horizontal:

Horizontal distance = L × cos(θ).

Vertical distance = L × sin(θ).

       * (x, y)
      /|
     / |
  L /  | y = L × sin(θ)
   /   |
  /θ   |
 *─────*
   x = L × cos(θ)

## Mathematical Derivation
### Step 1: Finding Joint 1 Position (Elbow)
The first link rotates from the origin (0, 0) by angle θ1:

x1 = L1 × cos(θ1).

y1 = L1 × sin(θ1).
### Example Calculation:
### Given: L1 = 1.5, θ1 = 30° = 0.524 radians (which the computer understand)

x1 = 1.5 × cos(30°) = 1.5 × 0.866 = 1.299

y1 = 1.5 × sin(30°) = 1.5 × 0.5 = 0.75

Joint 1 is at (1.299, 0.75)
## Visual:

      * (1.299, 0.75) ← Joint 1/Elbow
     /|
    / | 0.75
1.5/  |
  /30°|
 *────*
(0,0) 1.299

### Step 2: Finding End Effector Position
The second link starts from Joint 1 position (x1, y1) and extends by length L2.
#### Key Insight: The second link's absolute angle is θ1 + θ2 (not just θ2!)
Why? Because θ2 is relative to Link 1, not the ground.
x2 = x1 + L2 × cos(θ1 + θ2)
y2 = y1 + L2 × sin(θ1 + θ2)
### Example Calculation:
#### Given: 
- L1 = 1.5, L2 = 1.0
- θ1 = 30° = 0.524 rad
- θ2 = 30° = 0.524 rad
- Joint 1 at (1.299, 0.75)

Total angle for Link 2 = θ1 + θ2 = 30° + 30° = 60°

x2 = 1.299 + 1.0 × cos(60°)
   = 1.299 + 1.0 × 0.5
   = 1.299 + 0.5
   = 1.799

y2 = 0.75 + 1.0 × sin(60°)
   = 0.75 + 1.0 × 0.866
   = 0.75 + 0.866
   = 1.616

End Effector is at (1.799, 1.616)
### Visual:
              * (1.799, 1.616) ← End Effector
             /
            / 1.0 (L2)
           /  at 60° total
          /
         * (1.299, 0.75) ← Joint 1
        /
       / 1.5 (L1)
      /  at 30°
     /
    * (0, 0) ← Base

# Complete Forward Kinematics Equations:
## For a 2-link planar arm:
### Base Position:        (x0, y0) = (0, 0)

### Joint 1 Position:     
x1 = L1 × cos(θ1)
                     
y1 = L1 × sin(θ1)

### End Effector: 
x2 = x1 + L2 × cos(θ1 + θ2)
                     
y2 = y1 + L2 × sin(θ1 + θ2)

### Or expanded:   
x2 = L1×cos(θ1) + L2×cos(θ1 + θ2)

y2 = L1×sin(θ1) + L2×sin(θ1 + θ2)

# Code 
N/B: Firstly install numpy - pip install numpy and also pip install .

N/B: The code are ones I numbers, while others are just description.
## Full Code:
1. python import numpy as np
### numpy - 
A math library that will help in calculating the trigonometry such as sine, cosine angles below.

2. import matplotlib.pyplot as plt
### matplotlib
A drawing/graphing library that will create visual plots after running the code.

3. from matplotlib.widgets import Slider -  (A special tool from matplotlib that creates those sliding bars you will see at the bottom of the graph plot.)

### Let's Predefined links lengths.
4. L1 = 1.5 - (fixed length of link 1 from base or origin(0, 0) to (x1, y1))
5. L2 = 1.0 - (fixed length of link 2 from base or origin(x1, y1) to (x2, y2))

6. def fk(theta1, theta2): - (This creates/call a function named fk (forward kinematics), Takes two inputs: theta1 (first joint angle) and theta2 (second joint angle)).
    """Forward kinematics for a 2R planar arm."""
7.    x1 = L1*np.cos(theta1)  - (Horizontal distance: from the base/origin to where the elbow is located).
8.    y1 = L1*np.sin(theta1)  - (vertical distance: from the base/origin to where the elbow is located).
9.    x2 = x1 + L2*np.cos(theta1 + theta2)  - (Start from the x1 elbow position to the L2 distance in the horizontal direction conponent).
10.    y2 = y1 + L2*np.sin(theta1 + theta2)  - (Start from the y1 elbow position to the L2 distance in the vertical direction conponent).
### N/B: These x2 and y2 lines of code Calculates where the fingertip/end effector is located
11.    return (0, 0), (x1, y1), (x2, y2)
### N/B: The return statement gives you the final result(threepoints/position, which are then connected with lines to draw the robot) after all the calculations are done.

### --- Create figure and axes ---
12. plt.figure(figsize=(7, 7)) - (Calling out matplotlib to create a square window interface with width and height 7inches each).
13. ax = plt.subplot(111) - (The ax variable instructing python to draw on the whole window as one area instead of it being divided into four).
14. ax.set_aspect("equal", adjustable="box") - (This line of code forces 1 unit right horizontal movement of the robot equals one 1 unit right vertical movement of the robot).
15. ax.set_xlim(-(L1+L2+0.2), L1+L2+0.2) - (Shows how far left and right your robot arm can reach).
16. ax.set_ylim(-(L1+L2+0.2), L1+L2+0.2) - (Shows how far up and down your robot arm can reach).
### N/B: 
The 0.2 units or padding gives extra space in the room so the arm doesn't touch the window/room edges and Adds those gray dashed grid lines you see will see in the graph.
17. ax.grid(True, linestyle="--", linewidth=0.5)
### N/B: 
grid(True) turns on the grid. The linestyle="--" enables dashed lines (- - - -). Tlinewidth=0.5 make the lines thin (i.e 0.5 pixels wide)

18. ax.set_title("2-Link Planar Arm (use sliders below)") # Adds the text at the top of the graph plot.


### Calculating the starting angle(30 angles) for joint 1/L1 (the base joint) of the robot.
19. theta1_0 = np.deg2rad(30.0)
### Calculating the starting angle(30 angles) for joint 2/L2 (the elbow joint) of the robot.
20. theta2_0 = np.deg2rad(30.0)
### N/B:
30.0 means 30 degrees which is then converted to radians with the function np.deg2rad() which Converts degrees to radians (what the computer needs).
Also The _0 The underscore-zero means "initial" or "starting value".


21. base, joint, ee = fk(theta1_0, theta2_0)
### N/B: 
The the above line of code calls out your forward kinematics(fk) function to figure out where all the robot parts are(that's the three positions).
The theta1_0, theta2_0 variables that stored our calculated radains angles is not spared out from the calling.

22. (link_line,) = ax.plot([base[0], joint[0], ee[0]], (This creates a list of X-positions).
                       [base[1], joint[1], ee[1]] (This creates a list of Y-positions),
                       marker="o", linewidth=3)

### Just For Clarity:
23. ax.plot connect the positions/points with the line seen in the graph.
marker="o" puts a circle (o) at each points/position(that's base, elbow, E.E)
linewidth=3 makes the lines thick (3 pixels wide).

24. = ax.text(0.02, 0.98, "", transform=ax.transAxes,
                  va="top", ha="left", fontsize=10,
                  bbox=dict(boxstyle="round", fc="w", ec="0.7"))
### N/B: 
The above text function "ax.text" stored inside the text/number variable "ee_text" creates that white text box in the top-left corner showing position and angles in the graph.
0.02 = 2% from the left edge (almost at the left).
0.98 = 98% from the bottom = near the top.
transform=ax.transAxes tells python when the running the code to use the Position (0.02, 0.98) as reference to the corner positions (top-left), not arm positions (meters).
va="top" indicate to python that box should be at vertical alignment at top.
ha="left" indicate to python that box should be at horizontal alignment at the left.
fontsize=10 instruct that the text font size should be 10 pixels.
boxstyle="round" tells the compiler to box edge to be round in shape.
fc="w" F indicates face color/background should be white
ec="0.7" edge color  will be light gray


### --- slider axes (beneath plot) ---
### Position and size of the first slider (left, bottom, width, height)
25. slider_ax1 = plt.axes([0.15, 0.05, 0.7, 0.03])
### Position and size of the second slider (left, bottom, width, height)
26. slider_ax2 = plt.axes([0.15, 0.01, 0.7, 0.03])

27. s_theta1 = Slider(slider_ax1, 'θ1 (deg)', -180.0,
                  180.0, valinit=np.rad2deg(theta1_0))
### N/B:
the first Slider function install the actual knob in that graph. It set the label (volume), set the range (-180 to 180), starting position.

28. s_theta2 = Slider(slider_ax2, 'θ2 (deg)', -180.0,
                  180.0, valinit=np.rad2deg(theta2_0))
### N/B: 
the second Slider function install the actual knob in that graph. It set the label (volume), set the range (-180 to 180), starting position.


29. def update(_):
    This function runs every time you move a slider. It updates the robot arm drawing and the text box.
30.    th1 = np.deg2rad(s_theta1.val)
    Reads the current position of the first slider and converts to radians.
31.    th2 = np.deg2rad(s_theta2.val)
    Reads the current position of the second slider and converts to radians.
32.    b, j, e = fk(th1, th2)
    This calls the forward kinematics function with the new angles to calculate where all the robot parts should be now
33.    link_line.set_data([b[0], j[0], e[0]], [b[1], j[1], e[1]])
    This Updates the blue lines and dots to show the robot arm in its new position
34.    ee_text.set_text(
        f"EE: x={e[0]:.3f}, y={e[1]:.3f}\nθ1={np.rad2deg(th1):.1f}°, θ2={np.rad2deg(th2):.1f}°")
    Updates the white text box in the top-left corner with the new values.

35. plt.draw() -

36. s_theta1.on_changed(update) -(Tells the first slider whenever you move, call the update function)
37. s_theta2.on_changed(update) -(Tells the second slider whenever you move, call the update function).
38. update(None) - (Runs the update function once when the program starts).


plt.show() - (Instruct the window and keeps it open, waiting for your interaction.)


# Just Incase You Need The Code for Direct Copy, Paste And Run. Here's It Below:

import numpy as np  # Firstly install numpy - pip install numpy
# numpy - A math library that will help in calculating the trigonometry such as sine, cosine angles below

# Firstly install matplotlib - pip install numpy matplotlib
import matplotlib.pyplot as plt
# matplotlib - A drawing/graphing library that will create visual plots after running the code.

# A special tool from matplotlib that creates those sliding bars you will see at the bottom of the graph plot.
from matplotlib.widgets import Slider

# --- predefined link lengths (in arbitrary units) ---
L1 = 1.5  # fixed length of link 1 from base or origin(0, 0) to (x1, y1)
L2 = 1.0  # fixed length of link 2 from base or origin(x1, y1) to (x2, y2)


# This creates/call a function named fk (forward kinematics), Takes two inputs: theta1 (first joint angle) and theta2 (second joint angle).
def fk(theta1, theta2):
    """Forward kinematics for a 2R planar arm (angles in radians)."""

    # Horizontal distance: from the base/origin to where the elbow is located.
    x1 = L1*np.cos(theta1)
    # vertical distance: from the base/origin to where the elbow is located.
    y1 = L1*np.sin(theta1)
    # Start from the x1 elbow position to the L2 distance in the horizontal direction conponent.
    x2 = x1 + L2*np.cos(theta1 + theta2)
    # Start from the y1 elbow position to the L2 distance in the vertical direction conponent.
    y2 = y1 + L2*np.sin(theta1 + theta2)
    # These x2 and y2 lines of code Calculates where the fingertip/end effector is located
    return (0, 0), (x1, y1), (x2, y2)
# The return statement gives you the final result(three points/position, which are then connected with lines to draw the robot) after all the calculations are done.


# --- figure and axes ---
# Calling out matplotlib to create a square window interface with width and height 7inches each
plt.figure(figsize=(7, 7))
# The ax variable instructing python to draw on the whole window as one area instead of it being divided into four.
ax = plt.subplot(111)
# This line of code forces 1 unit right horizontal movement of the robot equals one 1 unit right vertical movement of the robot.
ax.set_aspect("equal", adjustable="box")
# Shows how far left and right your robot arm can reach.
ax.set_xlim(- (L1+L2+0.2), L1+L2+0.2)
# Shows how far up and down your robot arm can reach.
ax.set_ylim(- (L1+L2+0.2), L1+L2+0.2)
# The 0.2 units or padding gives extra space in the room so the arm doesn't touch the window/room edges.
# Adds those gray dashed grid lines you see will see in the graph.
ax.grid(True, linestyle="--", linewidth=0.5)
# grid(True) turns on the grid.
# the linestyle="--" enables dashed lines (- - - -).
# linewidth=0.5 make the lines thin (i.e 0.5 pixels wide)
# Adds the text at the top of the graph plot.
ax.set_title("2-Link Planar Arm (use sliders below)")

# initial angles (radians)
# Calculates the starting angle(30 angles) for joint 1/L1 (the base joint) of the robot.
theta1_0 = np.deg2rad(30.0)
# Calculates the starting angle(30 angles) for joint 2/L2 (the elbow joint) of the robot.
theta2_0 = np.deg2rad(30.0)
# 30.0 means 30 degrees which is then converted to radians with the below function.
# np.deg2rad() Converts degrees to radians (what the computer needs)
# The _0 The underscore-zero means "initial" or "starting value".

# draw initial arm
# This Calls out your forward kinematics(fk) function to figure out where all the robot parts are(that's the three positions).
base, joint, ee = fk(theta1_0, theta2_0)
# The theta1_0, theta2_0 variables that stored our calculated radains angles is not spared out from the calling.

(link_line,) = ax.plot([base[0], joint[0], ee[0]],
                       [base[1], joint[1], ee[1]],
                       marker="o", linewidth=3)
# This creates a list of X-positions and this also creates a list of Y-positions

# ax.plot connect the positions/points with the line seen in the graph.
# marker="o" puts a circle (o) at each points/position(that's base, elbow, E.E)
# linewidth=3 makes the lines thick (3 pixels wide).

ee_text = ax.text(0.02, 0.98, "", transform=ax.transAxes,
                  va="top", ha="left", fontsize=10,
                  bbox=dict(boxstyle="round", fc="w", ec="0.7"))
# The above text function "ax.text" stored inside the text/number variable "ee_text" creates that white text box in the top-left corner showing position and angles in the graph.
# 0.02 = 2% from the left edge (almost at the left).
# 0.98 = 98% from the bottom = near the top.
# transform=ax.transAxes tells python when the running the code to use the Position (0.02, 0.98) as reference to the corner positions (top-left), not arm positions (meters).
# va="top" indicate to python that box should be at vertical alignment at top.
# ha="left" indicate to python that box should be at horizontal alignment at the left.
# fontsize=10 instruct that the text font size should be 10 pixels.
# boxstyle="round" tells the compiler to box edge to be round in shape.
# fc="w" F indicates face color/background should be white
# ec="0.7" edge color  will be light gray


# --- slider axes (beneath plot) ---
# Position and size of the first slider (left, bottom, width, height)
slider_ax1 = plt.axes([0.15, 0.05, 0.7, 0.03])
# Position and size of the second slider (left, bottom, width, height)
slider_ax2 = plt.axes([0.15, 0.01, 0.7, 0.03])

s_theta1 = Slider(slider_ax1, 'θ1 (deg)', -180.0,
                  180.0, valinit=np.rad2deg(theta1_0))
# the first Slider function install the actual knob in that graph. It set the label (volume), set the range (-180 to 180), starting position.

s_theta2 = Slider(slider_ax2, 'θ2 (deg)', -180.0,
                  180.0, valinit=np.rad2deg(theta2_0))
# the second Slider function install the actual knob in that graph. It set the label (volume), set the range (-180 to 180), starting position.


# This function runs every time you move a slider. It updates the robot arm drawing and the text box.
def update(_):
    # Reads the current position of the first slider and converts to radians.
    th1 = np.deg2rad(s_theta1.val)
    # Reads the current position of the second slider and converts to radians.
    th2 = np.deg2rad(s_theta2.val)
    # This calls the forward kinematics function with the new angles to calculate where all the robot parts should be now
    b, j, e = fk(th1, th2)
    # Updates the blue lines and dots to show the robot arm in its new position
    link_line.set_data([b[0], j[0], e[0]], [b[1], j[1], e[1]])
    ee_text.set_text(
        f"EE: x={e[0]:.3f}, y={e[1]:.3f}\nθ1={np.rad2deg(th1):.1f}°, θ2={np.rad2deg(th2):.1f}°")
    # Updates the white text box in the top-left corner with the new values.
    plt.draw()


# Tells the first slider whenever you move, call the update function.
s_theta1.on_changed(update)
# Tells the second slider whenever you move, call the update function.
s_theta2.on_changed(update)
update(None)  # Runs the update function once when the program starts.

# Instruct the window and keeps it open, waiting for your interaction.
plt.show()


# Running the Simulation
## Requirements:
pip install numpy matplotlib (INSTALL IN TERMINAL OR VS CODE)

Running:

python robot_arm.py

Using the Simulator:

Move θ1 slider (top): Controls base joint angle

Move θ2 slider (bottom): Controls elbow joint angle

Observe:

Arm moves in real-

Text box shows end effector position (x, y)

Text box shows current joint angles



# Example Configurations/ what I Experimented:

Configuration 1: Pointing Right
θ1 = 0°, θ2 = 0°

Result: Arm fully extended horizontally 

EE position: (2.5, 0)

Configuration 2: Pointing Up

θ1 = 90°, θ2 = 0°

Result: Arm pointing straight up

EE position: (0, 2.5)

Configuration 3: 

θ1 = 45°, θ2 = -90°

Result: Second link folds back

# Mathematical Verification
## Test Case 1:
Given: L1 = 1.5, L2 = 1.0, θ1 = 0°, θ2 = 0°

### Joint 1:
x1 = 1.5 × cos(0°) = 1.5 × 1 = 1.5

y1 = 1.5 × sin(0°) = 1.5 × 0 = 0

Position: (1.5, 0)

### End Effector:
x2 = 1.5 + 1.0 × cos(0°) = 1.5 + 1 = 2.5

y2 = 0 + 1.0 × sin(0°) = 0 + 0 = 0

Position: (2.5, 0)

Verification: Arm fully extended 

## Test Case 2:
Given: L1 = 1.5, L2 = 1.0, θ1 = 90°, θ2 = 0°

### Joint 1:
x1 = 1.5 × cos(90°) = 1.5 × 0 = 0

y1 = 1.5 × sin(90°) = 1.5 × 1 = 1.5
Position: (0, 1.5)

### End Effector:
x2 = 0 + 1.0 × cos(90°) = 0 + 0 = 

y2 = 1.5 + 1.0 × sin(90°) = 1.5 + 1 = 2.5

Position: (0, 2.5)

Verification: Arm pointing straight up

## Test Case 3:
Given: L1 = 1.5, L2 = 1.0, θ1 = 33.8°, θ2 = 30°

### Joint 1:
x1 = 1.5 × cos(33.8°) ≈ 1.5 × 0.831 ≈ 1.246

y1 = 1.5 × sin(33.8°) ≈ 1.5 × 0.556 ≈ 0.834

# End Effector:

x2 = 1.246 + 1.0 × cos(63.8°) ≈ 1.246 + 0.441 ≈ 1.

y2 = 0.834 + 1.0 × sin(63.8°) ≈ 0.834 + 0.897 ≈ 1.731

Result: EE ≈ (1.687, 1.731)
Your display shows: (1.688, 1.732) ✓

# Key Concepts Summary
Forward Kinematics Formula:

x = L1×cos(θ1) + L2×cos(θ1 + θ2)

y = L1×sin(θ1) + L2×sin(θ1 + θ2)

## Important Points:
Angles are cumulative: Second link angle is θ1 + θ2, not just θ2
Trigonometry is key: cos for horizontal, sin for vertical
Radians vs Degrees: Computers use radians, humans prefer degrees
Positions are additive: Each link adds to the previous position

## Workspace:
The robot arm can reach any point within the workspace or space as defined by:

Maximum reach: L1 + L2 = 2.5 units

Minimum reach: |L1 - L2| = 0.5 units (when folded or I experimented)

I will say it was a great experience during the class and in caring out the task. Just to add to the above information that the robot arm can be use in Path planning (moving along specific trajectories), Obstacle avoidance, Workspace analysis, Singularity detection.

Thanks for your time.