# Forward Kinematics 

Forward Kinematics is the process of determining the position and the orientaton of the end-effector(the "hand" or tip) of a robotics given the joint angles. In 2D, we're working in a plane with links that rotate about joints. Basically we're tryung to figure out where the hand will be at a particular combination of the rotating joints.

## Basic Terminology

1. <ins>Link</ins>: A rigid body(like a rod or a segment of an arm) that connects joints
2. <ins>Joint</ins>: A point of rotation or translation that connects two links
3. <ins>Degrees of Freedom(DOF)</ins>: The number of independent parameters(angles or displacements) needed to fully describe the robot's configuration.
4. <ins>End-Effector</ins>: The "tip" or "hand" of the robot that interacts with the environment.

## For a Two-Link Planar Robot Arm:

The  position of the end-effector (X,Y) can be determined using forward kinematics, which relates the joint angles(theta_1,theta_2) and link lengths (L1,L2) to the end-effector's position.

The first link, with length L1, is rotated by an angle theta_1 with respect to the x-axis. The coordinates of the first joint are given by:
            ```

            x1 = L1 cos(theta_1)
            y1 = L1 sin(theta_1)
            ```


The second link, with length L2, is rotated by an angle of (theta_1 + theta_2) with respect to the x-axis. The coordinates are:
            ```

            x2 = L2 cos(theta_1 + theta_2)
            y2 = L2 sin(theta_1 + theta_2)
            ```


Therefore the equations or the positon for the end-effector are:
    ```

    X = x1 + x2 = L1 cos(theta_1) + L2 cos(theta_1 + theta_2)
    Y = y1 + y2 = L1 sin(theta_1) + L2 sin(theta_1 + theta_2)
    ```
