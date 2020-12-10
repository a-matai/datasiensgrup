import pandas as pd

# NB: You have to have the Crimes dataset in your data folder already.
# download from: https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/data?fbclid=IwAR0bFz89WTpotKU6dbm6VIudWC3kb5jm0s8uNKGMrLXnkq-0tLO68pmg40c


df = pd.read_csv("../data/Crimes_-_2001_to_Present.csv", na_values = " ", low_memory=False)

#Remove data before 2010
list = df[df['Year'] < 2010].index.tolist()
df.drop(list, inplace = True)
df.index = range(len(df))

#Delete rows that have a missing Community Area value
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
df["Date"] = date[0]


#add a crime label column using https://www.justia.com/criminal/offenses/ categories
property_crimes = "BURGLARY|THEFT|LARCENY|ROBBERY|SHOPLIFTING|PROPERTY|DAMAGE"
personal_crimes = "ASSAULT|BATTERY|ARSON|ABUSE|KIDNAPPING|RAPE|SEX|CHILDREN|HOMICIDE|MURDER"
financial_crimes = "FRAUD|DECEPTIVE PRACTICE|TAX|BLACKMAIL"
statutory_crimes = "NARCOTIC|ALCOHOL|DRUG|WEAPONS"

df["type"] = "Other"

mask = df['Primary Type'].str.contains(property_crimes)
df.loc[mask, 'type'] = "PROPERTY"

mask = df['Primary Type'].str.contains(personal_crimes)
df.loc[mask, 'type'] = "PERSONAL"

mask = df['Primary Type'].str.contains(financial_crimes)
df.loc[mask, 'type'] = "FINANCIAL"

mask = df['Primary Type'].str.contains(statutory_crimes)
df.loc[mask, 'type'] = "STATUTORY"

df.to_csv("../data/clean_data.csv")
