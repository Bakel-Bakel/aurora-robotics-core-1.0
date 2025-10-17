# 3d_frames_gui.py
# Requirements: python -m pip install numpy matplotlib
# (Tkinter ships with most Python installations; on Linux you may need python3-tk)

import tkinter as tk
from tkinter import ttk
import numpy as np
from math import cos, sin, radians
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# ---------- Transform helpers ----------
def T_translate(dx, dy, dz):
    T = np.eye(4)
    T[:3, 3] = [dx, dy, dz]
    return T

def R_axis_angle(axis, theta_deg):
    t = radians(theta_deg)
    R = np.eye(4)
    if axis == 'X':
        R[:3, :3] = np.array([[1, 0, 0],
                              [0, cos(t), -sin(t)],
                              [0, sin(t),  cos(t)]])
    elif axis == 'Y':
        R[:3, :3] = np.array([[ cos(t), 0, sin(t)],
                              [ 0,      1, 0     ],
                              [-sin(t), 0, cos(t)]])
    else:  # 'Z'
        R[:3, :3] = np.array([[cos(t), -sin(t), 0],
                              [sin(t),  cos(t), 0],
                              [0,       0,      1]])
    return R

def frame_axes_points(T, length=1.0):
    """Return 3 axis segments (start,end) for X(red), Y(green), Z(blue) in world coords."""
    o = T[:3, 3]
    R = T[:3, :3]
    x_end = o + R @ np.array([length, 0, 0])
    y_end = o + R @ np.array([0, length, 0])
    z_end = o + R @ np.array([0, 0, length])
    return (o, x_end), (o, y_end), (o, z_end)

