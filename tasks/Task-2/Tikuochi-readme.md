An interactive 2-link planar robotic arm simulator as task 2 of the Aurora Robotics core workshop, teaching me the fundamentals of forward kinematics.

Forward Kinematics: Given joint angles θ₁ and θ₂, where exactly is my robot's end-effector in Cartesian space?

Joint Space (θ₁, θ₂) → Forward Kinematics → Cartesian Space (x, y)

Breakdown of Implementation:

Link 1: P₁ = (L₁·cos(θ₁), L₁·sin(θ₁))
Link 2: P₂ = P₁ + (L₂·cos(θ₁ + θ₂), L₂·sin(θ₁ + θ₂))

Architecture

End-Effector (x₂, y₂)
              ●
             /
            /L₂
           /
    Joint ●
         /
        /L₁ 
       /
Base  ●────────► X-axis
      │
      ▼
   Y-axis
What I Learned Through This Project
1. Coordinate Frame Transformations
I discovered that each link in a robotic arm has its own coordinate frame. The magic happens when you transform from one frame to the next:

The base frame is my reference point (0,0)
Each subsequent joint adds its own rotation and translation
The compound angle θ₁ + θ₂ represents the absolute orientation of the second link

2. The Power of Interactive Learning
Static plots are boring! Real-time sliders were implemented because seeing how joint angles affect end-effector position is worth a thousand equations.
3. Workspace Limitations
My robot can't reach everywhere! The workspace is an annulus (ring shape):

Inner radius: |L₁ - L₂| = 0.5 units (when arms fold inward)
Outer radius: L₁ + L₂ = 2.5 units (when arms extend outward)

Advanced Extensions I'm Planning
1. 3-Link Planar Arm - More Degrees of Freedom!
2. Inverse Kinematics Solver - The Real Challenge!
3. 3D Robotic Arm - Enter the Third Dimension!

Creative Visualizations I Want to Add
1. Workspace Visualization
2. Trajectory Planning
3. Real-Time Performance Metrics

Manipulability Index: How "good" is the current arm configuration?
Joint Velocity Limits: Are we moving joints too fast?
Singularity Detection: When does the arm lose degrees of freedom?

 Code Architecture Improvements I'm Considering
1. Object-Oriented Design
2. Performance Optimization
3. Configuration Space Analysis

Real-World Applications I'm Exploring
1. Industrial Pick-and-Place

Path planning for manufacturing robots
Obstacle avoidance algorithms
Cycle time optimization

2. Surgical Robotics

Precision requirements (sub-millimeter accuracy)
Safety constraints and workspace boundaries
Tremor filtering and motion scaling

3. Humanoid Robotics

Arm coordination with full-body balance
Dynamic motion planning
Human-robot interaction safety

Performance Benchmarks I Want to Achieve

Observations!

Compound Angles: I initially tried to track each link's absolute angle separately. Wrong! The beauty is in θ₁ + θ₂ - it naturally handles the kinematic chain.
Workspace Geometry: The reachable area isn't a circle—it's a ring! This limitation drives real robot design decisions.
Interactive Learning: Static equations in textbooks are hard to grasp. But move that slider and suddenly everything clicks!
Coordinate Frames: Every joint is a mini coordinate system. Robotics is just coordinate frame transformations all the way down!
