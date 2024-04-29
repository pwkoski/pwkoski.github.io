import pandas as pd
from pyscript import display
import json
import os


display(os.getcwd())
display(os.listdir())


df = pd.read_json('recipes.json')

display(df, append=False)
#display(df2, append=True)



