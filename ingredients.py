import pandas as pd
from pyscript import display
import js

#Import
#Gets item from storage as a JSON in string format.
data = js.sessionStorage.getItem("df")

#Convert
df1 = pd.read_json(data)
display(df1, append=True)
