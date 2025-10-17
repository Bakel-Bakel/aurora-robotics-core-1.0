import math

def Rx(t):
    c, s = math.cos(t), math.sin(t)
    return [[1, 0, 0],
            [0, c,-s],
            [0, s, c]]

def Ry(t):
    c, s = math.cos(t), math.sin(t)
    return [[ c, 0, s],
            [ 0, 1, 0],
            [-s, 0, c]]

def Rz(t):
    c, s = math.cos(t), math.sin(t)
    return [[c,-s, 0],
            [s, c, 0],
            [0, 0, 1]]

def pretty_print(M, width=9, prec=4, label="R"):
    fmt = f"{{:{width}.{prec}f}}"
    print(f"{label} =")
    for row in M:
        print("[ " + "  ".join(fmt.format(x) for x in row) + " ]")

if __name__ == "__main__":
    axis = input("Axis (x/y/z): ").strip().lower()
    try:
        ang_deg = float(input("Angle (degrees): ").strip())
    except ValueError:
        print("Invalid angle."); raise SystemExit(1)

    t = math.radians(ang_deg)

    if axis == "x":
        R = Rx(t); lbl = f"R_x({ang_deg}°)"
    elif axis == "y":
        R = Ry(t); lbl = f"R_y({ang_deg}°)"
    elif axis == "z":
        R = Rz(t); lbl = f"R_z({ang_deg}°)"
    else:
        print("Axis must be x, y, or z."); raise SystemExit(1)

    pretty_print(R, label=lbl)
