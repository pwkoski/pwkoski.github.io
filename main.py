import pandas as pd
from pyscript import display
import json


with open('ingredients.json') as json_file:


    def df_recursive_create(array_of_dicts):

        df = pd.DataFrame()

        def recursion(dictionary, index):
            #for key, value in dictionary.items():
            #display(print(dictionary.keys()))
            for key in dictionary:
                #display(print(key))
                if type(dictionary[key]) is dict:
                    return recursion(dictionary[key], index)
                else:
                    df.at[index, key] = dictionary[key]

        for i in range(0, len(array_of_dicts)):
            for dictionary in array_of_dicts[i]:
                recursion(array_of_dicts[i][dictionary], i)
            #array_of_dicts[i] is not a dict but a dict of dicts


        return df

#Create dict from json
    recipe_list = json.load(json_file)

#Build dataframe automatically from dict

    df1 = df_recursive_create(recipe_list["ingredients"])

#Display

    display(df1, append=True)









