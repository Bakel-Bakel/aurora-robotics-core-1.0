# Importing libraries
import numpy as np #for math operations
import matplotlib.pyplot as plt # For plotting on graphs
from matplotlib.widgets import Slider # Slider for adjusting values easier🤷‍♀️, From the matplotlib library

# --- predefined link lengths (in arbitrary units) ---
L1 = 1.5 #lever 1
L2 = 1.0 #Lever 2

#Function for calculating all the positions for the arm joints 
def fk(theta1, theta2): #collects the two joint angles in radians (for some reason)
    """Forward kinematics for a 2R planar arm (angles in radians)."""
    x1 = L1*np.cos(theta1) # calculates x-axis position of the 1st joint 
    y1 = L1*np.sin(theta1) # calculates y-axis position of the 1st joint 
    x2 = x1 + L2*np.cos(theta1 + theta2) # calculates x-axis position of the 2nd joint (relative to the ground, not to the 1st joint)
    y2 = y1 + L2*np.sin(theta1 + theta2) # calculates y-axis position of the 2nd joint (relative to ...)
    return (0, 0), (x1, y1), (x2, y2) #outputs the ground, first and second joint coordinates 

# --- figure and axes ---
plt.figure(figsize=(7, 7)) # Defining the figure, where the axes sould be displayed, width and height 7
ax = plt.subplot(111) #defining the subplot, in a grid of 1 by 1, 
ax.set_aspect("equal", adjustable="box") #Set the aspect ratio, not sure about the attributes and their specific meanings sha

#setting the min and max x and y-axis values 
ax.set_xlim(- (L1+L2+0.2), L1+L2+0.2) 
ax.set_ylim(- (L1+L2+0.2), L1+L2+0.2) 
# the limit is the two lever lengths combined ...
# plus an additional 0.2 for extra room (lower limit is the negative version)
# maybe making the "L1+L2" or "L1+L2+0.2" into a variable "maxLength" for more readability would be better 


ax.grid(True, linestyle="--", linewidth=0.5) #customizing the grid visibility, the line style and thickness
ax.set_title("2-Link Planar Arm (use sliders below)") #title of the axes

# initial angles (radians)
#converts the angles for the two joints from degrees to radians
theta1_0 = np.deg2rad(30.0)
theta2_0 = np.deg2rad(30.0)

# draw initial arm
base, joint, ee = fk(theta1_0, theta2_0) #using the two angles as arguements in the function previously defined,...
# the return values are the coordinates stored each ...
# into the base, joint and the end effector "ee"

(link_line,) = ax.plot([base[0], joint[0], ee[0]],# plotting the x-axis values on the axes
                       [base[1], joint[1], ee[1]],# plotting the y-axis values 
                       marker="o", linewidth=3) # putting the dots on each point and setting the thickness

#Creating a text box (ngl I used ai a bit to understand this part a bit better)
ee_text = ax.text(0.02, 0.98, "", transform=ax.transAxes, # setting the x, y-axis position, initial text (empty), Using axes coordinates (0 to 1)
                  va="top", ha="left", fontsize=10, #vertical, horizontal alignment, font size
                  bbox=dict(boxstyle="round", fc="w", ec="0.7")) #borderbox style (object: style, bg/faceColor, border/edgeColor)

# --- slider axes (beneath plot) ---
slider_ax1 = plt.axes([0.15, 0.05, 0.7, 0.03]) #creates a new axes, (left, bottom, width, height)
slider_ax2 = plt.axes([0.15, 0.01, 0.7, 0.03]) #same as above, but bottom position lowered to avoid overlapping

s_theta1 = Slider(slider_ax1, 'θ1 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta1_0)) #creates the slider, with axes, label, minValue, max, and initialValue
s_theta2 = Slider(slider_ax2, 'θ2 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta2_0)) #same as above
# -? Confused why we keep switching between rads and degrees, like is it compulsory?

#callback function that occurs when slider value is changed
def update(_):
    th1 = np.deg2rad(s_theta1.val) #collects the slider val of the first slider, converts to rads
    th2 = np.deg2rad(s_theta2.val) #collects the 2nd slider val
    b, j, e = fk(th1, th2) #obtains the current coordinates of the base, joint and end effector
    link_line.set_data([b[0], j[0], e[0]], [b[1], j[1], e[1]]) #replots the link-line with the new values
    ee_text.set_text(f"EE: x={e[0]:.3f}, y={e[1]:.3f}\nθ1={np.rad2deg(th1):.1f}°, θ2={np.rad2deg(th2):.1f}°") #updates the text in the box to the coordinates
    plt.draw() #redraws the plot abi figure

s_theta1.on_changed(update) #event handler attached to first slider
s_theta2.on_changed(update) # ...... attanched to 2nd slider
update(None) #🤷‍♀️ 

plt.show() #written at the end t properly display the figure
