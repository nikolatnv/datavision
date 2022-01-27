import csv
from matplotlib import pyplot as plt
from datetime import datetime


dates, max_t, min_t = [], [], []
filename = 'data/sitka.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    for row in reader:
        current_data = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            maxt = int(row[8])
            mint = int(row[9])
            max_t.append(maxt)
            min_t.append(mint)
            dates.append(current_data)
        except ValueError as e:
            print(row[8])
            print(row[9])

plt.style.use('seaborn')
fig, ax = plt.subplots()    # type:  plt.Axes
ax.plot(dates, max_t, c='red', alpha=0.5)
ax.plot(dates, min_t, c='blue', alpha=0.5)
plt.fill_between(dates, max_t, min_t, facecolor='blue', alpha=0.1)
plt.title('Низкая температура за 2018г.', fontsize=24)
plt.title('Высокая температура за 2018г.', fontsize=24)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Температура (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()






