import matplotlib.pyplot as plt

squares = [1, 2, 4, 12, 4]

fix, ax = plt.subplots() # type: plt.Axes
ax.plot(squares, linewidth=3)
plt.show()