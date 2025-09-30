def c_to_f(c):
    return c * 9/5 + 32

def f_to_c(f):
    return (f - 32) * 5/9

c = 100
F = c_to_f(c)   
print(F)

F = c_to_f(32)
print(F)
F = c_to_f(110)
print(F)
F = c_to_f(0)
print(F)
F = c_to_f(2)
print(F)

