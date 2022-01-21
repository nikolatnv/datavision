from kubiki import Kubik
from plotly.graph_objs import Bar, Layout
from plotly import offline


kubiki = Kubik()

results = []
for roll_num in range(1000):
    result = kubiki.roll()
    results.append(result)

frequencies = []
for value in range(1, kubiki.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов
x_values = list(range(1, kubiki.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_conf = {'title': 'result', }
y_axis_conf = {'title': 'frequencies of Result'}
m_layout = Layout(title='Результат 1000 бросков кубика', xaxis=x_axis_conf,
                  yaxis=y_axis_conf)
offline.plot({'data': data, 'layout': m_layout}, filename='kubik.html')