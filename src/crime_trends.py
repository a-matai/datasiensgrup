import pandas as pd
import matplotlib as plt

df = pd.read_csv("../clean_data.csv")
print("Finished reading csv")

groups = df.groupby(["Year", "Month"]).size()
ax = groups.plot()
fig = ax.get_figure()
fig.savefig('test.png')
