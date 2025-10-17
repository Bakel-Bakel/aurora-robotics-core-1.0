
import numpy as np  #imports the NumPy package and refers to it as np
import matplotlib.pyplot as plt #imports the pyplot subpackage under the matplotlib and names it as plt
from matplotlib.widgets import Slider #from the widgets subpackage(under the matplotlib package), the Slider class is imported

# --- predefined link lengths (in arbitrary units) ---
L1 = 1.5 #length for link 1, L1
L2 = 1.0 #length for link 2, L2

def fk(theta1, theta2): #function fk witha two inputs theta1 and theta2
    """Forward kinematics for a 2R planar arm (angles in radians)."""
    x1 = L1*np.cos(theta1) #formula for x1, which is L1 times cos(theta1).The np.cos() basically applies cosine
    y1 = L1*np.sin(theta1) # formula for x2. the np.sin() applies the sine function to theta1
    x2 = x1 + L2*np.cos(theta1 + theta2) # formula for x2 which adds x1 to the cosine of theta1 plus theta2
    y2 = y1 + L2*np.sin(theta1 + theta2) # formula for y2 which adds y1 to the sine of theta1 plus theta2
    return (0, 0), (x1, y1), (x2, y2) # sends an output: a tuple of the base, the link 1 and link 2. these are the coordinates for this that will be plotted 

# --- figure and axes ---
plt.figure(figsize=(7, 7)) #this creates a window to plot that is 7 inches wide and 7 inches tall
ax = plt.subplot(111) # this creaates one row, one column and to the first(and only) subplot
ax.set_aspect("equal", adjustable="box") # sets the aspect ratio of the axes. "equals" makes the 1 unit on the x-axis the same lenagth as 1 unit on the y-axis. "box" adjusts the the plot are to make the axes equal
ax.set_xlim(- (L1+L2+0.2), L1+L2+0.2) # sets the visible upper and lower limit for the x-axis
ax.set_ylim(- (L1+L2+0.2), L1+L2+0.2) # sets the visible upper and lower limits for the y-axis
ax.grid(True, linestyle="--", linewidth=0.5) # sets the grid lines on, the linesyle to a dash style and the width of the grid line to 0.5 points
ax.set_title("2-Link Planar Arm (use sliders below)") # gives the plot a title

# initial angles (radians)
theta1_0 = np.deg2rad(30.0) # this converts the initial angle of joint 1 from degrees to radians and saves it to theta1_0
theta2_0 = np.deg2rad(30.0) # this converts the initial angle of joint 2 from degreees to radians and saves it to theta2_0

# draw initial arm
base, joint, ee = fk(theta1_0, theta2_0) # asigns the outputs of the function fk to base, joint and ee respectively 
(link_line,) = ax.plot([base[0], joint[0], ee[0]],
                       [base[1], joint[1], ee[1]],
                       marker="o", linewidth=3) # it plots the arm by connecting the x-coordinates to their corresponding y-coordinates, it sets the marker of the points to a circle indicated by 'o' and sets the thickness to 3 points. it returns a list of line objects but because of the parentheses it only returns a single line object
ee_text = ax.text(0.02, 0.98, "", transform=ax.transAxes,
                  va="top", ha="left", fontsize=10,
                  bbox=dict(boxstyle="round", fc="w", ec="0.7")) # # this line creates a text box in the top-left corner of the plot that will later display the end-effector's coordinates and joint angles. It's initially empty but it gets updated when the sliders move


# --- slider axes (beneath plot) ---
slider_ax1 = plt.axes([0.15, 0.05, 0.7, 0.03]) # creates a new set of axes, but instead of a graph it would be where the first slider will be
slider_ax2 = plt.axes([0.15, 0.01, 0.7, 0.03]) # creates a new set of aces, bu instead of a graph it would be whee the second slider will be   

s_theta1 = Slider(slider_ax1, 'θ1 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta1_0)) # creaates a slider bar for controlling theta1, labeled 'θ1 (deg)', ranging from -180 degrees to 180 degreees, starting at 30 degrees
s_theta2 = Slider(slider_ax2, 'θ2 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta2_0)) # creates a slider bar for controlling theta2, labeled 'θ2 (deg)', ranginf from -180 degrees to 180 degrees, starting at 30 degrees

def update(_): # defines a function named update. '_' is just a placeholde
    th1 = np.deg2rad(s_theta1.val) # reads the current value of the first slider which is in degrees and converts it to radians and stores it in th1
    th2 = np.deg2rad(s_theta2.val) # reads the current value of the second slider which is in degrees, converts it to radians, and stores it in th2
    b, j, e = fk(th1, th2) # calls the fk function with the updated angles and returnd the new coordinates of the base, joint and end-effector
    link_line.set_data([b[0], j[0], e[0]], [b[1], j[1], e[1]]) # updates the line plot with new coordinated so that the arms redraws its new position
    ee_text.set_text(f"EE: x={e[0]:.3f}, y={e[1]:.3f}\nθ1={np.rad2deg(th1):.1f}°, θ2={np.rad2deg(th2):.1f}°") # updates the text box in the corner of the plot
    plt.draw() # redraws the plot immediately, so that the changes appear when the slider moves

s_theta1.on_changed(update) # connects the slider s_theta1 to the function update
s_theta2.on_changed(update) # connects  the slider s_theta2 to the function update
update(None) #calls update() once at the start. None just fills the _ argument in

plt.show() # shows the matplotlib interactive window with the robot arm plot
