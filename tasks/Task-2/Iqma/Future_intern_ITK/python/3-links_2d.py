# Task - create 3 link arm as opposed to 2d done in class
# Decided to type this myself instead of copying the original code and just editing, good luck to me

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

L1 = 1.5
L2 = 1.0
L3 = 0.5

def fk(theta1, theta2, theta3):
    x1 = L1*np.cos(theta1)
    y1 = L1*np.sin(theta1)
    x2 = x1 + L2*np.cos(theta1 + theta2)
    y2 = y1 + L2*np.sin(theta1 + theta2)
    x3 = x2 + L3*np.cos(theta1 + theta2 + theta3)
    y3 = y2 + L3*np.sin(theta1 + theta2 + theta3)
    return (0,0), (x1, y1), (x2, y2), (x3,y3)

plt.figure(figsize=(7,7))
#had to change this from subplot to this for manual editing cause it was overlapping with the sliders
ax = plt.axes([0.15, 0.15, 0.7, 0.75]) #left bottom width height. mad trial and error here mehn
ax.set_aspect('equal', adjustable="box")
ax.set_xlim(- (L1 + L2 + L3 + 0.2), L1 + L2 + L3 + 0.2)
ax.set_ylim(- (L1 + L2 + L3 + 0.2), L1 + L2 + L3 + 0.2)
ax.grid(True, linestyle="--", linewidth=0.5)
ax.set_title("3-link Planar Arm (use sliders below)")

theta1_0 = np.deg2rad(30.0)
theta2_0 = np.deg2rad(30.0)
theta3_0 = np.deg2rad(30.0)

base, joint1, joint2, ee = fk(theta1_0, theta2_0, theta3_0)
(link_line,) = ax.plot([base[0], joint1[0], joint2[0], ee[0]],
                       [base[1], joint1[1], joint2[1], ee[1]],
                        marker='o', linewidth=3)
ee_text = ax.text(0.02, 0.98, "", transform=ax.transAxes,
                  va="top", ha="left", fontsize=10,
                  bbox=dict(boxstyle="round", fc="w", ec="0.7"))

slider_ax1 = plt.axes([0.15, 0.09, 0.7, 0.03]) # left , bottom, width, height
slider_ax2 = plt.axes([0.15, 0.05, 0.7, 0.03])
slider_ax3 = plt.axes([0.15, 0.01, 0.7, 0.03])

s_theta1 = Slider(slider_ax1, '01 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta1_0))
s_theta2 = Slider(slider_ax2, '02 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta2_0))
s_theta3 = Slider(slider_ax3, '03 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta3_0))

def update(_):
    th1 = np.deg2rad(s_theta1.val)
    th2 = np.deg2rad(s_theta2.val)
    th3 = np.deg2rad(s_theta3.val)
    b, j1, j2, e = fk(th1, th2, th3)
    link_line.set_data([b[0], j1[0], j2[0], e[0]], [b[1], j1[1], j2[1], e[1]])
    ee_text.set_text(f"EE: x={e[0]:.3f}, y ={e[1]:.3f}\n01={np.rad2deg(th1):.1f}°, 02={np.rad2deg(th2):.1f}°, 03={np.rad2deg(th3):.1f}°")
    plt.draw()

s_theta1.on_changed(update)
s_theta2.on_changed(update)
s_theta3.on_changed(update)
update(None)

plt.show()

# ran on the sixth try !! (forgot to add second joint variable name(x2), 
# numbering issues, then spacing issues, used wrong marker, overlapping graph and slider)