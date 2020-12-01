import scipy.stats as st
import numpy as np
import pandas as pd
from arcgis.geocoding import reverse_geocode
from arcgis.geometry import Geometry
from arcgis.gis import GIS

#import lstop data
parks = pd.read_csv('../data/CPD_Parks.csv', delimiter=',', quotechar='"')
print(parks.head())

#import ca to zip data and  rename columns
ca_to_zip = pd.read_csv('../data/ca_zip.csv',header=None)
ca_to_zip = ca_to_zip.drop(ca_to_zip.index[0])
ca_to_zip.columns = ["Community Area", "ZIP", "Pop2010"]
ca_to_zip['ZIP'] = ca_to_zip['ZIP'].apply(lambda z : float(z))


#merge based on ca_to_zip
parks = parks.merge(ca_to_zip, left_on="ZIP", right_on="ZIP")
parks['ZIP'] = parks['ZIP'].apply(lambda z : int(z))
print(parks.head())
#output csv
parks.to_csv("../data/parks_localized.csv",index=False)