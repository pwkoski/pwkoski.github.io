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


def calc_nutrition_per_ingred(ingredient_dataframe):

  #ingredient_dataframe['no_of_plants'] = pd.Series([0] * len(ingredient_dataframe))
 ingredient_dataframe['total_carbs'] = ingredient_dataframe['total_grams'] * ingredient_dataframe['carb_percentage']

 ingredient_dataframe['total_protein'] = ingredient_dataframe['total_grams'] * ingredient_dataframe['protein_percentage']

 ingredient_dataframe['total_fat'] = ingredient_dataframe['total_grams'] * ingredient_dataframe['fat_percentage']

 ingredient_dataframe['total_calories'] = ingredient_dataframe['total_grams'] * ingredient_dataframe['calories_per_gram']

 return ingredient_dataframe

df1 = calc_nutrition_per_ingred(df1)

monthly_carbs = df1['total_carbs'].sum()
monthly_protein = df1['total_protein'].sum()
monthly_fat = df1['total_fat'].sum()
monthly_calories = df1['total_calories'].sum()

# create data
monthly_caloric_limit = 60000
x = ['Carbs', 'Protein', 'Fat']
desired = [0.5 * monthly_caloric_limit, 0.3 * monthly_caloric_limit, 0.2 * monthly_caloric_limit]
actual = [monthly_carbs, monthly_protein, monthly_fat]



# plot bars in stack manner
#fig, ax = plt.subplots()

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Nutritional Information for One Month Period')
ax1.bar("Calories", monthly_caloric_limit, color='grey', label="Desired")
ax1.bar("Calories", monthly_calories, color='red', label="Actual")
ax2.bar(x, desired, color='grey', label="Desired")
ax2.bar(x, actual, color='red', label="Actual")
ax2.yaxis.tick_right()


plt.legend()
plt.show()