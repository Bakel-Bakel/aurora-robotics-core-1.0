import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# --- predefined link lengths (in arbitrary units) ---
L1 = 1.5 # this is the length of link 1
L2 = 1.0 #length of link 2

def fk(theta1, theta2): # creates a function fk assumping forward kinematics
    """Forward kinematics for a 2R planar arm (angles in radians)."""
    x1 = L1*np.cos(theta1) #np is used to explain the trig to the computer
    y1 = L1*np.sin(theta1) # x1 is the distance between the point of origin and the end of link1 o the x axis (horizontal)
    # y1 s the distance along the y axxis
    x2 = x1 + L2*np.cos(theta1 + theta2) # x2 is the distance from the origin to the end of link 2 on the x axis, it encompasses link1 and thus x1
    y2 = y1 + L2*np.sin(theta1 + theta2) # y2 is the distance along the y axis, thus it encompasses y1 also since link1 and link2 are conjoined at the jint
    return (0, 0), (x1, y1), (x2, y2) # provides the calculated values at the end of the function x1, y1, x2, and y2

# --- figure and axes ---
plt.figure(figsize=(7, 7)) #initiates a figure of this size 7in ches by 7in window for the interactive display
ax = plt.subplot(111)  # creates a 1 x1 subplot grid 
ax.set_aspect("equal", adjustable="box")
#Set x and y limits for the graph to be 0.2 beyond the strecthed out dimensions for link 1 and link2 combined
ax.set_xlim(- (L1+L2+0.2), L1+L2+0.2) 
ax.set_ylim(- (L1+L2+0.2), L1+L2+0.2)
ax.grid(True, linestyle="--", linewidth=0.5) #setting linestyle and title for the figure
ax.set_title("2-Link Planar Arm (use sliders below)")

# initial angles (radians) , serves as starting point for the sliders of theta1 &2
theta1_0 = np.deg2rad(30.0)
theta2_0 = np.deg2rad(30.0)

# draw initial arm
base, joint, ee = fk(theta1_0, theta2_0) # this calls on the function fk with the initial input theta 1 and 2
(link_line,) = ax.plot([base[0], joint[0], ee[0]], #plot the base point end of joint 1 and the end of the effector (the end of link2)
                       [base[1], joint[1], ee[1]],
                       marker="o", linewidth=3)
ee_text = ax.text(0.02, 0.98, "", transform=ax.transAxes, # creates a text box 2% from the top and 98 % from the bottom 
                  va="top", ha="left", fontsize=10, # sets textbox fontsize and position
                  bbox=dict(boxstyle="round", fc="w", ec="0.7")) #set as rounded rectangle, with white fill and a grey border line 

# --- slider axes (beneath plot) ---
slider_ax1 = plt.axes([0.15, 0.05, 0.7, 0.03]) #setting position of the sliders for both thetas based on the positions and widths on the figure plot
slider_ax2 = plt.axes([0.15, 0.01, 0.7, 0.03]) #setting position for second slider

s_theta1 = Slider(slider_ax1, 'θ1 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta1_0)) #setting limit values for both sliders i.e. -180 degree max and 180 degree min
s_theta2 = Slider(slider_ax2, 'θ2 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta2_0))

def update(_): # updates the new slider values through the f function recalculating the positions of the links
    th1 = np.deg2rad(s_theta1.val) #converts slider values from degree to radians for theta 1
    th2 = np.deg2rad(s_theta2.val) #converts for theta 2
    b, j, e = fk(th1, th2) # finds values for base, jointa nd end from new theat inputs
    link_line.set_data([b[0], j[0], e[0]], [b[1], j[1], e[1]]) # sets new positions for the links 
    ee_text.set_text(f"EE: x={e[0]:.3f}, y={e[1]:.3f}\nθ1={np.rad2deg(th1):.1f}°, θ2={np.rad2deg(th2):.1f}°") #updates text box with new x, y , theta 1 and theta 2 points
    plt.draw() #drws it in the already open figure window
#connects the slider the update function so when it changes it runs the update function 
s_theta1.on_changed(update)
s_theta2.on_changed(update)
update(None)
#Shows figure 
plt.show()
