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