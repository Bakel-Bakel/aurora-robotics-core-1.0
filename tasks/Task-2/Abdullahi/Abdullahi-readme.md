# 2-Links 2-Dimensional Forward Kinematics Robotics Arm Project
This project uses Matplotlib and a custom kinematics Python function to visualize how a robotic arm moves based on changes in angle values. Two sliders allow you to adjust one joint at a time (for θ1 and θ2, controlling the x-axis and y-axis, respectively).
The forward kinematics function uses basic trigonometry to calculate the X and Y positions. The arm has two links connected by two joints. This is a simple interactive tool to demonstrate and explain the proof of concept of how a robotic arm can be simulated.

## Features
- Interactive Sliders: Control the angle at joint 1 and joint 2 of links 1 and 2, respectively.
- Real-Time Simulation: The 2D planar robotic arm updates its links and end-effector position as the sliders are moved, using forward kinematics.
- Clear Visualization: Simulates the positions a robotic arm of fixed link lengths would reach at each joint angle.

## Get Started with the Script
### 1. Requirements
Install the following Python libraries (ensure you have a Python version installed already or visit [python.ord](https://www.python.org/downloads/) to download the latest version of Python):
```bash
pip install numpy matplotlib
```
### 2. Clone the repository
Clone the project repository
```bash
git clone git@github.com:Bakel-Bakel/aurora-robotics-core-1.0.git
```

### 3. Run the Script
Navigate to:
```bash
aurora-robotics-core-1.0/codes/kinematics/forward-kinematics/py/2-links_2d.py
```
and run it, or run directly in VSCode:
```
python "C:\Users\{user_name}\{other_directory_path_if_any}\aurora-robotics-core-1.0\codes\kinematics\forward-kinematics\py\2-links_2d.py"
```

A window will open showing the robotic arm. Use the sliders at the bottom to adjust θ1 and θ2. The arm will move, and the end-effector coordinates will update in the top-left corner in real time.

## Knowledge Gained
- Basics of forward kinematics for a 2-link 2D robotic arm.
- How to use Matplotlib widgets (Slider) for interactive visualization.
