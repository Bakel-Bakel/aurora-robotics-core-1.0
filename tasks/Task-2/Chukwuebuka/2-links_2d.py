#Import the numpy library with the name as np
import numpy as np

#Import the pyplot file from the matplotlib library with the name plt
import matplotlib.pyplot as plt

#Import the slider class from the widgets file in the matplotlib library
from matplotlib.widgets import Slider


# --- predefined link lengths (in arbitrary units) ---
L1 = 1.5 #Link 1 dimension
L2 = 1.0 #Link 2 dimension

#Foward Kinematic function, take in 2 argument theta1 and theta2
def fk(theta1, theta2):
    """Forward kinematics for a 2R planar arm (angles in radians)."""
    x1 = L1*np.cos(theta1) #Link 1 position in the x-axis
    y1 = L1*np.sin(theta1) #Link 1 position in the y-axis
    x2 = x1 + L2*np.cos(theta1 + theta2) #Link 2 position with relation to the Link 1 in the x-axis
    y2 = y1 + L2*np.sin(theta1 + theta2) #Link 2 position with relation to the Link 1 in the y-axis
    return (0, 0), (x1, y1), (x2, y2) #Returns the base position(0,0) the link1 position(x1,y1) and link2 position(x2,y2)

# --- figure and axes ---
#Gives the graph to a be plotted a specific dimension, in this case 7inches for the height and width.
plt.figure(figsize=(7, 7))

#Subplot() function provides the plot with some additional behaviour(in grid) which is diplayed subsequently. it takes in parameters which include nrow, ncol and index. The nrow and ncol indicate the amount of grid the plot will occupy and index is the particular position the grid will start, which 1 is the minimum. The sublot is assigned to ax for other additional behaviour.
ax = plt.subplot(111)

#All the following is not from the pyplot.py library but the base.py, except the grid and set_title, which is from the axes.py library. Maintain a particular scale with plot GUI, ie. if the size of the GUI is minimized the scale of the graph is the same.
ax.set_aspect("equal", adjustable="box")

#Sets the x-axis
ax.set_xlim(- (L1+L2+0.2), L1+L2+0.2)

#Sets the x-axis
ax.set_ylim(- (L1+L2+0.2), L1+L2+0.2)

#Add the grid inside the plot with the dashed linestyle and width of 0.5
ax.grid(True, linestyle="--", linewidth=0.5)

#Set te title of the plot
ax.set_title("2-Link Planar Arm (use sliders below)")

# initial angles (radians)
theta1_0 = np.deg2rad(30.0)
theta2_0 = np.deg2rad(30.0)

# draw initial arm
base, joint, ee = fk(theta1_0, theta2_0)#Get the 3 returns from the function call, with arg as the the angle initial.


#The (line_line,) represents a tuple unpacking, just to get the Line2D object, with the object the marker and linewidth can be used.
(link_line,) = ax.plot([base[0], joint[0], ee[0]],
                       [base[1], joint[1], ee[1]],
                       marker="o", linewidth=3)

#Add text to the axis. This just initial setting(a proper word can be used) since it will be changed in the update function.
ee_text = ax.text(0.02, 0.98, "", transform=ax.transAxes,
                  va="top", ha="left", fontsize=10,
                  bbox=dict(boxstyle="round", fc="w", ec="0.7"))

# --- slider axes (beneath plot) ---

#Customize the theta_1 and theta_2 Slider
slider_ax1 = plt.axes([0.15, 0.05, 0.7, 0.02])
slider_ax2 = plt.axes([0.15, 0.01, 0.7, 0.02])

#With the customized value this get the slider going, indicating the sliding range in degree
s_theta1 = Slider(slider_ax1, 'θ1 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta1_0))
s_theta2 = Slider(slider_ax2, 'θ2 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta2_0))

#Update function is responsible for making changes on the plot in realtime
def update(_):

    #Goes to the customize slidder and get the value of the slider with the .val then assign to to vaiable
    th1 = np.deg2rad(s_theta1.val)
    th2 = np.deg2rad(s_theta2.val)

    #With assigned variable call the Forward Kinematic function and assign them to the the variable b, j, e, since a return is expected
    b, j, e = fk(th1, th2)

    #With the Line2D call the method set_data for the plot
    link_line.set_data([b[0], j[0], e[0]], [b[1], j[1], e[1]])

    #Changes the text function already initialized
    ee_text.set_text(f"EE: x={e[0]:.3f}, y={e[1]:.3f}\nθ1={np.rad2deg(th1):.1f}°, θ2={np.rad2deg(th2):.1f}°")

    #Plot the graph
    plt.draw()

#Make the slider call the update function whenever the update function when the slidder Btn is moved
s_theta1.on_changed(update)
s_theta2.on_changed(update)

#Update function Call to be triggered when the script runs
update(None)

#Show the plot
plt.show()