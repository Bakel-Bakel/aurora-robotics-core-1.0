
import numpy as np #import numpy for numerical calculations
import matplotlib.pyplot as plt #import matplotlib, a vizualization library
from matplotlib.widgets import Slider #import the slider component from the matplotlib library

# --- predefined link lengths (in arbitrary units) ---
L1 = 1.5 # length of first link
L2 = 1.0 # length of second link

def fk(theta1, theta2): #defining the forward kinematics function that takes in two values(angle)
    """Forward kinematics for a 2R planar arm (angles in radians)."""
    x1 = L1*np.cos(theta1) #x-axis position of link (1)->(2) joint
    y1 = L1*np.sin(theta1) #y-axis position of link (1)->(2) joint
    X = x1 + L2*np.cos(theta1 + theta2) #x-axis final position of link 2 end effector
    Y = y1 + L2*np.sin(theta1 + theta2) #y-axis final position of link 2 end effector
    return (0, 0), (x1, y1), (X, Y) # functuin returns the position values

# --- figure and axes ---
plt.figure(figsize=(5, 5)) #this determines the size of the plot environment
ax = plt.subplot(111) #determines the size of the subplot, 111 fits the subplot to the figsize
ax.set_aspect("equal", adjustable="box") #this line allows equal scaling when the window is adjusted.
ax.set_xlim(- (L1+L2+0.2), L1+L2+0.2) #centers the plot around the origin and sets max limit on the X-axis to total length plus small margin
ax.set_ylim(- (L1+L2+0.2), L1+L2+0.2) #centers the plot around the origin and sets max limit on the Y-axis to total length plus small margin
ax.grid(True, linestyle="--", linewidth=0.5) #adds a grid to the plot with dashed lines and thin width
ax.set_title("2-Link Planar Arm (use sliders below)") #gives the plot a title

# initial angles (radians)
theta1_0 = np.deg2rad(30.0) #initial angle of the first link, comverted from degrees to radians
theta2_0 = np.deg2rad(30.0) #initial angle of the second link, comverted from degrees to radians

# draw initial arm
base, joint, ee = fk(theta1_0, theta2_0) # assigns the retune values from the fk function to those variables
(link_line,) = ax.plot([base[0], joint[0], ee[0]], #plots the lines connecting the base, joint, and end effector
                       [base[1], joint[1], ee[1]], 
                       marker="o", linewidth=3)
ee_text = ax.text(0.02, 0.98, "", transform=ax.transAxes,
                  va="top", ha="left", fontsize=10,
                  bbox=dict(boxstyle="round", fc="w", ec="0.7")) #adds a text box to the plot to display the end effector positionand the joint angles.

# --- slider axes (beneath plot) ---
slider_ax1 = plt.axes([0.15, 0.05, 0.7, 0.03]) #sets the positiom and size of the first slider with the format [left, bottom, width, height] 
slider_ax2 = plt.axes([0.15, 0.01, 0.7, 0.03]) #sets the positiom and size of the second slider with the format [left, bottom, width, height]

s_theta1 = Slider(slider_ax1, 'θ1 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta1_0)) #creates the first slider for controlling the angle of the firts link
s_theta2 = Slider(slider_ax2, 'θ2 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta2_0)) #creates the second slider for controlling the angle of the second link

def update(_): #this function is called when the slider values change. It updates the arm position on the plot and the text box with the new position and angle.
    th1 = np.deg2rad(s_theta1.val) #converts the value of the first slider from degrees to radians
    th2 = np.deg2rad(s_theta2.val) #converts the value of the second slider from degrees to radians
    b, j, e = fk(th1, th2) #calculates the new positions of the arm segments
    link_line.set_data([b[0], j[0], e[0]], [b[1], j[1], e[1]]) #this line updates the plot with the new positions of the base, joint, and end effector
    ee_text.set_text(f"EE: x={e[0]:.3f}, y={e[1]:.3f}\nθ1={np.rad2deg(th1):.1f}°, θ2={np.rad2deg(th2):.1f}°") #this line updates the text box with the new end effector position and the joint angles in degrees
    plt.draw() #this line redraws the plot to reflect the changes made by the update function

s_theta1.on_changed(update) #this function calls the update function whenever the value of the first slider changes
s_theta2.on_changed(update) #this function calls the update function whenever the value of the second slider changes
update(None) #initial call to update the plot with the initial slider values

plt.show() #this displays the plot and starts the interactive session
