
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# --- predefined link lengths (in arbitrary units) ---
L1 = 1.5  # link length 1
L2 = 1.0  # link length 2
L3 = 1.5  # link length 3
L4 = 1.0  # link length 4

def fk(theta1, theta2, theta3, theta4):   #defining a function which is for calculating forward kinematics
    """Forward kinematics for a 4R planar arm (angles in radians)."""
    x1 = L1*np.cos(theta1)  # x-coordinate of joint 1
    y1 = L1*np.sin(theta1)  # y-coordinate of joint 1

    x2 = x1 + L2*np.cos(theta1 + theta2) # x-coordinate of end-effector
    y2 = y1 + L2*np.sin(theta1 + theta2) # y-coordinate of end-effector

    x3 = x2 + L3*np.cos(theta1 + theta2 + theta3) # x-coordinate of end-effector
    y3 = y2 + L3*np.sin(theta1 + theta2 + theta3) # y-coordinate of end-effector

    x4 = x3 + L4*np.cos(theta1 + theta2 + theta3 + theta4) # x-coordinate of end-effector
    y4 = y3 + L4*np.sin(theta1 + theta2 + theta3 + theta4) # y-coordinate of end-effector
    return (0, 0), (x1, y1), (x2, y2), (x3, y3), (x4, y4)

# --- figure and axes ---
plt.figure(figsize=(7, 7)) 
ax = plt.subplot(111)
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(- (L1+L2+L3+0.2), L1+L2+L3+0.2)
ax.set_ylim(- (L1+L2+L3+0.2), L1+L2+L3+0.2)
ax.grid(True, linestyle="--", linewidth=0.5)
ax.set_title("4-Link Planar Arm (use sliders below)")

# initial angles (radians)
theta1_0 = np.deg2rad(30.0)
theta2_0 = np.deg2rad(30.0)
theta3_0 = np.deg2rad(30.0)
theta4_0 = np.deg2rad(30.0)

# draw initial arm
base, j1, j2,j3, ee = fk(theta1_0, theta2_0, theta3_0,theta4_0) # calling the fk function to get the positions of base, joint and end-effector

(link_line,) = ax.plot([base[0], j1[0], j2[0],j3[0], ee[0]], # plotting the arm
                       [base[1], j1[1], j2[1],j3[1], ee[1]],
                       marker="o", linewidth=3)
ee_text = ax.text(0.02, 0.98, "", transform=ax.transAxes,
                  va="top", ha="left", fontsize=10,
                  bbox=dict(boxstyle="round", fc="w", ec="0.7"))

# --- slider axes (beneath plot) ---
slider_ax1 = plt.axes([0.15, 0.01, 0.7, 0.03]) #slider for theta1
slider_ax2 = plt.axes([0.15, 0.06, 0.7, 0.03]) #slider for theta2
slider_ax3 = plt.axes([0.15, 0.11, 0.7, 0.03]) #slider for theta3
slider_ax4 = plt.axes([0.15, 0.16, 0.7, 0.03]) #slider for theta4

s_theta1 = Slider(slider_ax1, 'θ1 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta1_0)) #initial value of theta1
s_theta2 = Slider(slider_ax2, 'θ2 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta2_0))  #initial value of theta2
s_theta3 = Slider(slider_ax3, 'θ3 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta3_0))  #initial value of theta3
s_theta4 = Slider(slider_ax4, 'θ4 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta4_0))  #initial value of theta4

def update(_):
    th1 = np.deg2rad(s_theta1.val) # converting theta1 from degrees to radians
    th2 = np.deg2rad(s_theta2.val) # converting theta2 from degrees to radians
    th3 = np.deg2rad(s_theta3.val) # converting theta3 from degrees to radians
    th4 = np.deg2rad(s_theta4.val) # converting theta4 from degrees to radians
    b, j1, j2, j3, e = fk(th1, th2, th3, th4) # calling the fk function to get the positions of base, joint and end-effector

    link_line.set_data([b[0], j1[0], j2[0], j3[0], e[0]], [b[1], j1[1], j2[1], j3[1], e[1]]) # updating the arm position
    ee_text.set_text(f"EE: x={e[0]:.3f}, y={e[1]:.3f} \nθ1={np.rad2deg(th1):.1f}°, θ2={np.rad2deg(th2):.1f}° θ3={np.rad2deg(th3):.1f}° θ4={np.rad2deg(th4):.1f}°") # updating the end-effector text
    plt.draw()

s_theta1.on_changed(update)
s_theta2.on_changed(update)
s_theta3.on_changed(update)
s_theta4.on_changed(update)
update(None)

plt.show()
