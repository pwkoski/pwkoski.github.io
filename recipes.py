import pandas as pd
from pyscript import display, window, document
import js
import math
#import squarify
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import json




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
recipe_list = js.sessionStorage.getItem("recipe_list")

#display(print("this is recipe_list: ", recipe_list))
#display(print("this is recipe_list type: ", type(recipe_list)))


json_acceptable_string = recipe_list.replace("'", "\"")
recipe_dict = json.loads(json_acceptable_string)


#display(print("this is recipe_dict: ", recipe_dict))
#display(print("this is recipe_dict type: ", type(recipe_dict)))

#Convert to dataframe
#df1 = pd.read_json(data)

#Returns a string for HTML table for each ingredient.
def generate_recipe_table(recipe_list):
   htmlString = ""
   for i in range(0, len(recipe_list) - 1):
     recipe = recipe_list[i]
     recipe_string = "<table>\n"
     recipe_string = recipe_string + "<tr>\n"
     recipe_string = recipe_string + "<th align=\"left\">Recipe Name: </th>\n"
     recipe_string = recipe_string + "<th align=\"left\">" + recipe["name"] + "</th>\n"
     recipe_string = recipe_string + "</tr>\n"

     recipe_string = recipe_string + "<tr>\n"
     recipe_string = recipe_string + "<th align=\"left\">Recipe Calories: </th>\n"
     recipe_string = recipe_string + "<td>" + str(recipe["recipe_calories"]) + "</td>\n"
     recipe_string = recipe_string + "</tr>\n"

     recipe_string = recipe_string + "<tr>\n"
     recipe_string = recipe_string + "<th align=\"left\">Recipe Source: </th>\n"
     recipe_string = recipe_string + "<td>" + recipe["source"] + "</td>\n"
     recipe_string = recipe_string + "</tr>\n"

     recipe_string = recipe_string + "<tr>\n"
     recipe_string = recipe_string + "<th align=\"left\">Ingredients: </th>\n"
     recipe_string = recipe_string + "</tr>\n"
     #recipe_string = recipe_string + "<tr>\n"
     ingredient_list = recipe['ingredients_and_amounts_in_milliliters']

     #display(print("this is ingredient_list: ", ingredient_list))
     #display(print("this is ingredient_list type: ", type(ingredient_list)))

     for i in range(0, len(ingredient_list) - 2, 2):
      recipe_string = recipe_string + "<tr>" + "<td>" + str(ingredient_list[i + 1]) + " mL " + "</td>" + "<td>" + str(ingredient_list[i]) + "</td>" + "</tr>\n"

     #recipe_string = recipe_string + "</tr>\n"

     recipe_string = recipe_string + "</table>\n"
     htmlString = htmlString + recipe_string

   return htmlString

table_html = generate_recipe_table(recipe_dict['recipes'])

#Display as HTML table
#display(print("this is table_html: ", table_html))
htmlObject = document.querySelector("#recipes")
htmlObject.innerHTML = table_html

