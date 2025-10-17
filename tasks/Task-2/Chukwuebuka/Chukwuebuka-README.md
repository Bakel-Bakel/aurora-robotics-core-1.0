This is a 2D-Link robotic arm. This covers some of the basic related to 2 dimensional analysis of a robotic arm. Basic knowledge of trigonomentry(Mathematics) or resolution of forces(Vector mechanics) are needed to know what the arm is actually doing

For the understanding of the code, the knowledge of the programming language, python is needed which include the basics like imports, function, variable declaration and assignment, Tupple, lists.

The robtic arm uses a method known as Inverse Kinematic to move around but for this case it uses Forward Kinematic, since the the former is quite complicated to resolve. 
The Forward Kinematic is not the normal control method of a robotic arm, as previously mentioned but it gives a more easy way for the beginners to understand the world of robotic

Difference between Inverse and Forward Kinematic
Inverse Kinematics- Given the position of an end effector, in the x and y (2D) axis the angles of the joints needed for the end effector to get to that position is calculated

Forward Kinematic- Given the angles of the joint, the position in the x, y axis (2D) of the end effector can be calculated.

From the definition alone, you can tell how IK will be the hideous task. That of the Fk will be a bit more easy to achieve.

Note: From the lesson, we used only 2 links, which has 1 joint and a base. The links are not limited to this alone and can be up to 20 and th process of solving remain same. We can also relate the robotic arm to a human hand.

Base - Shoulder
Link 1 - Upper arm
Joint - Elbow
Link 2 - Fore arm
End Effector - Hand

