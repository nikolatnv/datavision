import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5,]
squares = [1, 2, 4, 12, 4]
fontdict = {'fontsize': 14,}
plt.style.use('seaborn')
fix, ax = plt.subplots() # type: plt.Axes
ax.plot(input_value, squares, linewidth=3)
ax.set_title('первый график', fontdict=fontdict)
ax.set_xlabel('значения', fontdict=fontdict)
ax.set_ylabel('величина', fontdict=fontdict)
ax.tick_params(axis='both', labelsize=14)
plt.show()
print(plt.style.available)