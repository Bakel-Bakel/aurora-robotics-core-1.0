# Task - add a third link

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D

L1 = 1.5
L2 = 1.0
L3 = 0.5

def Rz(t): 
    c, s = np.cos(t), np.sin(t)
    return np.array([[c,-s,0],
                     [s, c,0],
                     [0, 0,1]])

def Ry(t):
    c, s = np.cos(t), np.sin(t)
    return np.array([[ c,0,s],
                     [ 0,1,0],
                     [-s,0,c]])

def fk_3d(q_yaw, q_sh, q_el,q_wr):
    """Return 3D points (base, joint1, joint2, ee) for a 3-link arm with
       base-yaw (about z), then shoulder pitch (about y), then elbow pitch (about y), then wrist pitch (about y)."""
    R0 = Rz(q_yaw) 
    R1 = R0 @ Ry(q_sh) 
    R2 = R1 @ Ry(q_el)
    p0 = np.zeros(3)
    p1 = R1 @ np.array([L1, 0, 0])
    p2 = p1 + (R1 @ Ry(q_el)) @ np.array([L2, 0, 0])
    p3 = p2 + (R2 @ Ry(q_wr)) @ np.array([L3, 0, 0])
    return p0, p1, p2, p3

fig = plt.figure(figsize=(7,7))
ax = fig.add_axes([0.15, 0.15, 0.7, 0.75], projection='3d')
ax.set_title("3D 3-Link Arm (yaw, shoulder, elbow, wrist)")
ax.set_box_aspect((1,1,1))
lim = L1 + L2 + L3 + 0.3
ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-lim, lim)
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')

yaw0, sh0, el0, wr0 = 30.0, 20.0, 40.0, 10.0
yaw = np.deg2rad(yaw0); sh = np.deg2rad(sh0); el = np.deg2rad(el0); wr = np.deg2rad(wr0)

b, j1, j2, e = fk_3d(yaw, sh, el, wr)
(line,) = ax.plot([b[0], j1[0], j2[0], e[0]],
                  [b[1], j1[1], j2[0], e[1]],
                  [b[2], j1[2], j2[0], e[2]],
                  marker='o', linewidth=3)
txt = ax.text2D(0.02, 0.98, "", transform=ax.transAxes, va="top")

ax_yaw = plt.axes([0.15, 0.09, 0.7, 0.02]) 
ax_sh  = plt.axes([0.15, 0.06, 0.7, 0.02])
ax_el  = plt.axes([0.15, 0.03, 0.7, 0.02])
ax_wr  = plt.axes([0.15, 0.00, 0.7, 0.02])

s_yaw = Slider(ax_yaw, 'yaw (°)', -180, 180, valinit=yaw0)
s_sh  = Slider(ax_sh,  'shoulder (°)', -179, 179, valinit=sh0)
s_el  = Slider(ax_el,  'elbow (°)',   -179, 179, valinit=el0)
s_wr  = Slider(ax_wr,  'wrist (°)',   -179, 179, valinit=wr0)

def update(_): 
    q0 = np.deg2rad(s_yaw.val)
    q1 = np.deg2rad(s_sh.val)
    q2 = np.deg2rad(s_el.val)
    q3 = np.deg2rad(s_wr.val)
    b, j1, j2, e = fk_3d(q0, q1, q2, q3)
    line.set_data_3d([b[0], j1[0], j2[0], e[0]],
                     [b[1], j1[1], j2[0], e[1]],
                     [b[2], j1[2], j2[0], e[2]])
    txt.set_text(f"EE: x={e[0]:.3f}, y={e[1]:.3f}, z={e[2]:.3f}\n"
                 f"yaw={s_yaw.val:.1f}°, sh={s_sh.val:.1f}°, el={s_el.val:.1f}°, wr={s_wr.val:.1f}°")
    fig.canvas.draw_idle()

for s in (s_yaw, s_sh, s_el, s_wr):
    s.on_changed(update)
update(None)
plt.show()
