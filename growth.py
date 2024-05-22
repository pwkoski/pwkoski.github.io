import pandas as pd
from pyscript import display, window, document
import js
import math
#import squarify
import matplotlib.pyplot as plt
import matplotlib.patches as patches




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

#Import
#Gets item from storage as a JSON in string format.
data = js.sessionStorage.getItem("df")

#Convert to dataframe
df1 = pd.read_json(data)


def calc_number_of_plants_per_ingred(ingredient_dataframe):

  #ingredient_dataframe['no_of_plants'] = pd.Series([0] * len(ingredient_dataframe))

  ingredient_dataframe['no_of_plants'] = ingredient_dataframe['total_grams'] / ingredient_dataframe['grams_yield_per_plant']

  ingredient_dataframe['yearly_no_of_plants'] = 12 * ingredient_dataframe['no_of_plants']

  ingredient_dataframe['yearly_no_of_plants'] = ingredient_dataframe['yearly_no_of_plants'].apply(math.ceil)




  return ingredient_dataframe


def calc_grow_area_per_ingred(ingredient_dataframe):

    ingredient_dataframe['grow_area_sq_meters'] = ingredient_dataframe['no_of_plants'] / ingredient_dataframe['plants_per_square_meter']

    ingredient_dataframe['yearly_grow_area'] = 12 * ingredient_dataframe['grow_area_sq_meters']

    ingredient_dataframe['yearly_grow_area'] = ingredient_dataframe['yearly_grow_area'].apply(math.ceil)

    return ingredient_dataframe


df1 = calc_number_of_plants_per_ingred(df1)
df1 = calc_grow_area_per_ingred(df1)

df_display = df1[['name', 'yearly_no_of_plants', 'yearly_grow_area']]
df_display = df_display.rename(columns={'name': 'Ingredient Name', 'yearly_no_of_plants': 'Yearly Number of Plants', "yearly_grow_area": "Ingredient Yearly Grow Area (sq. m)"})

#Display as HTML table
df_html = df_display.to_html()
htmlObject = document.querySelector("#my_table")
htmlObject.innerHTML = df_html



#area = df1['grow_area_sq_meters'].sum()

values = df1[['name', 'yearly_grow_area']]

# values must be sorted descending (and positive)
#values.sort(reverse=True)
sorted = values.sort_values(by=['yearly_grow_area'], ascending=False)

#display(print("this is sorted: ", sorted))

listvalues = sorted['yearly_grow_area'].to_list()
listnames = sorted['name'].to_list()

#display(print("this is listvalues: ", listvalues))
#display(print("this is listnames: ", listnames))

#fig, ax = plt.subplots()

#ax.bar(x=listnames, height=listvalues, label=listnames, color=colorArray)

#fig.show()

#plt.plot(df1['name'], df1['grow_area_sq_meters'], label='totalarea')
#plt.plot(df1['name'], df1['plants_per_square_meter'], label='totalarea')

#plt.legend()

#plt.show()

#Calculate total grow area for year
area_in_sq_meters = df1['yearly_grow_area'].sum()

#Set the planting row length
row_length_in_m = 20

#Set the grow row width (3 ft)
grow_row_width_in_m = 0.914

#Set the path width (2 ft)
path_width_in_m = 0.6096

#Calculate length of row for entire grow area for a year
total_grow_length_in_m = area_in_sq_meters / grow_row_width_in_m

#Calculate how many rows of planting row length (round up)
no_of_rows = math.ceil(total_grow_length_in_m / row_length_in_m)

#Total length is number of rows * row width plus number of rows times path width
total_plot_length = no_of_rows * grow_row_width_in_m + no_of_rows * path_width_in_m

# Create figure and axes
fig, ax = plt.subplots()

#Set the figure area to the dimensions of plot
ax.set_xlim([0.0, total_plot_length])
ax.set_ylim([0.0, row_length_in_m])

#display(print('this is the number of rows: ', no_of_rows))
#Add the walking path rectangles
for i in range(1, no_of_rows + 1):
   x_coord = grow_row_width_in_m * (i) + path_width_in_m * (i - 1)
   y_coord = 0.0
   width = path_width_in_m
   height = row_length_in_m
   path = patches.Rectangle((x_coord, y_coord), width, height, linewidth=1, edgecolor='darkgoldenrod', facecolor='darkgoldenrod', fill=True, label="Walking Path")
   ax.add_patch(path)

#Add in the grow rows:
#I: a sorted list with areas of different ingredients
#O: a fig and ax?  just an ax? of the grow area

row_remaining = row_length_in_m


#Set starting points for first row
x_coord = 0.0
y_coord = 0.0

for i in range(0, len(listnames)):

   #Get a total row length for each ingredient on a yearly basis
   ingredient_row_length_remaining = listvalues[i] / grow_row_width_in_m



   while ingredient_row_length_remaining > 0:
        #display(print("in while loop"))
        if row_remaining > ingredient_row_length_remaining:
          #Draw rectangle and update ycoord,

          rect = patches.Rectangle((x_coord, y_coord), grow_row_width_in_m, ingredient_row_length_remaining, linewidth=1, edgecolor="black", facecolor=colorArray[i], fill=True, label=listnames[i])
          ax.add_patch(rect)
          y_coord = y_coord + ingredient_row_length_remaining

          row_remaining = row_remaining - ingredient_row_length_remaining
          ingredient_row_length_remaining = 0

        elif row_remaining <= ingredient_row_length_remaining:
           #Draw rectangle, update ycoord to zero, xcoord to next row

          rect = patches.Rectangle((x_coord, y_coord), grow_row_width_in_m, row_remaining, linewidth=1, edgecolor="black", facecolor=colorArray[i], fill=True, label=listnames[i])
          ax.add_patch(rect)

          y_coord = 0
          x_coord = x_coord + grow_row_width_in_m + path_width_in_m
          ingredient_row_length_remaining = ingredient_row_length_remaining - row_remaining
          row_remaining = row_length_in_m

#Gets rid of duplicate legend entries
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), bbox_to_anchor = (1.25, 0.6), loc='center right')

plt.tight_layout()

fig.set_figwidth(15)

plt.axis('equal')

plt.show()
