from arcgis.geocoding import reverse_geocode
from arcgis.geometry import Geometry
from arcgis.gis import GIS
import pandas as pd


df = pd.DataFrame({
    'Lat': [41.864712],
    'Lon': [-87.65882]

def coord_to_zip(df) :
    gis = GIS()

    def get_zip(df, lon_field, lat_field):
        location = reverse_geocode((Geometry({"x":float(df[lon_field]), "y":float(df[lat_field]), "spatialReference":{"wkid": 4326}})))
        return location['address']['Postal']

    })

    zipcodes = df.apply(get_zip, axis=1, lat_field='Lat', lon_field='Lon')
    return zipcodes

coord_to_zip(df)
'''
adapted from:
https://gis.stackexchange.com/questions/352961/convert-lat-lon-to-zip-postal-code-using-python?
fbclid=IwAR25An6-uDiY1Lpy5EVPUG15RcrRKj5fL1M86Bt3Svqy_iVRi1YLLfviRT0
'''