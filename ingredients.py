import pandas as pd
from pyscript import document
import js

#Import
#Gets item from storage as a JSON in string format.
data = js.sessionStorage.getItem("df")

#Convert
df = pd.read_json(data)

#Display as HTML table
df_html = df.to_html(index_names=False,index=False)
htmlObject = document.querySelector("#pythontable")
htmlObject.innerHTML = df_html