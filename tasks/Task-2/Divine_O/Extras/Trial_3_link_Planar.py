
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# --- predefined link lengths (in arbitrary units) ---
L1 = 1.5
L2 = 1.2
L3 = 1.0

def fk(theta1, theta2, theta3):
    """Forward kinematics for a 2R planar arm (angles in radians)."""
    x1 = L1*np.cos(theta1)
    y1 = L1*np.sin(theta1)
    x2 = x1 + L2*np.cos(theta1 + theta2)
    y2 = y1 + L2*np.sin(theta1 + theta2)
    x3 = x2 + L3*np.cos(theta1 + theta2 + theta3)
    y3 = y2 + L3*np.sin(theta1 + theta2 + theta3)
    return (0, 0), (x1, y1), (x2, y2), (x3,y3)

# --- helper: check segment intersection ---
def ccw(A, B, C):
    """Return True if points A,B,C are arranged counter-clockwise."""
    return (C[1] - A[1])*(B[0] - A[0]) > (B[1] - A[1])*(C[0] - A[0])

def segments_intersect(A, B, C, D):
    """Return True if line segments AB and CD intersect."""
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

# --- figure and axes ---
plt.figure(figsize=(7, 7))
ax = plt.subplot(111)
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(- (L1+L2+L3+0.2), L1+L2+L3+0.2)
ax.set_ylim(- (L1+L2+L3+0.2), L1+L2+L3+0.2)
ax.grid(True, linestyle="--", linewidth=0.5)
ax.set_title("3-Link Planar Arm (use sliders below)")

# initial angles (radians)
theta1_0 = np.deg2rad(30.0)
theta2_0 = np.deg2rad(30.0)
theta3_0 = np.deg2rad(-20.0)

# draw initial arm
base, joint1, joint2, ee = fk(theta1_0, theta2_0, theta3_0)
(link_line,) = ax.plot([base[0], joint1[0], joint2[0], ee[0]],
                       [base[1], joint1[1], joint2[0], ee[1]],
                       marker="s", linewidth=3)
ee_text = ax.text(0.02, 0.98, "", transform=ax.transAxes,
                  va="top", ha="left", fontsize=10,
                  bbox=dict(boxstyle="round", fc="w", ec="0.7"))

# --- slider axes (beneath plot) ---
slider_ax1 = plt.axes([0.15, 0.05, 0.7, 0.03])
slider_ax2 = plt.axes([0.15, 0.03, 0.7, 0.03])
slider_ax3 = plt.axes([0.15, 0.01, 0.7, 0.03])

s_theta1 = Slider(slider_ax1, 'θ1 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta1_0))
s_theta2 = Slider(slider_ax2, 'θ2 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta2_0))
s_theta3 = Slider(slider_ax3, 'θ3 (deg)', -90.0, 180.0, valinit=np.rad2deg(theta3_0))

def update(_):
    th1 = np.deg2rad(s_theta1.val)
    th2 = np.deg2rad(s_theta2.val)
    th3 = np.deg2rad(s_theta3.val)
    b, j1, j2, e = fk(th1, th2, th3)
        # --- check self-collision (link1 vs link3) ---
    collision = segments_intersect(b, j1, j2, e)
    link_line.set_color("red" if collision else "blue")
    
    link_line.set_data([b[0], j1[0], j2[0], e[0]], [b[1], j1[1], j2[1], e[1]])
    # --- display info ---
    msg = (
        f"EE: x={e[0]:.3f}, y={e[1]:.3f}\n"
        f"θ1={np.rad2deg(th1):.1f}°, θ2={np.rad2deg(th2):.1f}°, θ3={np.rad2deg(th3):.1f}°"
    )

    if collision:
        ee_text.set_text(msg + "\n⚠️ Self-collision detected!")
        ee_text.set_color("red")  # make the text red during collision
    else:
        ee_text.set_text(msg)
        ee_text.set_color("blue")  # restore to blue when safe
    plt.draw()

s_theta1.on_changed(update)
s_theta2.on_changed(update)
s_theta3.on_changed(update)
update(None)

plt.show()
