# Import numpy library with alias 'np' - provides mathematical functions including trigonometry
# NumPy is essential for robotics calculations as it handles arrays efficiently and provides
# vectorized operations for cos/sin calculations needed in forward kinematics
import numpy as np

# Import matplotlib.pyplot with alias 'plt' - the main plotting interface for creating figures
# pyplot provides a MATLAB-like interface for creating interactive plots and animations
import matplotlib.pyplot as plt

# Import Slider widget from matplotlib.widgets - enables interactive GUI controls
# Slider widgets allow real-time parameter adjustment without restarting the program
from matplotlib.widgets import Slider

# Define link lengths as global constants (in arbitrary units)
# L1: Length of the first link (shoulder to elbow) - made longer for realistic proportions
L1 = 1.5
# L2: Length of the second link (elbow to end-effector) - shorter for typical arm geometry
# These fixed lengths define the robot's workspace (reachable area)
L2 = 1.0

def fk(theta1, theta2):
    """
    Forward kinematics function for a 2R (2-Revolute) planar robotic arm.
    
    This function calculates the Cartesian positions of all joints given joint angles.
    Forward kinematics answers: "Given joint angles, where is the end-effector?"
    
    Args:
        theta1: First joint angle in radians (base rotation)
        theta2: Second joint angle in radians (relative to first link)
    
    Returns:
        Tuple of three (x,y) coordinates: base, joint, end-effector
    """
    # Calculate first joint position using basic trigonometry
    # The first link rotates around the origin (0,0) by angle theta1
    x1 = L1*np.cos(theta1)  # Horizontal component of first joint
    y1 = L1*np.sin(theta1)  # Vertical component of first joint
    
    # Calculate end-effector position using compound angle transformation
    # theta1 + theta2 represents the absolute angle of the second link
    # The second link starts at (x1,y1) and extends by length L2
    x2 = x1 + L2*np.cos(theta1 + theta2)  # End-effector x-coordinate
    y2 = y1 + L2*np.sin(theta1 + theta2)  # End-effector y-coordinate
    
    # Return all three key points: base (origin), first joint, end-effector
    # This allows drawing the complete arm configuration
    return (0, 0), (x1, y1), (x2, y2)

# Create matplotlib figure with square aspect ratio for proper arm visualization
# 7x7 inches provides good resolution while maintaining proportional display
plt.figure(figsize=(7, 7))

# Create subplot - using 111 means 1 row, 1 column, first (and only) subplot
ax = plt.subplot(111)

# Set equal aspect ratio so circles appear circular and lengths are proportional
# "adjustable='box'" maintains aspect ratio by adjusting the plot box size
ax.set_aspect("equal", adjustable="box")

# Set plot limits based on maximum possible reach of the arm
# Maximum reach = L1 + L2, add 0.2 buffer for visual clarity
# Symmetric limits center the workspace in the display
ax.set_xlim(-(L1+L2+0.2), L1+L2+0.2)
ax.set_ylim(-(L1+L2+0.2), L1+L2+0.2)

# Add grid with dashed lines for easier position reading
# linewidth=0.5 makes grid subtle so it doesn't dominate the visualization
ax.grid(True, linestyle="--", linewidth=0.5)

# Add descriptive title explaining the interactive nature
ax.set_title("2-Link Planar Arm (use sliders below)")

# Define initial joint angles in radians for startup configuration
# 30 degrees converted to radians - a reasonable "bent elbow" starting pose
# Using deg2rad ensures consistency since trigonometric functions expect radians
theta1_0 = np.deg2rad(30.0)  # Initial base angle
theta2_0 = np.deg2rad(30.0)  # Initial elbow angle

# Calculate initial arm configuration using forward kinematics
base, joint, ee = fk(theta1_0, theta2_0)

