# Import the needed libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# --- predefined link lengths (in arbitrary units) ---
L1 = 2.0    # Define length of link 1
L2 = 1.5    # Define length of link 2
L3 = 1.0    # Define length of link 3


# Function to calculate the X and  Y axis of a forward kinematics of a robot 
def fk(theta1, theta2, theta3):
    """Forward kinematics for a #R planar arm (angles in radians)."""
    # Link 1
    x1 = L1*np.cos(theta1)                # Calculate x-coordinate of the first joint (end of link 1)
    y1 = L1*np.sin(theta1)                # Calculate y-coordinate of the first joint (end of link 1)

    # Link 2
    x2 = x1 + L2*np.cos(theta1 + theta2)  # Calculate x-coordinate of the second joint (end of link 2)
    y2 = y1 + L2*np.sin(theta1 + theta2)  # Calculate y-coordinate of the second joint (end of link 2)

    # Link 3
    x3 = x2 + L3 * np.cos(theta1 + theta2 + theta3) # Calculate x-coordinate of the end-effector (end of link 3)
    y3 = y2 + L3 * np.sin(theta1 + theta2 + theta3) # Calculate y-coordinate of the end-effector (end of link 3)
    return (0, 0), (x1, y1), (x2, y2), (x3, y3)     # Return the base point, coordinate of links of the robot

# Plot the 2d robotics arm
# --- figure and axes ---
plt.figure(figsize=(7, 7))                                   # Define the plot size
ax = plt.subplot(111)                                        # Define a subplot for the robot
plt.subplots_adjust(bottom=0.15)  # Increase bottom margin
ax.set_aspect("equal", adjustable="box")                     # Set aspect ratio
ax.set_xlim(- (L1+L2+L3+0.2), L1+L2+L3+0.2)                        # Set the limit for x-axis
ax.set_ylim(- (L1+L2+L3+0.2), L1+L2+L3+0.2)                        # Set the limit for y-axis
ax.grid(True, linestyle="--", linewidth=0.5)                 # Allow grid line
ax.set_title("3-Link Planar Arm (use sliders below)")        # Set plot title

# Define default angles
# initial angles (radians)
theta1_0 = np.deg2rad(30.0)       # Define the angle between the ground (or reference point) and link 1
theta2_0 = np.deg2rad(30.0)       # Define the angle between link 1 and link 2
theta3_0 = np.deg2rad(30.0)       # Define the angle between link 1 and link 2


# Used forward kinematics function from above to visualize the 2d robotics arm
# draw initial arm
# fixed (or reference) point, joint, end-effector
base, joint1, joint2, ee = fk(theta1_0, theta2_0, theta3_0)

# Draw the line object (for the arm)
# using the first base point, first joint point and the first end-effector for x-axis
# and the other base point, other joint point and the other end-effector for x-axis
# set a marker (dot) and a linewidth (or line thickness) of 3 points
(link_line,) = ax.plot([base[0], joint1[0], joint2[0], ee[0]],
                       [base[1], joint1[1], joint2[1], ee[1]],
                       marker="o", linewidth=3)

# Create a text box for end-effector at 2% from the left and 98% from the bottom relative to the arm axes
# aligned vertically to the top and horizontally to the left with a font size of 10
# box type to round, box background color to be white and edge color of 70%
ee_text = ax.text(0.02, 0.98, "", transform=ax.transAxes,
                  va="top", ha="left", fontsize=10,
                  bbox=dict(boxstyle="round", fc="w", ec="0.7"))


# --- slider axes (beneath plot) ---
# Set slider position for X-axis and Y-axis
# ----------------- [left, bottom, width, height]
slider_ax1 = plt.axes([0.15, 0.07, 0.7, 0.03])
slider_ax2 = plt.axes([0.15, 0.04, 0.7, 0.03])
slider_ax3 = plt.axes([0.15, 0.01, 0.7, 0.03])

# Define sliders (position, label, minimum and maximum values, default slider value)
s_theta1 = Slider(slider_ax1, 'θ1 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta1_0))
s_theta2 = Slider(slider_ax2, 'θ2 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta2_0))
s_theta3 = Slider(slider_ax3, 'θ3 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta3_0))


# Define a function to auto-update line plot based on slider input
def update(_):
    th1 = np.deg2rad(s_theta1.val)      # Convert slider 1 (deg) value to radian
    th2 = np.deg2rad(s_theta2.val)      # Convert slider 2 (deg) value to radian
    th3 = np.deg2rad(s_theta3.val)      # Convert slider 3 (deg) value to radian
    b, j1, j2, e = fk(th1, th2, th3)    # Compute positions: base, joint, and end-effector
    link_line.set_data([b[0], j1[0], j2[0], e[0]], [b[1], j1[1], j2[1], e[1]])   # Update the robot arm plot
    # Update end-effector info text
    ee_text.set_text(f"EE: x={e[0]:.3f}, y={e[1]:.3f}\nθ1={np.rad2deg(th1):.1f}°, θ2={np.rad2deg(th2):.1f}°, θ3={np.rad2deg(th3):.1f}°")
    plt.draw()                      # Redraw the figure to reflect changes                   

# Trigger a change when either of the sliders are move
s_theta1.on_changed(update)
s_theta2.on_changed(update)
s_theta3.on_changed(update)
update(None)


# Plot/show 2d robotics arm
plt.show()
