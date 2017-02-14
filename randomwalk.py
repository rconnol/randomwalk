import random
from bokeh.plotting import figure, curdoc
from bokeh.driving import linear

p = figure(plot_width = 800, plot_height = 400)
r1 = p.line(x=[0], y=[0], line_width=2, color='#666699')

ds1 = r1.data_source

@linear()
def update(step):
	value = random.choice([-1, 1])
	ds1.data['x'].append(step)
	ds1.data['y'].append(ds1.data['y'][-1]+value)
	ds1.trigger('data', ds1.data, ds1.data)


curdoc().add_root(p)

curdoc().add_periodic_callback(update, 50)
