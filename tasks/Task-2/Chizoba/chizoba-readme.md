I made sure to try writing the code myself initially using docs and explainations of logic from gpt
you will notice some codes are commented out
# x1_link = np.array([base[0],joint[0]])
# y1_link = np.array([base[1], joint[1]])
# x2_link = np.array([joint[0], ee[0]])
# y2_link = np.array([joint[1], ee[1]])
# plt.plot(x1_link, y1_link, 'o-', label="Link 1")
# plt.plot(x2_link, y2_link, 'o-', label="Link 2")
Thats because initially this is what I used to draw the initial plot. but when it was time to update the plot. I saw that I won't be able to easily reuse the x and y links. so I checked you code and saw this
<!-- (link_line, ) = ax.plot([base[0], joint[0], ee[0]],
                      [base[1], joint[1], ee[1]],
                      marker="o", linewidth = '2') -->
<!-- def updatePlot(val):
    th_1 = np.deg2rad(s_theta1.val)
    th_2 = np.deg2rad(s_theta2.val)
    b, j, e = drawPlot(th_1, th_2)
    link_line.set_data([b[0], j[0], e[0]], [b[1], j[1], e[1]])
    plt.draw() -->

This was much better and reusable, so I decided to use it, thanks.