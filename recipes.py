import pandas as pd
from pyscript import document
import js
import json
import functions

#Import
#Gets item from storage and convert to dict.
recipe_list = js.sessionStorage.getItem("recipe_list")
json_acceptable_string = recipe_list.replace("'", "\"")
recipe_dict = json.loads(json_acceptable_string)

#Generate recipe table HTML
table_html = functions.generate_recipe_table(recipe_dict['recipes'])

#Display as HTML table
htmlObject = document.querySelector("#recipes")
htmlObject.innerHTML = table_html