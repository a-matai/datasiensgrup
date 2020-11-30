import pandas as pd

df = pd.read_csv("Crimes_-_2001_to_Present.csv", na_values = " ")
#delete rows that have a missing Community Area value
list = df[df['Community Area'].isnull()].index.tolist()
df.drop(list,inplace = True)
df.index = range(len(df))


#split the date-time into date and time
date = df["Date"].str.split(" ", n = 1, expand = True)
#split date into month day year
date_spec = date[0].str.split("/", n = 2, expand = True)
df["Month"] = date_spec[0]
df["Day"] = date_spec[1]
df["Time"] = date[1]

df.to_csv("clean_data.csv")
