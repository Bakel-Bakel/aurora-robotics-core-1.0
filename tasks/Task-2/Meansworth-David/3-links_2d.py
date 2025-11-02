 
import numpy as np #Importing numpy to enable mathematical computations
import matplotlib.pyplot as plt #Importing matplotlib for visualization of the links 
from matplotlib.widgets import Slider #Here we import an interactive control, the slider which is used to control the arm's position in space

# --- predefined link lengths (in arbitrary units) ---
L1 = 1.5 # defining the first link
L2 = 1.0 # defining the secondlink
L3 = 1.5

def fk(theta1, theta2): #This function is used to define the positiion of the two links in space in respect to the angles between each-other and the ground level
    """Forward kinematics for a 2R planar arm (angles in radians)."""
    x1 = L1*np.cos(theta1) #Defines the position of link 1 in space with respect to the x-axis
    y1 = L1*np.sin(theta1) #Defines the position of the first link in space with respect to the y-axis 
    x2 = x1 + L2*np.cos(theta1 + theta2)  #Defines the position of link 2 in space with respect to the x-axis
    y2 = y1 + L2*np.sin(theta1 + theta2)  #Defines the position of the second link in space with respect to the y-axis
    return (0, 0), (x1, y1), (x2, y2) #This line returns the position of the two links with respect to an origin (0,0)

def fk1(theta1, theta2, theta3): #This function is used to define the positiion of the two links in space in respect to the angles between each-other and the ground level
    """Forward kinematics for a 2R planar arm (angles in radians)."""
    x1 = L1*np.cos(theta1) #Defines the position of link 1 in space with respect to the x-axis
    y1 = L1*np.sin(theta1) #Defines the position of the first link in space with respect to the y-axis 
    x2 = x1 + L2*np.cos(theta1 + theta2)  #Defines the position of link 2 in space with respect to the x-axis
    y2 = y1 + L2*np.sin(theta1 + theta2)  #Defines the position of the second link in space with respect to the y-axis
    x3 = x2 + L3*np.cos(theta1 + theta2 + theta3)
    y3 = y2 + L3*np.sin(theta1 + theta2 + theta3)
    return (0, 0), (x1, y1), (x2, y2), (x3, y3) #This line returns the position of the two links with respect to an origin (0,0)

# --- figure and axes ---
#This sectio gives the specification for the subplot
plt.figure(figsize=(7, 7)) #This creates a window for a plot and the 'fig-size represents the size of the window'
ax = plt.subplot(121) #This specifies the amount of sub-plots in the main plot (111) specifies 1 by 1 sub-plot and in the first position compared to (559) which is basically a bunch of plots forming a  5 by 5 grid and the plot in question is in the 9th grid
ax.set_aspect("equal", adjustable="box") # This sets the aspect ratio of the plot 'equal' meaning the x and y axis are equal ond 'adjustable = "box"' being the property of the grids to retain proportion 
ax.set_xlim(- (L1+L2+0.2), L1+L2+0.2) #This specifies the limits of the plot on the x-axis
ax.set_ylim(- (L1+L2+0.2), L1+L2+0.2) #This specifies the limits of the plot on the y-axis
ax.grid(True, linestyle="--", linewidth=0.5) #This specifies the grids line property ; true sets it on, linestyle defines how the grid-lines appear (dashed, dotted etc.) and the linewidth represents how wide the line looks
ax.set_title("2-Link Planar Arm (use sliders below)") #This represents the title for the sub-plot

bx = plt.subplot(122)
bx.set_aspect("equal", adjustable="box")
bx.set_xlim(- (L1+L2+L3+0.2), L1+L2+L3+0.2)
bx.set_ylim(- (L1+L2+L3+0.2), L1+L2+L3+0.2)
bx.grid(True, linestyle='--', linewidth=0.5)
bx.set_title("3-link Planar arm")

# initial angles (radians)
theta1_0 = np.deg2rad(30.0) #This sets the angles to be used to radians
theta2_0 = np.deg2rad(30.0) #This sets the angles to be used to radians
theta3_0 = np.deg2rad(30.0)

