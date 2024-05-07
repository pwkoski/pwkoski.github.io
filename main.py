import pandas as pd
from pyscript import display
import json


with open('ingredients.json') as json_file:
    #Create dict from json
    recipe_list = json.load(json_file)

    #Build dataframe manually from dict

    df2 = pd.DataFrame(columns=['Name',
                                "Growable?",
                                "Price Per Month ($)",
                                "Fresh?",
                                "Composite?",
                                "Ingredient Density (g/mL)",
                                "Grams Yield per Plant (g/plant)",
                                "Planting Density (plants/sq. m)",
                                "Amount per Container (g/container)",
                                "Storage Type",
                                "Container",
                                "Container Area Density (containers/sq. m)",
                                "Container Volume Density (containers/cu. m)",
                                "Protein %",
                                "Carb %",
                                "Fat %",
                                "Caloric Density (kcal/g)"
                                ])


    r = recipe_list["ingredients"]
    for i in range(len(r)):
       recipe = r[i]
       df2.loc[i] = [recipe["info"]["name"],
                     recipe["info"]["growable"],
                     recipe["info"]["price_per_month"],
                     recipe["info"]["fresh"],
                     recipe["info"]["composite"],
                     recipe["info"]["ingredient_grams_per_milliliter"],
                     recipe["growth"]["grams_yield_per_plant"],
                     recipe["growth"]["plants_per_square_meter"],
                     recipe["storage"]["grams_per_container"],
                     recipe["storage"]["storage_type"],
                     recipe["storage"]["storage"],
                     recipe["storage"]["containers_per_square_meter"],
                     recipe["storage"]["containers_per_cubic_meter"],
                     recipe["nutrition"]["protein_percentage"],
                     recipe["nutrition"]["carb_percentage"],
                     recipe["nutrition"]["fat_percentage"],
                     recipe["nutrition"]["calories_per_gram"]
                     ]

    #Display
    display(df2, append=True)