# Draw the initial arm as a connected line plot with circular markers
# The comma after link_line creates a tuple - matplotlib plot() returns a list
# This unpacking gets the Line2D object for later updates
(link_line,) = ax.plot([base[0], joint[0], ee[0]],    # x-coordinates of all points
                       [base[1], joint[1], ee[1]],    # y-coordinates of all points
                       marker="o",                     # Circular markers at joints
                       linewidth=3)                   # Thick line for visibility

# Create text display for end-effector coordinates and joint angles
# Position at (2%, 98%) of axes in normalized coordinates (top-left corner)
# transform=ax.transAxes uses axes coordinates instead of data coordinates
ee_text = ax.text(0.02, 0.98, "",                    # Initial empty text
                  transform=ax.transAxes,             # Use axes coordinate system
                  va="top",                           # Vertical alignment: top
                  ha="left",                          # Horizontal alignment: left
                  fontsize=10,                        # Readable font size
                  bbox=dict(boxstyle="round",         # Rounded corner box
                           fc="w",                     # White face color
                           ec="0.7"))                  # Light gray edge color

# Create slider axes positioned below the main plot
# Format: [left, bottom, width, height] in figure coordinates (0 to 1)
# 0.15 left margin, 0.7 width leaves space for labels on both sides
slider_ax1 = plt.axes([0.15, 0.05, 0.7, 0.03])      # First slider position
slider_ax2 = plt.axes([0.15, 0.01, 0.7, 0.03])      # Second slider position (lower)

# Create interactive sliders for joint angle control
# Range: -180 to +180 degrees covers full rotation capability
# valinit sets initial slider position to match the initial arm configuration
s_theta1 = Slider(slider_ax1,                        # Slider's axes object
                  'θ1 (deg)',                        # Display label with Greek theta
                  -180.0, 180.0,                     # Min and max values in degrees
                  valinit=np.rad2deg(theta1_0))      # Initial value (convert to degrees)

s_theta2 = Slider(slider_ax2,                        # Second slider axes
                  'θ2 (deg)',                        # Display label
                  -180.0, 180.0,                     # Same range for symmetry
                  valinit=np.rad2deg(theta2_0))      # Initial value in degrees

def update(_):
    """
    Callback function triggered when slider values change.
    
    The underscore parameter represents the slider event (unused here).
    This function recalculates arm position and updates the visualization.
    """
    # Get current slider values and convert from degrees to radians
    # Trigonometric functions in numpy require radian inputs
    th1 = np.deg2rad(s_theta1.val)  # Convert slider 1 value to radians
    th2 = np.deg2rad(s_theta2.val)  # Convert slider 2 value to radians
    
    # Recalculate arm configuration with new angles
    b, j, e = fk(th1, th2)  # b=base, j=joint, e=end-effector
    
    # Update the line plot with new coordinates
    # set_data() efficiently updates existing plot without redrawing everything
    link_line.set_data([b[0], j[0], e[0]],           # New x-coordinates
                       [b[1], j[1], e[1]])           # New y-coordinates
    
    # Update the information text with current values
    # f-string formatting provides clean numerical display with controlled precision
    ee_text.set_text(f"EE: x={e[0]:.3f}, y={e[1]:.3f}\n"  # End-effector position (3 decimals)
                     f"θ1={np.rad2deg(th1):.1f}°, "        # Joint 1 angle (1 decimal)
                     f"θ2={np.rad2deg(th2):.1f}°")         # Joint 2 angle (1 decimal)
    
    # Trigger plot redraw to display changes
    # plt.draw() is more efficient than plt.show() for updates
    plt.draw()

# Register the update function as callback for slider changes
# on_changed() connects slider movement events to the update function
s_theta1.on_changed(update)  # Link first slider to update function
s_theta2.on_changed(update)  # Link second slider to update function

# Call update once to initialize the display with current slider values
# Passing None as parameter since the function doesn't use the event argument
update(None)

# Display the interactive plot window
# This starts the matplotlib event loop, enabling slider interaction
plt.show()