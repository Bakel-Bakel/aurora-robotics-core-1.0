import numpy as np 
import matplotlib.pyplot as plt 

fig = plt.figure()             # an empty figure with no Axes
ax = plt.subplots()  
# a figure with one Axes on the left, and two on the right:
fig, axs = plt.subplot_mosaic([['left', 'right_top'],
                               ['left', 'right_top'],
                               ['left', 'right_bottom']])

plt.show()