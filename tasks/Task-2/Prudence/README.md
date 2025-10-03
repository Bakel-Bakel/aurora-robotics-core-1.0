# 2-Link Planar Arm Visualization

This Python script visualizes the forward kinematics of a 2-link planar robotic arm. You can interactively adjust the joint angles using sliders and observe the resulting position of the end effector.

## Features

- **Interactive Sliders:** Change the angles of both joints (θ1 and θ2) in degrees.
- **Real-Time Visualization:** The arm updates instantly as you move the sliders.
- **End Effector Display:** Shows the current (x, y) position of the end effector and the joint angles.

## Requirements

- Python 3.x
- `numpy`
- `matplotlib`

Install dependencies with:

```
pip install numpy matplotlib
```

## Usage

Run the script from the terminal:

```
python prudence_2-links_2d.py
```

A window will appear showing the arm and sliders. Adjust the sliders to change the arm configuration.

## How It Works

- The arm consists of two links of lengths `L1` and `L2`.
- The `fk` function computes the positions of the base, joint, and end effector using forward kinematics.
- The plot updates dynamically as you change the joint angles.

## File Structure

- `prudence_2-links_2d.py`: Main script for visualization.

## Example
![Screenshot of 2-Link Planar Arm Visualization](images/screenshot.png)

## Author

the-HTML-programmer