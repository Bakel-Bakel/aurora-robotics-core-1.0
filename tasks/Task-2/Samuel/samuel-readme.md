### 2 Links 2-D Robot Arm

## Terminologies:
- Link: think of it as an arm, but for a robot
- Joint: this connects links together
- End effector: this is the tool attached to the end of the robot arm. You want your robot arm to do something right, like draw, paint, weld...So the end effector can have any of those tools attached.


## What is Kinematics
Kinematics is a field of Engineering that is concerned with describing the motion of objects without considering the forces acting on it. If that is complex, think of it this way: you have a robot arm, and you want to understand what happens to part A of the arm if you move part B, the branch dedicated to this is Kinematics.(Note this is a simple explanantion).

Kinematics is quite important in Robotics, and it is usually the entry point for many robotics enthusiast, as it is an easy way to appreciate mathematics, and see how it serves as the foundation for building and controlling robot arms for example.

There are mainly two types of kinematics. Think of them as types of problems that kinematics solves as well, we have:
1. Forward Kinematics(FK): say you have a robot arm, you then ask the question - If I change the angles between the links, where do I end up. This question is what FK attempts to solve.
2. Inverse Kinematics: This one answers the question: There is a position I wish to get to, to what degree do I need to move the links to get to that position. Here you are controlling the joint angles because the link length is fixed.

# Project File details
This project is a simple 2 links 2 dimensional robot arm, and the tip of the arm is assumed to be the end effector.
It makes use of:
- Python: Programming language
- Numpy: Popular library for numerical computuation, some operations are faster than the regular python-default methods.
- Matplotlib: The most popular python library for graphs and plots, very easy to use as well.