# draw initial arm
base, joint, ee = fk(theta1_0, theta2_0) #This calls the previously defined function and gives its three outputs to the three variable names given
(link_line,) = ax.plot([base[0], joint[0], ee[0]], # This represents the position of the three points (base, joint and end effector) in space with respect to the x-axis
                       [base[1], joint[1], ee[1]], # This represents the position of the three points (base, joint and end effector) in space with respect to the y-axis
                       marker="*", linewidth=3) # This specifies the visualization of the joints and the links
ee_text = ax.text(0.20, 1.0, "", transform=ax.transAxes, # This renders  box with transform=ax.transAxes means position (0.02, 0.98) is relative to the axes, so it stays in the corner
                  va="top", ha="right", fontsize=12, #Specifies the position of the text
                  bbox=dict(boxstyle="round", fc="w", ec="0.7")) #Draws a box with a white background

#Draw 2nd 3-link arm
base, joint1, joint2, ee = fk1(theta1_0, theta2_0, theta3_0)
(link_line2,) = bx.plot([base[0], joint1[0], joint2[0], ee[0]],
                       [base[1], joint1[1], joint2[1], ee[1]],
                       marker="*", linewidth=3)
print(base[1], joint1[1], joint2[1], ee[1])

# --- slider axes (beneath plot) ---
slider_ax2 = plt.axes([0.15, 0.01, 0.7, 0.03]) # This specifies the first slider's size and position being in format [horizontal position, vertical position, width, height]
slider_ax1 = plt.axes([0.15, 0.05, 0.7, 0.03]) # This specifies the second slider's size and position being in format [horizontal position, vertical position, width, height]
slider_ax3 = plt.axes([0.15, -0.02, 0.7, 0.03])

# This sets up the functionality of the slider
s_theta1 = Slider(slider_ax1, 'θ1 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta1_0)) # Specified slider to be used, title of slider, range of slider, starting point of slider
s_theta2 = Slider(slider_ax2, 'θ2 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta2_0)) # Specified slider to be used, title of slider, range of slider, starting point of slider
s_theta3 = Slider(slider_ax3, 'θ3 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta3_0)) # Specified slider to be used, title of slider, range of slider, starting point of slider

def update(_): # This updates the plot in real time 
    th1 = np.deg2rad(s_theta1.val) #Obtains the new value of theta1 from the slider and converts it to radians
    th2 = np.deg2rad(s_theta2.val) #Obtains the new value of theta2 from the slider and converts it to radians
    th3_ = np.deg2rad(s_theta3.val) #Obtains the new value of theta1 from the slider and converts it to radians
    print(s_theta3)
    
    b, j, e = fk(th1, th2) # substitutes the values from the sliders into the variables b, j, e
    link_line.set_data([b[0], j[0], e[0]], [b[1], j[1], e[1]]) #sets the x and y positions of the new point 
    ee_text.set_text(f"EE: x={e[0]:.3f}, y={e[1]:.3f}\nθ1={np.rad2deg(th1):.1f}°, θ2={np.rad2deg(th2):.1f}°") # Updats the text with the new positions
    plt.draw() #Rewrites the plot with the new position of the links and joints

    b, j1, j2, e = fk1(th1, th2, th3_) # substitutes the values from the sliders into the variables b, j, e
    link_line2.set_data([b[0], j1[0], j2[0], e[0]], [b[1], j1[1], j2[1], e[1]]) #sets the x and y positions of the new point 
    ee_text.set_text(f"EE: x={e[0]:.3f}, y={e[1]:.3f}\nθ1={np.rad2deg(th1):.1f}°, θ2={np.rad2deg(th2):.1f}°") # Updats the text with the new positions
    plt.draw()

s_theta1.on_changed(update) #This tells python that whenever the slider1 is changed call the update function
s_theta2.on_changed(update) #This tells python that whenever the slider2 is changed call the update function
s_theta3.on_changed(update)
update(None) #This calls the function at default position

plt.show() # This shows the interactive plot
