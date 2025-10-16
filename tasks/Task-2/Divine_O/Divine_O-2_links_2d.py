''' 
All libraries are imported at the start to help organize the code, 
provide ready-made tools available within the program,
and make the code easier to read, readily knowing the external tools used
'''


import numpy as np 
# Numpy library can be used to perform array, matrices and mathematical functions
# 'np' is the new variable representing 'numpy' in this program for ease of use

import matplotlib.pyplot as plt
# matplotlib library is used for data visualization and graph plotting.
# pyplot module of matplotlib used for plotting is saved as 'plt' for ease of use

from matplotlib.widgets import Slider
# from the widgets module of matplotlib that adds interactive features to a plot (buttons, check buttons...), we import slider class

# --- predefined link lengths (in arbitrary units) ---
L1 = 1.5
L2 = 1.0

# We assign float values of '1.5' and '1.0' into variables L1 and L2.
# The values represent the length of the robot links
# defined outside the function 'fk' because it is fixed


def fk(theta1, theta2):
# Created the function 'fk' to define forward kinematics algorithm, the heart of the robot.
# theta1 and theta2 are function parameters. They function as placeholders to hold the actual value when the function is called.

    """Forward kinematics for a 2R planar arm (angles in radians)."""
    x1 = L1*np.cos(theta1)
    # This line calculates the x co-ordinate at the end of link1. It performs L1 x cos(theta1), and saves the value as x1
    # We use numpy's (np) function of cosine on theta1, hence np.cos(theta1) 
    y1 = L1*np.sin(theta1)
    # This line calculates the y co-ordinate at the end of link1. It uses numpy's sine function.
    x2 = x1 + L2*np.cos(theta1 + theta2)
    # This line calculates the end of the x co-ordinate at the end of the second link. 'x1' represents the first algorithm to help reduce redundancy.
    y2 = y1 + L2*np.sin(theta1 + theta2)
    # Calculation of the y co-ordinate at the end of the second link.
    return (0, 0), (x1, y1), (x2, y2)
    # This function returns 3 co-ordinates. (0,0) representing the base joint/origin
    # (x1,y1) representing the joint at the end of link1
    # (x2,y2) representing the joint at the end of link2 or the position of the end-effector
    # These 3 co-ordinates are needed to plot or visualize the robotic arm.

# --- figure and axes ---
# This next block of code defines the plotting environment where the arm would be displayed
# It's like getting a sheet of paper and ruling a graph so you can draw to scale
plt.figure(figsize=(7, 7))
# This creates a figure/ plotting window equal in length and height
ax = plt.subplot(111)
# This defines where in the window to draw the arm. It is actually plt.subplot(nrows, ncols, index)
# nrows -> defines how many rows are stacked vertically
# ncols -> defines how many columns are arranged side-by-side
# index -> specifies which subplot area is to be activated 
ax.set_aspect("equal", adjustable="box")
# method 'set_aspect' adjusts the aspect ratio for the figure. It ensures the axes units are equal
# It also allows matplotlib automatically resize or adjust the axes box to keep the aspect ratio equal.
ax.set_xlim(- (L1+L2+0.2), L1+L2+0.2)
# This method 'set_xlim' sets the viewing limit of the x axes to +- the total robot links length when fully extended plus a margin of 0.2
ax.set_ylim(- (L1+L2+0.2), L1+L2+0.2)
# This method 'set_ylim' sets the viewing limit of the y axes to +- the total robot links length when fully extended plus a margin of 0.2
ax.grid(True, linestyle="--", linewidth=0.5)
# Enables and Customizes the plot grid lines
#True turns the grid on, specifies dashed line type with a linewidth of 0.5
ax.set_title("2-Link Planar Arm (use sliders below)")
# labels the plot with the description string

# initial angles (radians)
theta1_0 = np.deg2rad(30.0)
# converts 30 degrees initial angle of base joint to rad
theta2_0 = np.deg2rad(30.0)
#converts 30 degrees initial angle of second joint to rad

# draw initial arm
base, joint, ee = fk(theta1_0, theta2_0)
# calls forward kinematics algorithm function, passes in the values of 30 degrees in radians as theta 1 and 2
# computes the cordinate values of the base, first joint and end effector and saves it as 'base', 'joint' and 'ee' variables
(link_line,) = ax.plot([base[0], joint[0], ee[0]],
                       [base[1], joint[1], ee[1]],
                       marker="o", linewidth=3)
# plots the base, joint and ee x cordinates [0] against the y cordinates [1], with a marker at the cordinate points and a line of weight 3 connecting them
ee_text = ax.text(0.02, 0.98, "", transform=ax.transAxes,
                  va="top", ha="left", fontsize=10,
                  bbox=dict(boxstyle="round", fc="w", ec="0.7"))
#ax.text adds a text label in the plot and describes the look of the box. Setting 0.02 and 0.98 as the axes fraction units; "" means the text updates with end effector angles and positions; the text box is at the top left corner with text of size 10 font in a bounding box with round edges, white space fill and 0.7 light gray border.

# --- slider axes (beneath plot) ---
slider_ax1 = plt.axes([0.15, 0.05, 0.7, 0.03])
#creates an axes area for the first slider describing 15%,5%,70% and 3% of [distance from left edge, distance from bottom edge, width of axes, height of axes] 
slider_ax2 = plt.axes([0.15, 0.01, 0.7, 0.03])
#creates an axes area for the second slider describing 15%, 1%,70% and 3% of [distance from left edge, distance from bottom edge, width of axes, height of axes] 
#This is later used to create the actual slider widget.

s_theta1 = Slider(slider_ax1, 'θ1 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta1_0))
#This line creates the actual slider widget for theta1. The axes plot function is called 'slider_ax1) to create the plotting area for the slider; the slider is labelled 'θ1 (deg)', the minimum and maximum values of the slider are specified as -180 to 180, allowing full range motion of the robot, the initial value of the slider when the program is run is given by valinit, which gets the initial value of the program but converts it to degrees since the slider is labelled in degrees.
s_theta2 = Slider(slider_ax2, 'θ2 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta2_0))
#Performs a similar function to s_theta1 but for theta2

def update(_):
#update function
    th1 = np.deg2rad(s_theta1.val)
    #reads the slider value for theta1 and converts to radian
    th2 = np.deg2rad(s_theta2.val)
    #reads the slider value for theta2 and converts to radian
    b, j, e = fk(th1, th2)
    #runs the forward kinematics function passing in the read values and returns the co-ordinate values of base, joint and end effector
    link_line.set_data([b[0], j[0], e[0]], [b[1], j[1], e[1]])
    #updates data and connects the link lines using the calculated x and y coordinate
    ee_text.set_text(f"EE: x={e[0]:.3f}, y={e[1]:.3f}\nθ1={np.rad2deg(th1):.1f}°, θ2={np.rad2deg(th2):.1f}°")
    #updates data in the end effector textbox using the new values of theta1, theta2, and end effector coordinates (x,y)
    plt.draw()
    #redraws the plot figure with updated link connections and end effector text label

s_theta1.on_changed(update)
#calls the update function whenever the slider values for theta1 changes
s_theta2.on_changed(update)
#calls the update function whenever the slider values for theta2 changes
update(None)
#No argument is being passed into the update function although it is possible to pass into it. Not necessary because the variables needed are predetermined and appear in the function body

plt.show()
#command to open the matplotlib interactive window and display the coded diagram
