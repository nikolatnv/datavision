import matplotlib.pyplot as plt
from randomwalk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

fontdict = {'fontsize': 14,}
plt.style.use('seaborn')
fix, ax = plt.subplots() # type: plt.Axes

ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()