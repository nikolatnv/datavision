from kubiki import Kubik
from plotly.graph_objs import Bar, Layout
from plotly import offline


kubiki_1 = Kubik()
kubiki_2 = Kubik()

results = []
for roll_num in range(1000):
    result = kubiki_1.roll() + kubiki_2.roll()
    results.append(result)

frequencies = []
max_result = kubiki_1.num_sides + kubiki_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_conf = {'title': 'result', 'dtick': 1}
y_axis_conf = {'title': 'frequencies of Result'}
m_layout = Layout(title='Результат 1000 бросков кубика', xaxis=x_axis_conf,
                  yaxis=y_axis_conf)
offline.plot({'data': data, 'layout': m_layout}, filename='kubik.html')