# ---------- App ----------
class FramesApp:
    def __init__(self, root):
        self.root = root
        root.title("3D Kinematics: Incremental Frames")

        # State: list of world transforms T_i, start with base at origin
        self.frames = [np.eye(4)]

        # --- UI controls ---
        ctrl = ttk.Frame(root, padding=8)
        ctrl.grid(row=0, column=0, sticky="nsew")

        # Inputs
        self.dx_var = tk.StringVar(value="0.0")
        self.dy_var = tk.StringVar(value="0.0")
        self.dz_var = tk.StringVar(value="0.0")
        self.axis_var = tk.StringVar(value="Z")
        self.ang_var = tk.StringVar(value="0.0")

        row = 0
        ttk.Label(ctrl, text="Δx").grid(row=row, column=0, sticky="e"); 
        ttk.Entry(ctrl, textvariable=self.dx_var, width=10).grid(row=row, column=1, sticky="w")
        ttk.Label(ctrl, text="Δy").grid(row=row, column=2, sticky="e"); 
        ttk.Entry(ctrl, textvariable=self.dy_var, width=10).grid(row=row, column=3, sticky="w")
        ttk.Label(ctrl, text="Δz").grid(row=row, column=4, sticky="e"); 
        ttk.Entry(ctrl, textvariable=self.dz_var, width=10).grid(row=row, column=5, sticky="w")

        row += 1
        ttk.Label(ctrl, text="Axis").grid(row=row, column=0, sticky="e")
        ttk.Combobox(ctrl, textvariable=self.axis_var, values=["X","Y","Z"], width=8, state="readonly").grid(row=row, column=1, sticky="w")
        ttk.Label(ctrl, text="Angle (°)").grid(row=row, column=2, sticky="e")
        ttk.Entry(ctrl, textvariable=self.ang_var, width=10).grid(row=row, column=3, sticky="w")

        row += 1
        ttk.Button(ctrl, text="Add Frame", command=self.add_frame).grid(row=row, column=0, columnspan=2, sticky="ew", pady=(6,0))
        ttk.Button(ctrl, text="Reset", command=self.reset).grid(row=row, column=2, columnspan=2, sticky="ew", pady=(6,0))
        ttk.Button(ctrl, text="Fit View", command=self.fit_view).grid(row=row, column=4, columnspan=2, sticky="ew", pady=(6,0))

        # --- Matplotlib 3D canvas ---
        fig = Figure(figsize=(6.5, 6.5), dpi=100)
        self.ax = fig.add_subplot(111, projection='3d')
        self.ax.set_box_aspect([1,1,1])
        self.canvas = FigureCanvasTkAgg(fig, master=root)
        self.canvas.get_tk_widget().grid(row=0, column=1, sticky="nsew")

        # Layout weights
        root.columnconfigure(1, weight=1)
        root.rowconfigure(0, weight=1)

        self.update_plot(initial=True)

    # ---- actions ----
    def add_frame(self):
        try:
            dx = float(self.dx_var.get())
            dy = float(self.dy_var.get())
            dz = float(self.dz_var.get())
            ang = float(self.ang_var.get())
            axis = self.axis_var.get()
        except ValueError:
            print("Please enter valid numbers for dx, dy, dz, and angle.")
            return

        T_prev = self.frames[-1]
        # Convention: apply translation then rotation w.r.t. the *previous frame axes*
        # i.e., T_new = T_prev * Trans(dx,dy,dz) * R_axis(ang)
        T_new = T_prev @ T_translate(dx, dy, dz) @ R_axis_angle(axis, ang)
        self.frames.append(T_new)

        # Print the 4x4 homogeneous transform to terminal
        np.set_printoptions(precision=4, suppress=True)
        print(f"\nFrame {len(self.frames)-1} (world):")
        print(T_new)

        self.update_plot()

    def reset(self):
        self.frames = [np.eye(4)]
        self.update_plot()

    def fit_view(self):
        # Autoscale to include all origins
        pts = np.array([T[:3,3] for T in self.frames])
        if len(pts) == 0:
            pts = np.zeros((1,3))
        mins = pts.min(axis=0) - 0.5
        maxs = pts.max(axis=0) + 0.5
        # Make cube bounds
        span = max(maxs - mins)
        center = (mins + maxs)/2.0
        lower = center - span/2.0
        upper = center + span/2.0
        self.ax.set_xlim(lower[0], upper[0])
        self.ax.set_ylim(lower[1], upper[1])
        self.ax.set_zlim(lower[2], upper[2])
        self.canvas.draw_idle()

    # ---- drawing ----
    def update_plot(self, initial=False):
        self.ax.cla()
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_zlabel("Z")
        self.ax.view_init(elev=22, azim=-60)

        # Draw frames as triads and links between origins
        # Choose axis length based on spread
        origins = np.array([T[:3,3] for T in self.frames])
        if len(origins) >= 2:
            span = np.linalg.norm(origins.max(axis=0) - origins.min(axis=0))
        else:
            span = 1.0
        axis_len = max(0.2, 0.12*span)

        # Draw base frame in darker tones, subsequent in brighter
        for i, T in enumerate(self.frames):
            (o,x_end), (o2,y_end), (o3,z_end) = frame_axes_points(T, length=axis_len)
            # X (red), Y (green), Z (blue)
            self.ax.plot([o[0], x_end[0]], [o[1], x_end[1]], [o[2], x_end[2]], lw=2, color='r')
            self.ax.plot([o2[0], y_end[0]], [o2[1], y_end[1]], [o2[2], y_end[2]], lw=2, color='g')
            self.ax.plot([o3[0], z_end[0]], [o3[1], z_end[1]], [o3[2], z_end[2]], lw=2, color='b')
            self.ax.scatter([o[0]], [o[1]], [o[2]], s=18, color='k' if i==0 else '0.25')
            self.ax.text(o[0], o[1], o[2], f" {i}", fontsize=9)

        # Links between consecutive origins
        if len(self.frames) >= 2:
            for i in range(1, len(self.frames)):
                a = self.frames[i-1][:3,3]
                b = self.frames[i][:3,3]
                self.ax.plot([a[0], b[0]], [a[1], b[1]], [a[2], b[2]], lw=2, linestyle='-', color='k')

        # Set bounds
        if initial:
            self.ax.set_xlim(-1, 1)
            self.ax.set_ylim(-1, 1)
            self.ax.set_zlim(-1, 1)
        else:
            self.fit_view()

        self.canvas.draw_idle()

if __name__ == "__main__":
    root = tk.Tk()
    app = FramesApp(root)
    root.mainloop()
