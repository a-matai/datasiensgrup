import scipy.stats as st
import numpy as np
import pandas as pd
from arcgis.geocoding import reverse_geocode
from arcgis.geometry import Geometry
from arcgis.gis import GIS

'''
# Now we will make the crime dataframe.
print(crime.columns)
crime1 = crime.filter(['Month','Year',''])
Index(['Unnamed: 0', 'ID', 'Case Number', 'Date', 'Block', 'IUCR',
       'Primary Type', 'Description', 'Location Description', 'Arrest',
       'Domestic', 'Beat', 'District', 'Ward', 'Community Area', 'FBI Code',
       'X Coordinate', 'Y Coordinate', 'Year', 'Updated On', 'Latitude',
       'Longitude', 'Location', 'Month', 'Day', 'Time'],
      dtype='object')
'''
#import lstop data
crime = pd.read_csv('../data/clean_data.csv', delimiter=',', quotechar='"')

print(crime.head())

#check column
lstops["Location"] = lstops["Location"].str.replace("(","") 
lstops["Location"] = lstops["Location"].str.replace(")","") 
lat_list = []
lon_list = []
for each in lstops["Location"]:
    x = each.split(",")
    lat = float(x[0])
    lon = float(x[1])
    lat_list.append(lat)
    lon_list.append(lon)

lstops["Lat"] = lat_list
lstops["Lon"] = lon_list

# 0        Location         |   Lat   |    Lon
# 1  41.857908, -87.669147  41.857908 -87.669147  

#import ca to zip data
ca_to_zip = pd.read_csv('../data/ca_zip.csv',header=None)

ca_to_zip = ca_to_zip.drop(ca_to_zip.index[0])

ca_to_zip.columns = ["Community Area", "Zipcode", "Pop2010"]

#adapted from:
#https://gis.stackexchange.com/questions/352961/convert-lat-lon-to-zip-postal-code-using-python?
#fbclid=IwAR25An6-uDiY1Lpy5EVPUG15RcrRKj5fL1M86Bt3Svqy_iVRi1YLLfviRT0
df = lstops

gis = GIS()

def get_zip(df, lon_field, lat_field):
    location = reverse_geocode((Geometry({"x":float(df[lon_field]), "y":float(df[lat_field]), "spatialReference":{"wkid": 4326}})))
    return location['address']['Postal']

#apply zipcodes
lstops["zips"] = df.apply(get_zip, axis=1, lat_field='Lat', lon_field='Lon')
#merge based on ca_to_zip
lstops = lstops.merge(ca_to_zip, left_on="zips", right_on="Zipcode")
#output csv
lstops.to_csv("../data/lstops_localized.csv",index=False)