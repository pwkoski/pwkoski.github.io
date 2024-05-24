import pandas as pd
from pyscript import display, document
import js

#Import
#Gets item from storage as a JSON in string format.
data = js.sessionStorage.getItem("df")

#Convert
df1 = pd.read_json(data)

#Display as HTML table
df_html = df1.to_html(index_names=False,index=False)
htmlObject = document.querySelector("#pythontable")
htmlObject.innerHTML = df_html


#display(df1, append=True)
