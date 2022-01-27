import json
from plotly.graph_objs import Layout
from plotly import offline

filename = 'data/dat_eq.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dict = all_eq_data['features']
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dict:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    lons.append(lon)
    lats.append(lat)
    mags.append(mag)
    hover_texts.append(title)

data = [{'type': 'scattergeo',
         'lon': lons,
         'lat': lats,
         'text': hover_texts,
         'marker': {
             'size': [5*mag for mag in mags],
             'color': mags,
             'colorscale': 'Viridis',
             'reversescale': True,
             'colorbar': {'title': 'Магнитуда'},
          }, }]

my_layout = Layout(title='Землетрясение')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_erthquaqes.html')

print(mags[:10])
print(lats[:5])
print(lons[:5])
# readable_file = 'data/eq_r_file.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)
#
