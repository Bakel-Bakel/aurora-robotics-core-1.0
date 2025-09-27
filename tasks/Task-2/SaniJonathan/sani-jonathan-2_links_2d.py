# two_link_click_ik.py
# ----------------------------------------------------------------------
# This program demonstrates inverse kinematics (IK) for a 2-link robotic
# planar arm using interactive clicks on a matplotlib plot.
# By clicking anywhere in the workspace, the program computes the
# possible joint angles and visualizes both "elbow-up" and "elbow-down"
# configurations of the arm.
# ----------------------------------------------------------------------

# Import numerical library NumPy - provides mathematical functions and array operations
# Essential for robotics since it handles trigonometry (cos, sin, atan2) efficiently
import numpy as np

# Import matplotlib's plotting library - for creating interactive 2D visualizations
# We'll use it to display the arm, reachable area, and respond to mouse clicks
import matplotlib.pyplot as plt

# ---------------- Arm Parameters -----------------
# Define the lengths of the two robotic arm links (arbitrary units)
# L1: Length of the first link (base to elbow)
# L2: Length of the second link (elbow to end-effector)
L1 = 1.5
L2 = 1.0

# R: Maximum reach of the arm = sum of both links
# Used for plotting the outer workspace boundary
R  = L1 + L2

# ---------------- Inverse Kinematics Function -----------------
def ik_2r(x, y, L1=L1, L2=L2):
    """
    Compute inverse kinematics (IK) for a 2-link planar robot.
    
    Given a target point (x, y), return possible joint angle solutions:
    - θ1: angle of first joint (base)
    - θ2: angle of second joint (elbow)
    
    Args:
        x, y: Cartesian coordinates of target point
        L1, L2: link lengths (defaults set above)
    
    Returns:
        List of tuples [(theta1a, theta2a), (theta1b, theta2b)]
        Each solution corresponds to elbow-up or elbow-down.
        Returns empty list if target is unreachable.
    """
    # Compute squared distance to target point
    r2 = x*x + y*y

    # Reachability check:
    # - If target is farther than (L1+L2), it’s unreachable
    # - If target is closer than |L1-L2|, it’s unreachable
    if r2 > (L1 + L2)**2 + 1e-9 or r2 < (L1 - L2)**2 - 1e-9:
        return []  # no solution

    # Compute cosine of θ2 using law of cosines
    c2 = (r2 - L1*L1 - L2*L2) / (2.0 * L1 * L2)
    # Clip c2 between -1 and 1 to avoid floating-point errors
    c2 = np.clip(c2, -1.0, 1.0)

    # Two possible values for sine(θ2): positive (elbow-down) and negative (elbow-up)
    s2_pos = np.sqrt(1.0 - c2*c2)   # positive square root
    s2_neg = -s2_pos                # negative square root

    # Compute the two possible θ2 values
    t2a = np.arctan2(s2_pos, c2)    # elbow-down
    t2b = np.arctan2(s2_neg, c2)    # elbow-up

    # Inner function to compute θ1 given θ2
    def t1_for(t2):
        # Using geometric trick with atan2 for stable computation
        k1 = L1 + L2*np.cos(t2)     # projection along x-axis
        k2 = L2*np.sin(t2)          # projection along y-axis
        return np.arctan2(y, x) - np.arctan2(k2, k1)

    # Return both possible (θ1, θ2) pairs
    return [(t1_for(t2a), t2a), (t1_for(t2b), t2b)]

# ---------------- Forward Kinematics Function -----------------
def fk_2r(t1, t2, L1=L1, L2=L2):
    """
    Forward kinematics (FK) for a 2-link planar robot.
    
    Given joint angles (t1, t2), compute the coordinates of:
    - Base (0,0)
    - Elbow joint
    - End-effector (tool tip)
    
    Args:
        t1, t2: joint angles in radians
        L1, L2: link lengths
    
    Returns:
        Tuple of 3 points: (base, joint, end-effector)
    """
    # Compute elbow coordinates using link 1
    x1 = L1*np.cos(t1)
    y1 = L1*np.sin(t1)

    # Compute end-effector coordinates using link 2
    x2 = x1 + L2*np.cos(t1 + t2)
    y2 = y1 + L2*np.sin(t1 + t2)

    return (0,0), (x1,y1), (x2,y2)

