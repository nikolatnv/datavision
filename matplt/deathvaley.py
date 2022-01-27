import csv
from matplotlib import pyplot as plt
from datetime import datetime


dates, max_t, min_t = [], [], []
filename = 'data/deathvaley.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    for row in reader:
        current_data = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            maxt = int(row[4])
            mint = int(row[5])
        except ValueError as e:
            print(f'пропущенна дата {current_data}')
        else:
            max_t.append(maxt)
            min_t.append(mint)
            dates.append(current_data)

plt.style.use('seaborn')
fig, ax = plt.subplots()    # type:  plt.Axes
ax.plot(dates, max_t, c='red', alpha=0.5)
ax.plot(dates, min_t, c='blue', alpha=0.5)
plt.fill_between(dates, max_t, min_t, facecolor='blue', alpha=0.1)
plt.title('температура за 2018г.', fontsize=24)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Температура (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
