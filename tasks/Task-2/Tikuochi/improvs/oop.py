class PlanarArm:
    def __init__(self, link_lengths):
        self.links = link_lengths
        self.joint_angles = [0] * len(link_lengths)
    
    def forward_kinematics(self):
        # Clean, reusable implementation
        pass
    
    def inverse_kinematics(self, target):
        # Multiple solution handling
        pass
    
    def plot_arm(self):
        # Integrated visualization
        pass
