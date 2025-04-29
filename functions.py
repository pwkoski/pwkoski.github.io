import pandas as pd
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches


#SUMMARY PAGE FUNCTIONS#
#----------------------#

#Creates an ingredient dataframe from an array of dictionarys containing the ingredient entries.  Each key will become a column title and the value will be entered at (row, column) -> (ingredient, key) unless the value is another dictionary.
#@param array_of_dicts: a Python list of dictonaries
#@return: Pandas dataframe with keys as column titles.
def df_recursive_create(array_of_dicts):

    df = pd.DataFrame()

    def recursion(dictionary, index):
        for key in dictionary:
            if type(dictionary[key]) is dict:
                return recursion(dictionary[key], index)
            else:
                df.at[index, key] = dictionary[key]

    for i in range(0, len(array_of_dicts)):
        for dictionary in array_of_dicts[i]:
            recursion(array_of_dicts[i][dictionary], i)

    return df

#Calculates the mass of each ingredient for the month for a particular caloric limit and adds that column to a dataframe.
#@param list_of_recipes: a Python list of recipe dictionaries
#@param ingredient_dataframe: a Pandas dataframe created from ingredients.json
#@param monthly_caloric_limit: a float representing a caloric limit for a 30-day month
#@return: a Pandas dataframe with the monthly grams of each ingredient added
def calc_tot_mass_per_ingred(list_of_recipes, ingredient_dataframe, monthly_caloric_limit=60000.0):

  #Create an empty column, initialize variables
  ingredient_dataframe['total_grams'] = pd.Series([0] * len(ingredient_dataframe))
  calories = 0
  i = 0

  while calories <= monthly_caloric_limit:

    #If at the end of the recipe list, start over
    if i == len(list_of_recipes):
      i = 0

    #Alias for the ingredient list in specific recipe
    ingredient_list = list_of_recipes[i]["ingredients_and_amounts_in_milliliters"]

    #Iterate through the ingredient list for a specific recipe
    for j in range(0, len(ingredient_list) - 1, 2):

      #Alias for a specific ingredient in specific recipe
      ingredient_name = ingredient_list[j]

      #Gets the row label for ingredient row
      dataframe_label = ingredient_dataframe.index[ingredient_dataframe['name'] == ingredient_name][0]

      ingredient_volume_in_ml = ingredient_list[j + 1]

      ingredient_grams_per_milliliter = ingredient_dataframe.at[dataframe_label, "ingredient_grams_per_milliliter"]

      mass_of_ingredient = ingredient_volume_in_ml * ingredient_grams_per_milliliter

      ingredient_dataframe.at[dataframe_label, "total_grams"] = ingredient_dataframe.at[dataframe_label, "total_grams"] + mass_of_ingredient

    #Update running calories and index
    calories = calories + list_of_recipes[i]["recipe_calories"]
    i = i + 1

  return ingredient_dataframe

#GROWTH PAGE FUNCTIONS#
#----------------------#

#Calculates the monthly and yearly number of plants needed and adds those columns to a dataframe.
#@param ingredient_dataframe: a Pandas dataframe created from ingredients.json
#@return: a Pandas dataframe with the monthly and yearly number of plants added
def calc_number_of_plants_per_ingred(ingredient_dataframe):

  ingredient_dataframe['no_of_plants'] = ingredient_dataframe['total_grams'] / ingredient_dataframe['grams_yield_per_plant']

  #12.166 due to 30-day "months"
  ingredient_dataframe['yearly_no_of_plants'] = 12.166 * ingredient_dataframe['no_of_plants']

  ingredient_dataframe['yearly_no_of_plants'] = ingredient_dataframe['yearly_no_of_plants'].apply(math.ceil)

  return ingredient_dataframe

#Calculates the monthly and yearly grow area needed and adds those columns to a dataframe.
#@param ingredient_dataframe: a Pandas dataframe created from ingredients.json
#@return: a Pandas dataframe with the monthly and yearly grow area added
def calc_grow_area_per_ingred(ingredient_dataframe):

    ingredient_dataframe['grow_area_sq_meters'] = ingredient_dataframe['no_of_plants'] / ingredient_dataframe['plants_per_square_meter']

    ingredient_dataframe['yearly_grow_area'] = 12.166 * ingredient_dataframe['grow_area_sq_meters']

    ingredient_dataframe['yearly_grow_area'] = ingredient_dataframe['yearly_grow_area'].apply(math.ceil)

    return ingredient_dataframe

#Color array used for drawing the garden plot
color_array = ['#FF6633', '#FFB399', '#FF33FF', '#FFFF99', '#00B3E6',
		  '#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D',
		  '#80B300', '#809900', '#E6B3B3', '#6680B3', '#66991A',
		  '#FF99E6', '#CCFF1A', '#FF1A66', '#E6331A', '#33FFCC',
		  '#66994D', '#B366CC', '#4D8000', '#B33300', '#CC80CC',
		  '#66664D', '#991AFF', '#E666FF', '#4DB3FF', '#1AB399',
		  '#E666B3', '#33991A', '#CC9999', '#B3B31A', '#00E680',
		  '#4D8066', '#809980', '#E6FF80', '#1AFF33', '#999933',
		  '#FF3380', '#CCCC00', '#66E64D', '#4D80CC', '#9900B3',
		  '#E64D66', '#4DB380', '#FF4D4D', '#99E6E6', '#6666FF']

