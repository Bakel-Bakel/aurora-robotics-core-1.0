def inverse_kinematics(target_x, target_y):
    """
    My ambitious goal: Given (x,y), find the joint angles!
    This is the HARD problem in robotics.
    """
    # Method 1: Geometric approach (analytical solution)
    d = np.sqrt(target_x**2 + target_y**2)
    
    if d > L1 + L2 or d < abs(L1 - L2):
        return None  # Target unreachable!
    
    # Law of cosines magic
    cos_theta2 = (d**2 - L1**2 - L2**2) / (2 * L1 * L2)
    theta2 = np.arccos(np.clip(cos_theta2, -1, 1))
    
    # Two solutions: elbow up/down
    theta2_solutions = [theta2, -theta2]
    
    solutions = []
    for th2 in theta2_solutions:
        k1 = L1 + L2 * np.cos(th2)
        k2 = L2 * np.sin(th2)
        theta1 = np.arctan2(target_y, target_x) - np.arctan2(k2, k1)
        solutions.append((theta1, th2))
    
    return solutions
