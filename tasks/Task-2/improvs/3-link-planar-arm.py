def fk_3link(theta1, theta2, theta3):
    """My next challenge: 3-DOF arm with redundancy!"""
    # Base to Joint 1
    x1 = L1 * np.cos(theta1)
    y1 = L1 * np.sin(theta1)
    
    # Joint 1 to Joint 2  
    x2 = x1 + L2 * np.cos(theta1 + theta2)
    y2 = y1 + L2 * np.sin(theta1 + theta2)
    
    # Joint 2 to End-Effector
    x3 = x2 + L3 * np.cos(theta1 + theta2 + theta3)
    y3 = y2 + L3 * np.sin(theta1 + theta2 + theta3)
    
    return [(0,0), (x1,y1), (x2,y2), (x3,y3)]
