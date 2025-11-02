# Forward Kinematics with python
Kinematics can be represented using forward and Inverse Kinematics 

## Inverse Kinematics
Here the position of the robot's end effector is already known(its target position and orientation in space) and then the joint angles and displacement from the base is then calulated.

## Forward Kinematics 
Here the posititon and orientation of the end effector in space is calculated using the angles and positions of its joints.


To visualize this phenomenon we can use python.

## 🚀 Steps  


1. **Install Python**  
   - Download and install Python from [python.org](https://www.python.org/downloads/).  

2. **Install VS Code**  
   - Download from [Visual Studio Code](https://code.visualstudio.com/).  

3. **Install python extensions**
    - Download python, Python Nevironments and python Debugger (by Microsoft)

4. **Install python packages**
    - To download packages you need pip; 
    Run this in the terminal
    ```bash
    python - pip install --upgrade pip
    ```

5. **Install visualization/mathematical packages**
    - Run 
    ```bash
    pip install numpy
    pip install matplotlib
    ```

Numpy here is used to do mathematical computation like scientific manipulations; used to calculate the angle and position of the links and joints.

Matplotlib here is used to visualize the image in plot form 