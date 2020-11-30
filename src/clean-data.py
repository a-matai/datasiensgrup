import pandas as pd

# NB: You have to have the Crimes dataset in your data folder already.
# download from: https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/data?fbclid=IwAR0bFz89WTpotKU6dbm6VIudWC3kb5jm0s8uNKGMrLXnkq-0tLO68pmg40c


df = pd.read_csv("../data/Crimes_-_2001_to_Present.csv", na_values = " ")
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

df.to_csv("../data/clean_data.csv")
