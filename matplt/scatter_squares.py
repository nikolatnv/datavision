import matplotlib.pyplot as plt


x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
fontdict = {'fontsize': 14, }
datadict = {'which': 'major', 'labelsize': 14, }
style = plt.style.available[11]
plt.style.use(style)
fig, ax = plt.subplots()    # type: plt.Axes
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.get_cmap('Greens'), s=10)
ax.set_title('точка на графике', fontdict)
ax.set_xlabel('значение', fontdict)
ax.set_ylabel('расстояние', fontdict)
ax.tick_params(axis='both', **datadict)
ax.axis([0, 1100, 0, 110000])
plt.show()