# ---------------- Plot Setup -----------------
# Create a figure and axis for interactive plotting
fig, ax = plt.subplots(figsize=(7,7))   # 7x7 inches square figure
ax.set_aspect("equal", adjustable="box")  # keep aspect ratio square

# Set limits to cover full reach + small margin
ax.set_xlim(-R-0.2, R+0.2)
ax.set_ylim(-R-0.2, R+0.2)

# Add background grid for reference
ax.grid(True, linestyle="--", linewidth=0.5)
ax.set_title("2-Link IK (click anywhere)")  # title of the window

# ---------------- Workspace Visualization -----------------
# Outer circle: maximum reach boundary
circ = plt.Circle((0,0), R, color="0.85", fill=False, linestyle=":")
ax.add_patch(circ)

# Inner circle: minimum reach boundary (when links fold back)
inner = plt.Circle((0,0), abs(L1-L2), color="0.85", fill=False, linestyle=":")
ax.add_patch(inner)

# ---------------- Arm Visualization -----------------
# Create empty line objects for two possible solutions (to be updated later)
(line_a,) = ax.plot([], [], marker="o", linewidth=4, label="elbow-down")
(line_b,) = ax.plot([], [], marker="o", linewidth=4, label="elbow-up")

# Target marker (red 'x')
target_dot, = ax.plot([], [], "rx", markersize=10, mew=2)

# Text box to display joint angles and target info
txt = ax.text(0.02, 0.98, "", transform=ax.transAxes, va="top",
              bbox=dict(boxstyle="round", fc="w", ec="0.7"))

# Add legend to distinguish elbow-up vs elbow-down solutions
ax.legend(loc="lower right")

# ---------------- Mouse Click Handler -----------------
def on_click(event):
    """
    Callback function triggered when user clicks inside the plot.
    
    Steps:
    1. Get target coordinates from click
    2. Compute inverse kinematics
    3. If unreachable → show message
    4. If reachable → update both elbow-up and elbow-down arm plots
    """
    # Ignore clicks outside the axes
    if not event.inaxes: 
        return

    # Extract target coordinates from click event
    x, y = event.xdata, event.ydata
    target_dot.set_data([x], [y])  # show red "x" at target

    # Solve inverse kinematics for clicked target
    sols = ik_2r(x, y)

    # Case 1: No solution (unreachable target)
    if not sols:
        line_a.set_data([], []); line_b.set_data([], [])
        txt.set_text(f"Target: ({x:.3f}, {y:.3f})\nUnreachable.")
        fig.canvas.draw_idle()
        return

    # Case 2: Two solutions exist (elbow-up and elbow-down)
    (t1a,t2a), (t1b,t2b) = sols

    # Compute FK and update elbow-down solution
    b, j, e = fk_2r(t1a, t2a)
    line_a.set_data([b[0], j[0], e[0]], [b[1], j[1], e[1]])

    # Compute FK and update elbow-up solution
    b, j, e = fk_2r(t1b, t2b)
    line_b.set_data([b[0], j[0], e[0]], [b[1], j[1], e[1]])

    # Update info text with angles (in degrees for readability)
    txt.set_text(
        f"Target: ({x:.3f}, {y:.3f})\n"
        f"Elbow-down: θ1={np.degrees(t1a):.1f}°, θ2={np.degrees(t2a):.1f}°\n"
        f"Elbow-up  : θ1={np.degrees(t1b):.1f}°, θ2={np.degrees(t2b):.1f}°"
    )

    # Redraw figure with updated arm positions
    fig.canvas.draw_idle()

# Connect the mouse click event to the handler function
fig.canvas.mpl_connect("button_press_event", on_click)

# ---------------- Run Interactive Plot -----------------
# Start matplotlib’s interactive event loop
# Window stays open and responds to mouse clicks
plt.show()
```
