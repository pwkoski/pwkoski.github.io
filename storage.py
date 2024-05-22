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


def calc_number_of_containers_per_ingred(ingredient_dataframe):

  #ingredient_dataframe['no_of_plants'] = pd.Series([0] * len(ingredient_dataframe))
 ingredient_dataframe['no_of_containers'] = ingredient_dataframe['total_grams'] / ingredient_dataframe['grams_per_container']

 ingredient_dataframe.loc[ingredient_dataframe['storage'] == '16oz jar', 'container_area'] = ingredient_dataframe['no_of_containers'] / ingredient_dataframe['containers_per_square_meter']
 ingredient_dataframe.loc[ingredient_dataframe['storage'] != '16oz jar', 'container_area'] = 0.0

 ingredient_dataframe.loc[ingredient_dataframe['storage'] == '1 gal bag', 'container_volume'] = ingredient_dataframe['no_of_containers'] / ingredient_dataframe['containers_per_cubic_meter']
 ingredient_dataframe.loc[ingredient_dataframe['storage'] != '1 gal bag', 'container_volume'] = 0.0

 #if ingredient_dataframe['storage'] == "16oz jar":
 #   ingredient_dataframe['container_area'] = ingredient_dataframe['no_of_containers'] / ingredient_dataframe['containers_per_square_meter']
 #elif ingredient_dataframe['storage'] == "1 gal bag":
 #   ingredient_dataframe['container_volume'] = ingredient_dataframe['no_of_containers'] / ingredient_dataframe['containers_per_cubic_meter']


 ingredient_dataframe['yearly_no_of_containers'] = 12 * ingredient_dataframe['no_of_containers']

 ingredient_dataframe['yearly_no_of_containers'] = ingredient_dataframe['yearly_no_of_containers'].apply(math.ceil)

 ingredient_dataframe['yearly_container_area'] = 12 * ingredient_dataframe['container_area']

 #ingredient_dataframe['yearly_container_area'] = ingredient_dataframe['yearly_container_area'].apply(math.ceil)

 ingredient_dataframe['yearly_container_volume'] = 12 * ingredient_dataframe['container_volume']

 #ingredient_dataframe['yearly_container_volume'] = ingredient_dataframe['yearly_container_volume'].apply(math.ceil)



 return ingredient_dataframe

df1 = calc_number_of_containers_per_ingred(df1)


df_display = df1[['name', 'yearly_no_of_containers', 'storage_type', 'storage', 'yearly_container_area', 'yearly_container_volume' ]]
df_display = df_display.rename(columns={'name': 'Ingredient Name', 'yearly_no_of_containers': 'Yearly Number of Containers', "storage_type": "Dry/Frozen Storage", 'storage': "Container Type", 'yearly_container_area': "Area for Storage (sq. m)", 'yearly_container_volume': "Volume for Storage (cu. m)" })

#Display as HTML table
df_html = df_display.to_html()
htmlObject = document.querySelector("#my_table")
htmlObject.innerHTML = df_html

