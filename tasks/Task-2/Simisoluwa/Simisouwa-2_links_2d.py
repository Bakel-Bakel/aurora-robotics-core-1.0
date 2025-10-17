# two_link_click_ik.py
import numpy as np                      # Import NumPy for math and array operations
import matplotlib.pyplot as plt         # Import Matplotlib for plotting and interactivity

# ----- link lengths (units) -----
L1 = 1.5                                # Length of the first arm link
L2 = 1.0                                # Length of the second arm link
R  = L1 + L2                            # Maximum reach of the arm (used for plot limits)

def ik_2r(x, y, L1=L1, L2=L2):
    """Return list of (theta1, theta2) in radians for target (x, y)."""
    r2 = x*x + y*y                      # Compute squared distance from base to target

    # ---- Reachability check ----
    # If target is beyond the arm’s max reach or too close to the base, it's unreachable.
    if r2 > (L1 + L2)**2 + 1e-9 or r2 < (L1 - L2)**2 - 1e-9:
        return []

    # ---- Compute the cosine of theta2 using the law of cosines ----
    c2 = (r2 - L1*L1 - L2*L2) / (2.0 * L1 * L2)
    c2 = np.clip(c2, -1.0, 1.0)         # Numerical safety (avoid domain error in sqrt)

    # Two possible solutions for sin(theta2): elbow-down (positive) and elbow-up (negative)
    s2_pos = np.sqrt(1.0 - c2*c2)       # Elbow-down configuration
    s2_neg = -s2_pos                    # Elbow-up configuration

    # Compute theta2 angles using atan2 for both configurations
    t2a = np.arctan2(s2_pos, c2)
    t2b = np.arctan2(s2_neg, c2)

    # ---- Nested helper function to compute theta1 given a theta2 ----
    def t1_for(t2):
        k1 = L1 + L2*np.cos(t2)         # x-component of wrist position when theta2 is known
        k2 = L2*np.sin(t2)              # y-component contribution from second link
        return np.arctan2(y, x) - np.arctan2(k2, k1)  # Compute theta1 using atan2 geometry

    # Return both possible (theta1, theta2) pairs
    return [(t1_for(t2a), t2a), (t1_for(t2b), t2b)]

def fk_2r(t1, t2, L1=L1, L2=L2):
    """Forward kinematics: returns joint coordinates for given angles."""
    x1 = L1*np.cos(t1); y1 = L1*np.sin(t1)                 # Position of the first joint
    x2 = x1 + L2*np.cos(t1 + t2)                           # End-effector x-position
    y2 = y1 + L2*np.sin(t1 + t2)                           # End-effector y-position
    return (0,0), (x1,y1), (x2,y2)                         # Base, joint, and end-effector

# ---- Setup figure and axes ----
fig, ax = plt.subplots(figsize=(7,7))                      # Create a square figure
ax.set_aspect("equal", adjustable="box")                   # Equal scaling for x and y
ax.set_xlim(-R-0.2, R+0.2); ax.set_ylim(-R-0.2, R+0.2)     # Set visible range with margin
ax.grid(True, linestyle="--", linewidth=0.5)                # Light dashed grid
ax.set_title("2-Link IK (Click Anywhere)")                 # Plot title

# ---- Draw reachability circles ----
circ = plt.Circle((0,0), R, color="0.85", fill=False, linestyle=":")      # Max reach
ax.add_patch(circ)
inner = plt.Circle((0,0), abs(L1-L2), color="0.85", fill=False, linestyle=":") # Min reach
ax.add_patch(inner)

# ---- Create line artists for the two arm configurations ----
(line_a,) = ax.plot([], [], marker="o", linewidth=4, label="Elbow-Down", color="#A861CC")  # Elbow-down arm
(line_b,) = ax.plot([], [], marker="o", linewidth=4, label="Elbow-Up", color="#84B3D7")    # Elbow-up arm
target_dot, = ax.plot([], [], "rx", markersize=10, mew=2)                 # Red "X" for target

# ---- Display text box for angles ----
txt = ax.text(
    0.02, 0.98, "", transform=ax.transAxes, va="top",
    bbox=dict(boxstyle="round", fc="w", ec="0.7")         # Small white box with rounded corners
)
ax.legend(loc="lower right")                              # Add legend for clarity

# ---- Event handler: runs when user clicks inside the plot ----
def on_click(event):
    if not event.inaxes:                                  # Ignore clicks outside the plot area
        return
    x, y = event.xdata, event.ydata                       # Get clicked coordinates

    target_dot.set_data([x], [y])                         # Update red target position
    sols = ik_2r(x, y)                                    # Compute IK solutions

    if not sols:                                          # If no valid solution found:
        line_a.set_data([], []); line_b.set_data([], [])   # Clear arm drawings
        txt.set_text(f"Target: ({x:.3f}, {y:.3f})\nUnreachable.")  # Display warning
        fig.canvas.draw_idle()
        return

    # ---- Compute and draw both arm configurations ----
    (t1a, t2a), (t1b, t2b) = sols                         # Unpack solutions

    # Elbow-down
    b, j, e = fk_2r(t1a, t2a)
    line_a.set_data([b[0], j[0], e[0]], [b[1], j[1], e[1]])

    # Elbow-up
    b, j, e = fk_2r(t1b, t2b)
    line_b.set_data([b[0], j[0], e[0]], [b[1], j[1], e[1]])

    # Display joint angles in degrees for both solutions
    txt.set_text(
        f"Target: ({x:.3f}, {y:.3f})\n"
        f"Elbow-Down: θ1={np.degrees(t1a):.1f}°, θ2={np.degrees(t2a):.1f}°\n"
        f"Elbow-Up  : θ1={np.degrees(t1b):.1f}°, θ2={np.degrees(t2b):.1f}°"
    )

    fig.canvas.draw_idle()                                # Refresh the plot display

# ---- Connect click event to handler ----
fig.canvas.mpl_connect("button_press_event", on_click)

# ---- Show the interactive plot ----
plt.show()
