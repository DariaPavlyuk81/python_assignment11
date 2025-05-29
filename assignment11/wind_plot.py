#Task3

import plotly.express as px
import plotly.data as pldata
import pandas as pd


df = pldata.wind(return_type='pandas')

#  the first and last 10 lines
print("First 10 rows:\n", df.head(10))
print("\nLast 10 rows:\n", df.tail(10))

# Clean the 'strength' 
df['strength'] = df['strength'].str.extract(r'(\d+\.?\d*)').astype(float)

# interactive scatter plot
fig = px.scatter(df, 
                 x='frequency', 
                 y='strength', 
                 color='direction',
                 title='Wind Strength vs Frequency by Direction',
                 labels={'strength': 'Wind Strength', 'frequency': 'Frequency'},
                 hover_data=['direction'])

fig.write_html("wind.html")
