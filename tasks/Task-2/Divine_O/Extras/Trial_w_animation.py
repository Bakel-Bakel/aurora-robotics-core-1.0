import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Link lengths
L1 = 1.0
L2 = 0.8

def fk(theta1, theta2):
    """Forward kinematics for a 2R planar arm."""
    x1 = L1 * np.cos(theta1)
    y1 = L1 * np.sin(theta1)
    x2 = x1 + L2 * np.cos(theta1 + theta2)
    y2 = y1 + L2 * np.sin(theta1 + theta2)
    return (0, 0), (x1, y1), (x2, y2)

# --- figure and axes setup ---
fig = plt.figure(figsize=(10, 5))

# Create two subplots: (1 row, 2 columns)
ax1 = plt.subplot(1, 2, 1)  # Left: Robot arm visualization
ax2 = plt.subplot(1, 2, 2)  # Right: End-effector trajectory

# Left subplot: Robot arm
ax1.set_aspect("equal", adjustable="box")
ax1.set_xlim(- (L1+L2+0.2), L1+L2+0.2)
ax1.set_ylim(- (L1+L2+0.2), L1+L2+0.2)
ax1.grid(True, linestyle="--", linewidth=0.5)
ax1.set_title("2-Link Planar Arm")

# Right subplot: End-effector trajectory
ax2.set_aspect("equal", adjustable="box")
ax2.set_xlim(- (L1+L2+0.2), L1+L2+0.2)
ax2.set_ylim(- (L1+L2+0.2), L1+L2+0.2)
ax2.grid(True, linestyle="--", linewidth=0.5)
ax2.set_title("End-Effector Path")

# Line for the robot arm (2 links + joints)
arm_line, = ax1.plot([], [], 'o-', linewidth=3, markersize=8, color='blue')

# Line for the trajectory (just a path of points)
traj_line, = ax2.plot([], [], 'r-', linewidth=2)

# Empty lists to store trajectory points
x_traj, y_traj = [], []

def init():
    arm_line.set_data([], [])
    traj_line.set_data([], [])
    return arm_line, traj_line

def update(frame):
    theta1 = np.radians(frame)
    theta2 = np.radians(60 * np.sin(np.radians(frame)))

    # Compute forward kinematics
    (x0, y0), (x1, y1), (x2, y2) = fk(theta1, theta2)

    # Update robot arm in left plot
    arm_line.set_data([x0, x1, x2], [y0, y1, y2])

    # Update trajectory in right plot
    x_traj.append(x2)
    y_traj.append(y2)
    traj_line.set_data(x_traj, y_traj)

    return arm_line, traj_line
ani = FuncAnimation(
    fig, update,
    frames=np.arange(0, 360, 2),
    init_func=init,
    interval=50,
    blit=True
)

plt.tight_layout()
plt.show()
