import matplotlib.pyplot as plt
from randomwalk import RandomWalk


while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    fontdict = {'fontsize': 14,}
    plt.style.use('seaborn')
    fix, ax = plt.subplots(figsize=(13, 8), dpi=128)  # type: plt.Axes
    point_numbers = range(rw.num_pints)
    ax.plot(rw.x_values, rw.y_values, linewidth=12)

    # ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
    #            edgecolor='none', s=1)
    # Выделение первой и последней точки
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.y_values[-1], rw.y_values[-1], c='red', edgecolors='none',
               s=100)
    # Удаление осей
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_runing = input(f'Запустить случайное блуждание? (д/н): ')
    if keep_runing == 'n' or keep_runing == 'н':
        break