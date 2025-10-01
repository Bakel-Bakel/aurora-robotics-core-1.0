# Python & C++ Training Codes – Rotation Matrices & Basics

This folder contains simple demo codes used for the class training.  
They are short, standalone programs that can run independently.  

---

## 📌 Contents

### 1. **Python Codes**
- **`rotation.py`**  
  - Requests an axis (`x`, `y`, or `z`) and an angle in degrees.  
  - Computes the corresponding 3×3 rotation matrix using `sin` and `cos`.  
  - Prints the result neatly formatted as a matrix.  


---

### 2. **C++ Codes**
- **`rotation.cpp`**  
  - Requests an axis (`x`, `y`, or `z`) and an angle in degrees.  
  - Computes the 3×3 rotation matrix.  
  - Prints the matrix in a neat format with fixed precision.  

---

## ⚙️ Requirements

### Python
- Python 3.8+  
- Standard libraries: `math`  
- Optional: `numpy`, `matplotlib` for extra demos  

Install requirements (if needed):
```bash
pip install numpy matplotlib
```

Run:
```bash
python rotation.py
```

---

### C++
- C++17 or newer compiler (e.g., g++ or clang++).  
- No external dependencies.  

Compile & run:
```bash
g++ -std=c++17 rotation.cpp -o rotation
./rotation
```



---

## ✅ Example Session

```text
Axis (x/y/z): z
Angle (degrees): 90
R_z(90°) =
[     0.0000     -1.0000      0.0000 ]
[     1.0000      0.0000      0.0000 ]
[     0.0000      0.0000      1.0000 ]
```

---

## 📚 Learning Objectives

- Understand how to compute and format rotation matrices.  
- Build intuition for how computers represent 3D rotations.  

---
