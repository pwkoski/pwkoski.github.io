import pandas as pd
from pyscript import display
import js
import matplotlib.pyplot as plt
import functions

#Import
#Gets item from storage as a JSON in string format.
data = js.sessionStorage.getItem("df")

#Convert to dataframe
df = pd.read_json(data)

#Perform calculations
df = functions.calc_nutrition_per_ingred(df)

monthly_carbs = df['total_carbs'].sum()
monthly_protein = df['total_protein'].sum()
monthly_fat = df['total_fat'].sum()
monthly_calories = df['total_calories'].sum()

#Calculate desired macros
monthly_caloric_limit = 60000
x = ['Carbs', 'Protein', 'Fat']
desired = [0.5 * monthly_caloric_limit, 0.3 * monthly_caloric_limit, 0.2 * monthly_caloric_limit]
actual = [monthly_carbs, monthly_protein, monthly_fat]

#Set up plots
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Nutritional Information for One Month Period')
fig.set_figwidth(10)
ax1.bar("Calories", monthly_caloric_limit, color='grey', label="Desired")
ax1.bar("Calories", monthly_calories, color='red', label="Actual")
ax1.set_ylabel("Calories")
ax2.bar(x, desired, color='grey', label="Desired")
ax2.bar(x, actual, color='red', label="Actual")
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")
ax2.set_ylabel("Grams")
ax2.legend()

#Display data
display(fig, target="pythontable")