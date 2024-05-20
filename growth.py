import pandas as pd
from pyscript import display
import js
import math
import squarify
import matplotlib.pyplot as plt

#Import
#Gets item from storage as a JSON in string format.
data = js.sessionStorage.getItem("df")

#Convert to dataframe
df1 = pd.read_json(data)


def calc_number_of_plants_per_ingred(ingredient_dataframe):

  #ingredient_dataframe['no_of_plants'] = pd.Series([0] * len(ingredient_dataframe))

  ingredient_dataframe['no_of_plants'] = ingredient_dataframe['total_grams'] / ingredient_dataframe['grams_yield_per_plant']

  return ingredient_dataframe


def calc_grow_area_per_ingred(ingredient_dataframe):

    ingredient_dataframe['grow_area_sq_meters'] = ingredient_dataframe['no_of_plants'] / ingredient_dataframe['plants_per_square_meter']

    return ingredient_dataframe


df1 = calc_number_of_plants_per_ingred(df1)
df1 = calc_grow_area_per_ingred(df1)

# these values define the coordinate system for the returned rectangles
# the values will range from x to x + width and y to y + height
x = 0.
y = 0.
area = df1['grow_area_sq_meters'].sum()

width = math.sqrt(2 * area)
height = 0.5 * width

values = df1[['name', 'grow_area_sq_meters']]

# values must be sorted descending (and positive, obviously)
#values.sort(reverse=True)
sorted = values.sort_values(by=['grow_area_sq_meters'], ascending=False)

display(print("this is sorted: ", sorted))
display(print("this is values type: ", type(values)))
display(print("this is total area: ", area, " sq. meters"))
display(print("type width : ", type(width), " meters, type height: ", type(height), " meters"))

# the sum of the values must equal the total area to be laid out
# i.e., sum(values) == width * height
listvalues = sorted['grow_area_sq_meters'].to_list()
listnames = sorted['name'].to_list()
#listvalues.sort(reverse=True)

display(print("this is listvalues: ", listvalues))
display(print("this is listvalues type: ", type(listvalues[0])))
display(print('check if df dx bs is true: ', width * height == df1['grow_area_sq_meters'].sum()))

colorArray = ['#FF6633', '#FFB399', '#FF33FF', '#FFFF99', '#00B3E6',
		  '#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D',
		  '#80B300', '#809900', '#E6B3B3', '#6680B3', '#66991A',
		  '#FF99E6', '#CCFF1A', '#FF1A66', '#E6331A', '#33FFCC',
		  '#66994D', '#B366CC', '#4D8000', '#B33300', '#CC80CC',
		  '#66664D', '#991AFF', '#E666FF', '#4DB3FF', '#1AB399',
		  '#E666B3', '#33991A', '#CC9999', '#B3B31A', '#00E680',
		  '#4D8066', '#809980', '#E6FF80', '#1AFF33', '#999933',
		  '#FF3380', '#CCCC00', '#66E64D', '#4D80CC', '#9900B3',
		  '#E64D66', '#4DB380', '#FF4D4D', '#99E6E6', '#6666FF']

colorArray = colorArray[0:15]

values = squarify.normalize_sizes(listvalues, width, height)

display(print("this is normalized values: ", values))
display(print("this is list of names: ", listnames))


#rects = squarify.squarify(values, x, y, width, height)

fig, ax = plt.subplots()

#plt.figure(num=None, figsize=(width + 4, height + 2))

#ax = squarify.plot(label=listnames, sizes=values, ec = 'black', color=colorArray)

ax.bar(x=listnames, height=listvalues, label=listnames, color=colorArray)

h, l = ax.get_legend_handles_labels()
display(print("this is h and type: ", h, ' ', type(h)))
display(print("this is list(l[0]) and type: ", l, ' ', type(l)))
ax.legend(listnames)


display(print("this is listnames: ", listnames))
display(print("this is length of listnames ", len(listnames)))



#ax.legend(labels=listnames, bbox_to_anchor=(.4, .8), borderaxespad=0)
#loc="right"

fig.show()
#plt.show()

