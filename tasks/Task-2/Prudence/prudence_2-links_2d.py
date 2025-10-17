
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# --- predefined link lengths (in arbitrary units) ---
L1 = 1.5
L2 = 1.0

def fk(theta1, theta2):
    """Forward kinematics for a 2R planar arm (angles in radians)."""
    x1 = L1*np.cos(theta1)
    y1 = L1*np.sin(theta1)
    x2 = x1 + L2*np.cos(theta1 + theta2)
    y2 = y1 + L2*np.sin(theta1 + theta2)
    return (0, 0), (x1, y1), (x2, y2)

# --- figure and axes ---
plt.figure(figsize=(7, 7))
ax = plt.subplot(111)
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(- (L1+L2+0.2), L1+L2+0.2)
ax.set_ylim(- (L1+L2+0.2), L1+L2+0.2)
ax.grid(True, linestyle="--", linewidth=0.5)
ax.set_title("2-Link Planar Arm (use sliders below)")

# initial angles (radians)
theta1_0 = np.deg2rad(30.0)
theta2_0 = np.deg2rad(30.0)

# draw initial arm
base, joint, ee = fk(theta1_0, theta2_0)
(link_line,) = ax.plot([base[0], joint[0], ee[0]],
                       [base[1], joint[1], ee[1]],
                       marker="o", linewidth=3)
ee_text = ax.text(0.02, 0.98, "", transform=ax.transAxes,
                  va="top", ha="left", fontsize=10,
                  bbox=dict(boxstyle="round", fc="w", ec="0.7"))

# --- slider axes (beneath plot) ---
slider_ax1 = plt.axes([0.15, 0.05, 0.7, 0.03])
slider_ax2 = plt.axes([0.15, 0.01, 0.7, 0.03])

s_theta1 = Slider(slider_ax1, 'θ1 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta1_0))
s_theta2 = Slider(slider_ax2, 'θ2 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta2_0))

def update(_):
    th1 = np.deg2rad(s_theta1.val)
    th2 = np.deg2rad(s_theta2.val)
    b, j, e = fk(th1, th2)
    link_line.set_data([b[0], j[0], e[0]], [b[1], j[1], e[1]])
    ee_text.set_text(f"EE: x={e[0]:.3f}, y={e[1]:.3f}\nθ1={np.rad2deg(th1):.1f}°, θ2={np.rad2deg(th2):.1f}°")
    plt.draw()

s_theta1.on_changed(update)
s_theta2.on_changed(update)
update(None)

plt.show()



 
import numpy as np #imported numpy as np
import matplotlib.pyplot as plt #imported matplotlib.pyplot as plt
from matplotlib.widgets import Slider #imported Slider from matplotlib.widgets

# --- predefined link lengt hs (in arbitrary units) ---
L1 = 1.5
L2 = 1.0

def fk(theta1, theta2): #defined a function fk that takes 2 parameters theta1 and theta2
    """Forward kinematics for a 2R planar arm (angles in radians)."""
    x1 = L1*np.cos(theta1) #calculated for the value of x1 using the euation gotten from the forward kinematics calculation
    y1 = L1*np.sin(theta1) #calculated for the value of y1 using the euation gotten from the forward kinematics calculation
    x2 = x1 + L2*np.cos(theta1 + theta2) #calculated for the value of x2 using the euation gotten from the forward kinematics calculation
    y2 = y1 + L2*np.sin(theta1 + theta2) #calculated for the value of y2 using the euation gotten from the forward kinematics calculation
    return (0, 0), (x1, y1), (x2, y2) #returned the values of the base, the joint and the end effector

# --- figure and axes ---
plt.figure(figsize=(7, 7)) # creates a new plot figure that is 7 by 7 inches
ax = plt.subplot(111) # adds a single subplot to the figure 1 row 1 column
ax.set_aspect("equal", adjustable="box") #Ensures that 1 unit on the x-axis = 1 unit on the y-axis.
ax.set_xlim(- (L1+L2+0.2), L1+L2+0.2) #sets limits for the plot of x axis
ax.set_ylim(- (L1+L2+0.2), L1+L2+0.2) #sets limits for the plot of y axis
ax.grid(True, linestyle="--", linewidth=0.5) #Turns on the grid for easier visualization with dashed lines
ax.set_title("2-Link Planar Arm (use sliders below)") #sets the title of the plot

# initial angles (radians)
theta1_0 = np.deg2rad(30.0) #converts 30 degrees to radians
theta2_0 = np.deg2rad(30.0) #converts 30 degrees to radians

# draw initial arm   #assigns the returned values of the fk function to base, joint and ee as a tuple
base, joint, ee = fk(theta1_0, theta2_0)
(link_line,) = ax.plot([base[0], joint[0], ee[0]], #draws a line througth the 3 key points ,the base ,joint and ee using the initial values [0]
                       [base[1], joint[1], ee[1]], #draws a lone througth the 3 key points ,the base ,joint and ee using the second values [1]
                       marker="o", linewidth=3) #sets the marker to be a circle and the linewidth to be 3
ee_text = ax.text(0.02, 0.98, "", transform=ax.transAxes, #adds a text box to the plot at the top left corner
                  va="top", ha="left", fontsize=10, #sets the vertical alignment to top and horizontal alignment to left
                  bbox=dict(boxstyle="round", fc="w", ec="0.7"))

# --- slider axes (beneath plot) ---
slider_ax1 = plt.axes([0.15, 0.05, 0.7, 0.03]) #this creates a slider axis for link 1 with values for top bottom width and height
slider_ax2 = plt.axes([0.15, 0.01, 0.7, 0.03]) #this creates a slider axis for link 2 with values for top bottom width and height

s_theta1 = Slider(slider_ax1, 'θ1 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta1_0)) #creates the slider for link 1 Slider(axis, label, min, max, valinit)
s_theta2 = Slider(slider_ax2, 'θ2 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta2_0)) #creates the slider for link 2 Slider(axis, label, min, max, valinit)

def update(_): #defines a function update to update the new position of the robot arm based on the slider that takes one parameter _
    """Update the arm position based on the slider values."""
    th1 = np.deg2rad(s_theta1.val) # takes the value of the slider 1, converts it to radians and assigns it to th1
    th2 = np.deg2rad(s_theta2.val) # takes the value of the slider 2, converts it to radians and assigns it to th2
    b, j, e = fk(th1, th2) #calls the fk function with the new angles and assigns the returned values to b, j and e
    link_line.set_data([b[0], j[0], e[0]], [b[1], j[1], e[1]]) #updates the line data to the new positions of the base, joint and end effector
    ee_text.set_text(f"EE: x={e[0]:.3f}, y={e[1]:.3f}\nθ1={np.rad2deg(th1):.1f}°, θ2={np.rad2deg(th2):.1f}°") #updates the text box with the new end effector position and angles
    plt.draw() #redraws the plot

s_theta1.on_changed(update) #calls the update function when the value of slider 1 is changed
s_theta2.on_changed(update) #`calls the update function when the value of slider 2 is changed
update(None)#

plt.show()#displays the plot with the robot arm and sliders

