# two_link_sliders.py
import numpy as np #Numpy-Numerical Python is a library imported for working with arrays
import matplotlib.pyplot as plt #Matplotlib is a library for graph plotting, we access the pyplot package as plt for visualisation
from matplotlib.widgets import Slider  #Slider is a widget in matplotlib library for sliding or control over visual properties of the plot

# --- predefined link lengths (in arbitrary units) ---
L1 = 1.5   #Length of link 1
L2 = 1.0   #Length of link 2

def fk(theta1, theta2): #A function fk is defined, it takes in theta1, theta2 parameters(arguments)to compute x1,x2,y1,y2 data
    """Forward kinematics for a 2R planar arm (angles in radians)."""
    x1 = L1*np.cos(theta1) #This formula gets the value of x1 i.e from origin to tip of L1 in the x-direction
    y1 = L1*np.sin(theta1) #This formula gets the value of y1 i.e from origin to tip of L1 in the y-direction
    x2 = x1 + L2*np.cos(theta1 + theta2) #This formula gets the value of x2 i.e from origin to tip of L2 in the x direction, (X=x1+x2)
    y2 = y1 + L2*np.sin(theta1 + theta2) #This formula gets the value of y2 i.e from origin to tip of L2 in the y direction, (Y=y1+y2)
    return (0, 0), (x1, y1), (x2, y2)  #The return statement sends back values 0,0,x1,y1,x2,y2 to any program that call the def fk function
# --- figure and axes ---
plt.figure(figsize=(4, 4)) #Create a plot figure  with a size 7inches tall,7inches wide
ax = plt.subplot(111) #The subplot function take 3 arguments, 1 row, 1 column and the first plot in the figure and asigned ax
ax.set_aspect("equal", adjustable="box")  #This set the aspect ratio of the axis scaling
ax.set_xlim(- (L1+L2+0.2), L1+L2+0.2) #Set the x-axis view limits with Link 1 and Link 2
ax.set_ylim(- (L1+L2+0.2), L1+L2+0.2) #set the y-axis view limits
ax.grid(True, linestyle="--", linewidth=0.5) #configure the grid to show, -- style, 0.5 thickness
ax.set_title("2-Link Planar Arm (use sliders below)") #Set a title for the axes

# initial angles (radians)
theta1_0 = np.deg2rad(30.0) #convert angle 30 from degree to radian
theta2_0 = np.deg2rad(30.0) #convert angle 30 from degree to radian


# draw initial arm
base, joint, ee = fk(theta1_0, theta2_0) #initial angle theta is passed into the fk function then the value is returned into base, joint and ee
(link_line,) = ax.plot([base[0], joint[0], ee[0]], #draws line from point to point within the x-axis,y-axis
                       [base[1], joint[1], ee[1]], #the marker 'o' is used for the lines, 
                       marker="o", linewidth=3) #linewidth is 0 - 3
ee_text = ax.text(0.02, 0.98, "", transform=ax.transAxes,  #draws the text box at the top left corner
                  va="top", ha="left", fontsize=10, #set text alignment
                  bbox=dict(boxstyle="round", fc="w", ec="0.7")) #box around the text
 
# --- slider axes (beneath plot) ---
slider_ax1 = plt.axes([0.15, 0.05, 0.7, 0.03]) #this create a bar for the slider1, left, bottom, width, height
slider_ax2 = plt.axes([0.15, 0.01, 0.7, 0.03]) #the plt.axes()function in pyplot module is used to add axes for slider 2

s_theta1 = Slider(slider_ax1, 'θ1 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta1_0)) #Slider1 widget is created with slider axis
s_theta2 = Slider(slider_ax2, 'θ2 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta2_0)) #Slider2 widget is created

def update(_): #a function with one argument, ignored
    th1 = np.deg2rad(s_theta1.val) #converting degree to rad for th1
    th2 = np.deg2rad(s_theta2.val) #converting degree to rad for th2
    b, j, e = fk(th1, th2) #fk function is called
    link_line.set_data([b[0], j[0], e[0]], [b[1], j[1], e[1]]) #used for updating the data of the arm
    ee_text.set_text(f"EE: x={e[0]:.3f}, y={e[1]:.3f}\nθ1={np.rad2deg(th1):.1f}°, θ2={np.rad2deg(th2):.1f}°") #update text box
    plt.draw() #update the arm

s_theta1.on_changed(update) #whenever slider1 moves, update is called
s_theta2.on_changed(update) #connecting to slider2 to update function
update(None) #runs before slider is touch. None placeholder

plt.show() #display the generated plot
