# Vectorized operations for multiple configurations
def batch_forward_kinematics(theta_array):
    """Process 1000s of configurations simultaneously!"""
    # Use NumPy broadcasting for speed
    # Perfect for workspace analysis
