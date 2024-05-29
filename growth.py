import pandas as pd
from pyscript import display, document
import js
import matplotlib.pyplot as plt
import functions

#Gets item from storage as a JSON.
data = js.sessionStorage.getItem("df")

#Convert to dataframe
df = pd.read_json(data)

#Perform calculations
df = functions.calc_number_of_plants_per_ingred(df)
df = functions.calc_grow_area_per_ingred(df)

#Rename columns for display
df_display = df[['name', 'yearly_no_of_plants', 'yearly_grow_area']]
df_display = df_display.rename(columns={'name': 'Ingredient Name', 'yearly_no_of_plants': 'Yearly Number of Plants', "yearly_grow_area": "Ingredient Yearly Grow Area (sq. m)"})

#Display as HTML table
df_html = df_display.to_html(index_names=False, index=False)
htmlObject = document.querySelector("#my_table")
htmlObject.innerHTML = df_html

#Prepare inputs for the Garden Layout function
values = df[['name', 'yearly_grow_area']]

#Inputs must be sorted descending
sorted = values.sort_values(by=['yearly_grow_area'], ascending=False)

#Inputs must be Python lists
area_values = sorted['yearly_grow_area'].to_list()
ingredient_names = sorted['name'].to_list()

#Create and display garden plot
fig, ax = plt.subplots()
fig, ax = functions.generate_garden_layout(fig, ax,ingredient_names, area_values, 20.0, 0.914, 0.6096, functions.color_array)
display(fig, target="pythontable")