#Draws the layout for the garden required to grow the ingredient amounts.
#@param fig: a matplotlib figure returned from plt.subplots()
#@param ax: a matplotlib axes returend from plt.subplots()
#@param ingredient_names: a list of strings of each ingredient whose order corresponds with area_values.
#@param area_values: a list of floats indicating area required for each ingredient, sorted descending.
#@param: row_length_in_m: length of the garden planting rows in meters.
#@param: grow_row_width_in_m: width of the garden planting rows in meters.
#@param: path_width_in_m: width of the walking path between rows in meters.
#@param: color_array: a list of strings whose values correspond to color codes.  If the list of ingredients is longer than the list of colors, the colors will cycle back to the beginning of list.
#@param: fig_width: optional value to set the figure width.
#@return fig, ax: updated figure and axes that shows the garden layout.
def generate_garden_layout(fig, ax, ingredient_names, area_values, row_length_in_m, grow_row_width_in_m, path_width_in_m, color_array, fig_width=15):

  #Calculate total grow area for year
  area_in_sq_meters = sum(area_values)

  #Calculate length of row for entire grow area for a year
  total_grow_length_in_m = area_in_sq_meters / grow_row_width_in_m

  #Calculate how many rows of planting row length (round up)
  no_of_rows = math.ceil(total_grow_length_in_m / row_length_in_m)

  #Total length is number of rows times the row width plus number of rows times path width
  total_plot_length = no_of_rows * grow_row_width_in_m + no_of_rows * path_width_in_m

  #Set the figure area to the dimensions of plot
  ax.set_xlim([0.0, total_plot_length])
  ax.set_ylim([0.0, row_length_in_m])

  #Add the walking path rectangles
  for i in range(1, no_of_rows + 1):
    x_coord = grow_row_width_in_m * (i) + path_width_in_m * (i - 1)
    y_coord = 0.0
    width = path_width_in_m
    height = row_length_in_m
    path = patches.Rectangle((x_coord, y_coord), width, height, linewidth=1, edgecolor='darkgoldenrod', facecolor='darkgoldenrod', fill=True, label="Walking Path")
    ax.add_patch(path)


  #Add the ingredient rows
  #Set initial values for first row
  x_coord = 0.0
  y_coord = 0.0
  row_remaining = row_length_in_m

  #Iterate through ingredients and plot rectangles corresponding to the grow area for each ingredient
  for i in range(0, len(ingredient_names)):

    #Get a total row length for each ingredient
    ingredient_row_length_remaining = area_values[i] / grow_row_width_in_m

    #Keep drawing rectangles until you run out of ingredient
    while ingredient_row_length_remaining > 0:

      #If you don't have enough ingredient to finish a row
      if row_remaining > ingredient_row_length_remaining:

        #Draw a rectangle and update y_coord for next rectangle start point
        rect = patches.Rectangle((x_coord, y_coord), grow_row_width_in_m, ingredient_row_length_remaining, linewidth=1, edgecolor="black", facecolor=color_array[i % len(color_array)], fill=True, label=ingredient_names[i])
        ax.add_patch(rect)
        y_coord = y_coord + ingredient_row_length_remaining

        #Update the amount of row remaining for planting
        row_remaining = row_remaining - ingredient_row_length_remaining

        #Set the remaining length to zero to move on to next ingredient.
        ingredient_row_length_remaining = 0

      #Else you need to start a new row
      elif row_remaining <= ingredient_row_length_remaining:

        #Draw rectangle to fill the rest of the row, update y_coord to zero, x_coord to next row location to start drawing the next row
        rect = patches.Rectangle((x_coord, y_coord), grow_row_width_in_m, row_remaining, linewidth=1, edgecolor="black", facecolor=color_array[i % len(color_array)], fill=True, label=ingredient_names[i])
        ax.add_patch(rect)

        y_coord = 0
        x_coord = x_coord + grow_row_width_in_m + path_width_in_m

        #Take out what you need to finish the current row then update row_remaining for a new row.
        ingredient_row_length_remaining = ingredient_row_length_remaining - row_remaining
        row_remaining = row_length_in_m

  #Gets rid of duplicate legend entries and prepares the plot (1.3, 0.5)
  handles, labels = plt.gca().get_legend_handles_labels()
  by_label = dict(zip(labels, handles))
  plt.legend(by_label.values(), by_label.keys(), bbox_to_anchor = (1.3, 0.5), loc='center right', ncol=2)
  ax.set_title("Garden Layout")
  ax.set_xlabel("Garden Length (meters)")
  ax.set_ylabel("Row Length (meters)")
  plt.tight_layout()
  plt.axis('equal')
  fig.set_figwidth(fig_width)

  return fig, ax

#STORAGE PAGE FUNCTIONS#
#----------------------#

