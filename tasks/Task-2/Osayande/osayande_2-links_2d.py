
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# --- predefined link lengths (in arbitrary units) ---
L1 = 1.5  # link length 1
L2 = 1.0  # link length 2

def fk(theta1, theta2):   #defining a function which is for calculating forward kinematics
    """Forward kinematics for a 2R planar arm (angles in radians)."""
    x1 = L1*np.cos(theta1)  # x-coordinate of joint 1
    y1 = L1*np.sin(theta1)  # y-coordinate of joint 1
    x2 = x1 + L2*np.cos(theta1 + theta2) # x-coordinate of end-effector
    y2 = y1 + L2*np.sin(theta1 + theta2) # y-coordinate of end-effector
    return (0, 0), (x1, y1), (x2, y2)

# --- figure and axes ---
plt.figure(figsize=(7, 7))
ax = plt.subplot(111)
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(- (L1+L2+0.2), L1+L2+0.2)
ax.set_ylim(- (L1+L2+0.2), L1+L2+0.2)
ax.grid(True, linestyle="--", linewidth=0.5)
ax.set_title("2-Link Planar Arm (use sliders below)") # this is fotor write the title for the graph

# initial angles (radians)
theta1_0 = np.deg2rad(30.0)
theta2_0 = np.deg2rad(30.0)

# draw initial arm
base, joint, ee = fk(theta1_0, theta2_0) # calling the fk function to get the positions of base, joint and end-effector
 
(link_line,) = ax.plot([base[0], joint[0], ee[0]], # plotting the arm
                       [base[1], joint[1], ee[1]],
                       marker="o", linewidth=3)
ee_text = ax.text(0.02, 0.98, "", transform=ax.transAxes,
                  va="top", ha="left", fontsize=10,
                  bbox=dict(boxstyle="round", fc="w", ec="0.7"))

# --- slider axes (beneath plot) ---
slider_ax1 = plt.axes([0.15, 0.05, 0.7, 0.03]) #slider for theta1
slider_ax2 = plt.axes([0.15, 0.01, 0.7, 0.03]) #slider for theta2

s_theta1 = Slider(slider_ax1, 'θ1 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta1_0)) #initial value of theta1
s_theta2 = Slider(slider_ax2, 'θ2 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta2_0))  #initial value of theta2

def update(_):
    th1 = np.deg2rad(s_theta1.val) # converting theta1 from degrees to radians
    th2 = np.deg2rad(s_theta2.val) # converting theta2 from degrees to radians
    b, j, e = fk(th1, th2) # calling the fk function to get the positions of base, joint and end-effector
    link_line.set_data([b[0], j[0], e[0]], [b[1], j[1], e[1]]) # updating the arm position
    ee_text.set_text(f"EE: x={e[0]:.3f}, y={e[1]:.3f}\nθ1={np.rad2deg(th1):.1f}°, θ2={np.rad2deg(th2):.1f}°")
    plt.draw()

s_theta1.on_changed(update) #
s_theta2.on_changed(update)
update(None)

plt.show() #this is to plot the graph
