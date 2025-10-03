import numpy as np #needed to work with arrays
import matplotlib.pyplot as plt #to plot 
L1 = 1.5 #Link lenght 1
L2 = 1.0 #Link length 2
x0,y0=0,0 #origin
theta1 = np.deg2rad(30) #convert degree to rad
theta2 = np.deg2rad(30)
x1 = L1*np.cos(theta1) #x1 formula from forward kinematics
y1 = L1*np.sin(theta2) #y1 formula from inverse kinematics
x2 = x1 + L2*np.cos(theta1+theta2) #x2 formula from forward kinematics
y2 = y1 + L2*np.sin(theta1+theta2) #y2 formula from forward kinematics

plt.figure(figsize=(4,4)) #initialise figure
plt.plot([x0,x1,x2],[y0,y1,y2],'-o',linewidth=3) #plot line from origin to x,y with dot zero
plt.grid(True, linestyle="--", linewidth=0.5) #show plot grid
plt.xlim(-4,4) #set limit of x axis
plt.ylim(-4,4) #Limit of y axis
plt.title("Simple 2-Link Arm") #include title
plt.show() #visualize everything