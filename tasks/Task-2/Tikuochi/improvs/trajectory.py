def plan_trajectory(start_pos, end_pos, steps=50):
    """Plan smooth paths between two points in workspace"""
    # Interpolate in Cartesian space
    # Convert back to joint space
    # Ensure smooth joint motions (no sudden jumps!)
