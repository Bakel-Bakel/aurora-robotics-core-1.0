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
