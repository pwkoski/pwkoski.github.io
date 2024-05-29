import pandas as pd
from pyscript import document
import js
import functions

#Import
#Gets item from storage as a JSON in string format.
data = js.sessionStorage.getItem("df")

#Convert to dataframe
df = pd.read_json(data)

#Perform calculations
df = functions.calc_number_of_containers_per_ingred(df)


#Create summary table
#Group entries by storage type and sum columns
grouped_df = df.groupby('storage').sum(numeric_only=True)

df_display1 = grouped_df[['yearly_no_of_containers', 'yearly_container_area', 'yearly_container_volume' ]]
df_display1.index.names = ['Container Type']
df_display1 = df_display1.rename(columns={'yearly_no_of_containers': 'Yearly Number of Containers', 'yearly_container_area': "Area for Storage (sq. m)", 'yearly_container_volume': "Volume for Storage (cu. m)" })

#Display summary table as HTML table
df_html1 = df_display1.to_html()
htmlObject1 = document.querySelector("#my_table1")
htmlObject1.innerHTML = df_html1


#Create individual table
df_display2 = df[['name', 'yearly_no_of_containers', 'storage_type', 'storage', 'yearly_container_area', 'yearly_container_volume' ]]
df_display2 = df_display2.rename(columns={'name': 'Ingredient Name', 'yearly_no_of_containers': 'Yearly Number of Containers', "storage_type": "Dry/Frozen Storage", 'storage': "Container Type", 'yearly_container_area': "Area for Storage (sq. m)", 'yearly_container_volume': "Volume for Storage (cu. m)" })

#Display individual table as HTML table
df_html2 = df_display2.to_html(index_names=False, index=False)
htmlObject2 = document.querySelector("#my_table2")
htmlObject2.innerHTML = df_html2