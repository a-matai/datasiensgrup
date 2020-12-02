import pandas as pd
import matplotlib as plt

df = pd.read_csv("../clean_data.csv")
print("Finished reading csv")

#Remove 2001
list = df[df['Year'] == 2001].index.tolist()
df.drop(list, inplace = False)

#Graph the general trend
groups = df.groupby(["Year", "Month"]).size()
ax = groups.plot()
fig = ax.get_figure()
fig.savefig('test.png')
