# 2d_frames_gui.py
# Requirements: python -m pip install numpy matplotlib
# (On Linux you may need: sudo apt-get install python3-tk)

import tkinter as tk
from tkinter import ttk
import numpy as np
from math import cos, sin, radians
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# ---------- 2D transform helpers (3x3 homogeneous) ----------
def T_translate(dx, dy):
    T = np.eye(3)
    T[:2, 2] = [dx, dy]
    return T

def Rz(theta_deg):
    t = radians(theta_deg)
    c, s = cos(t), sin(t)
    T = np.eye(3)
    T[:2, :2] = np.array([[c, -s],
                          [s,  c]])
    return T

def frame_axes_points(T, length=1.0):
    """Return line segments ((x0,y0)->(x1,y1)) for X(red) and Y(green) axes in world coords."""
    o = T[:2, 2]
    R = T[:2, :2]
    x_end = o + R @ np.array([length, 0.0])
    y_end = o + R @ np.array([0.0, length])
    return (o, x_end), (o, y_end)

# ---------- App ----------
class Frames2DApp:
    def __init__(self, root):
        self.root = root
        root.title("2D Kinematics: Incremental Frames")

        # State: list of world transforms (3x3), start with base at origin
        self.frames = [np.eye(3)]

        # --- Controls ---
        panel = ttk.Frame(root, padding=8)
        panel.grid(row=0, column=0, sticky="nsew")

        self.dx_var = tk.StringVar(value="0.0")
        self.dy_var = tk.StringVar(value="0.0")
        self.ang_var = tk.StringVar(value="0.0")

        r = 0
        ttk.Label(panel, text="Δx").grid(row=r, column=0, sticky="e")
        ttk.Entry(panel, textvariable=self.dx_var, width=10).grid(row=r, column=1, sticky="w")
        ttk.Label(panel, text="Δy").grid(row=r, column=2, sticky="e")
        ttk.Entry(panel, textvariable=self.dy_var, width=10).grid(row=r, column=3, sticky="w")

        r += 1
        ttk.Label(panel, text="Angle (°)").grid(row=r, column=0, sticky="e")
        ttk.Entry(panel, textvariable=self.ang_var, width=10).grid(row=r, column=1, sticky="w")

        r += 1
        ttk.Button(panel, text="Add Frame", command=self.add_frame).grid(row=r, column=0, columnspan=2, sticky="ew", pady=(6,0))
        ttk.Button(panel, text="Reset", command=self.reset).grid(row=r, column=2, sticky="ew", pady=(6,0))
        ttk.Button(panel, text="Fit View", command=self.fit_view).grid(row=r, column=3, sticky="ew", pady=(6,0))

        # --- Matplotlib canvas (2D) ---
        fig = Figure(figsize=(6.2, 6.2), dpi=100)
        self.ax = fig.add_subplot(111)
        self.ax.set_aspect("equal", adjustable="box")
        self.ax.grid(True, linestyle=":", linewidth=0.6)
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
            ang = float(self.ang_var.get())
        except ValueError:
            print("Please enter valid numbers for Δx, Δy, and Angle.")
            return

        T_prev = self.frames[-1]
        # Convention: translation then rotation w.r.t. previous frame axes
        # T_new = T_prev * Trans(dx,dy) * Rz(theta)
        T_new = T_prev @ T_translate(dx, dy) @ Rz(ang)
        self.frames.append(T_new)

        # Print 3x3 homogeneous transform
        np.set_printoptions(precision=4, suppress=True)
        print(f"\nFrame {len(self.frames)-1} :")
        print(T_new)

        self.update_plot()

    def reset(self):
        self.frames = [np.eye(3)]
        self.update_plot()

    def fit_view(self):
        pts = np.array([T[:2, 2] for T in self.frames])
        if len(pts) == 0:
            pts = np.zeros((1,2))
        mins = pts.min(axis=0) - 0.5
        maxs = pts.max(axis=0) + 0.5
        span = max(maxs - mins)
        center = (mins + maxs)/2.0
        lower = center - span/2.0
        upper = center + span/2.0
        self.ax.set_xlim(lower[0], upper[0])
        self.ax.set_ylim(lower[1], upper[1])
        self.canvas.draw_idle()

    # ---- drawing ----
    def update_plot(self, initial=False):
        self.ax.cla()
        self.ax.set_aspect("equal", adjustable="box")
        self.ax.grid(True, linestyle=":", linewidth=0.6)
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")

        origins = np.array([T[:2,2] for T in self.frames])
        if len(origins) >= 2:
            span = np.linalg.norm(origins.max(axis=0) - origins.min(axis=0))
        else:
            span = 1.0
        axis_len = max(0.2, 0.18*span)

        # Draw frames
        for i, T in enumerate(self.frames):
            (o, x_end), (_, y_end) = frame_axes_points(T, length=axis_len)
            self.ax.plot([o[0], x_end[0]], [o[1], x_end[1]], lw=2, color='r')  # X
            self.ax.plot([o[0], y_end[0]], [o[1], y_end[1]], lw=2, color='g')  # Y
            self.ax.scatter([o[0]], [o[1]], s=20, color='k' if i==0 else '0.25')
            self.ax.text(o[0], o[1], f" {i}", fontsize=9, va="center", ha="left")

        # Links between consecutive origins
        if len(self.frames) >= 2:
            for i in range(1, len(self.frames)):
                a = self.frames[i-1][:2, 2]
                b = self.frames[i][:2, 2]
                self.ax.plot([a[0], b[0]], [a[1], b[1]], lw=2, color='k')

        # Bounds
        if initial:
            self.ax.set_xlim(-1, 1)
            self.ax.set_ylim(-1, 1)
        else:
            self.fit_view()

        self.canvas.draw_idle()

if __name__ == "__main__":
    root = tk.Tk()
    app = Frames2DApp(root)
    root.mainloop()
