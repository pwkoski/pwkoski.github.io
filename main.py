import pandas as pd
from pyscript import display
import json
import js
import matplotlib.pyplot as plt

#%matplotlib inline

with open('ingredients.json') as json_file:

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

#Create dict from json
    ingredient_list = json.load(json_file)

#Build dataframe from dict
    df1 = df_recursive_create(ingredient_list["ingredients"])

#Plot a column of data
    df1.plot.barh(x="name", y="calories_per_gram", figsize=(30, 5))
    plt.show()


#Export
    jsonDf = df1.to_json()
    js.sessionStorage.setItem("df", jsonDf)