#Calculates the monthly and yearly number of containers and container area/volume needed and adds those columns to a dataframe.
#@param ingredient_dataframe: a Pandas dataframe created from ingredients.json
#@return: a Pandas dataframe with the monthly and yearly number of containers and container area/volume added
def calc_number_of_containers_per_ingred(ingredient_dataframe):

 #Calculate number of containers for each ingredient
 ingredient_dataframe['no_of_containers'] = ingredient_dataframe['total_grams'] / ingredient_dataframe['grams_per_container']

 #Checks if storage type is a jar and calculates the total storage area for the number of jars of the ingredient.
 ingredient_dataframe.loc[ingredient_dataframe['storage'] == '16oz jar', 'container_area'] = ingredient_dataframe['no_of_containers'] / ingredient_dataframe['containers_per_square_meter']
 ingredient_dataframe.loc[ingredient_dataframe['storage'] != '16oz jar', 'container_area'] = 0.0

 #Checks if storage type is a gallon bag and calculates the total storage volume for the number of bags of that ingredient.
 ingredient_dataframe.loc[ingredient_dataframe['storage'] == '1 gal bag', 'container_volume'] = ingredient_dataframe['no_of_containers'] / ingredient_dataframe['containers_per_cubic_meter']
 ingredient_dataframe.loc[ingredient_dataframe['storage'] != '1 gal bag', 'container_volume'] = 0.0

 ingredient_dataframe['yearly_no_of_containers'] = 12.166 * ingredient_dataframe['no_of_containers']

 ingredient_dataframe['yearly_no_of_containers'] = ingredient_dataframe['yearly_no_of_containers'].apply(math.ceil)

 ingredient_dataframe['yearly_container_area'] = 12.166 * ingredient_dataframe['container_area']

 ingredient_dataframe['yearly_container_volume'] = 12.166 * ingredient_dataframe['container_volume']

 return ingredient_dataframe

#NUTRITION PAGE FUNCTIONS#
#----------------------#

#Calculates the monthly calories, carbohydrates, proteins, and fats obtained from eating ingredients and adds those columns to a dataframe.
#@param ingredient_dataframe: a Pandas dataframe created from ingredients.json
#@return: a Pandas dataframe with the monthly and yearly calories, carbohydrates, proteins, and fats added
def calc_nutrition_per_ingred(ingredient_dataframe):

 ingredient_dataframe['total_carbs'] = ingredient_dataframe['total_grams'] * ingredient_dataframe['carb_percentage']

 ingredient_dataframe['total_protein'] = ingredient_dataframe['total_grams'] * ingredient_dataframe['protein_percentage']

 ingredient_dataframe['total_fat'] = ingredient_dataframe['total_grams'] * ingredient_dataframe['fat_percentage']

 ingredient_dataframe['total_calories'] = ingredient_dataframe['total_grams'] * ingredient_dataframe['calories_per_gram']

 return ingredient_dataframe

#RECIPE PAGE FUNCTIONS#
#----------------------#

#Builds an html table from a list of recipes.
#@param recipe_list: a list of recipe dictionaries created from recipes.json
#@return: an string that represents the table in html.
def generate_recipe_table(recipe_list):

   htmlString = ""

   #Iterate through recipes and create a table for each one
   for i in range(0, len(recipe_list)):
     recipe = recipe_list[i]
     recipe_string = "<table>\n"

     #First Row
     recipe_string = recipe_string + "<tr>\n"
     recipe_string = recipe_string + "<th style=\"width:100px\" align=\"left\">Recipe Name: </th>\n"
     recipe_string = recipe_string + "<th style=\"width:600px\" align=\"left\">" + recipe["name"] + "</th>\n"
     recipe_string = recipe_string + "</tr>\n"

     #Second Row
     recipe_string = recipe_string + "<tr>\n"
     recipe_string = recipe_string + "<th align=\"left\">Recipe Calories: </th>\n"
     recipe_string = recipe_string + "<td>" + str(recipe["recipe_calories"]) + "</td>\n"
     recipe_string = recipe_string + "</tr>\n"

     #Third Row
     recipe_string = recipe_string + "<tr>\n"
     recipe_string = recipe_string + "<th align=\"left\">Recipe Source: </th>\n"
     recipe_string = recipe_string + "<td>" + "<a href=" + recipe["source"] + ">" + "<div style=\"height:100%;width:100%\">" + recipe["source"] + "</div>" + "</a>" + "</td>\n"
     recipe_string = recipe_string + "</tr>\n"

     #Ingredients Section
     recipe_string = recipe_string + "<tr>\n"
     recipe_string = recipe_string + "<th align=\"left\">Ingredients: </th>\n"
     recipe_string = recipe_string + "</tr>\n"

     ingredient_list = recipe['ingredients_and_amounts_in_milliliters']

     #Iterate through ingredients and put into table
     for i in range(0, len(ingredient_list) - 1, 2):
      recipe_string = recipe_string + "<tr>" + "<td>" + str(ingredient_list[i + 1]) + " mL " + "</td>" + "<td>" + str(ingredient_list[i]) + "</td>" + "</tr>\n"

     #End table
     recipe_string = recipe_string + "</table>\n"
     htmlString = htmlString + recipe_string

   return htmlString