# %%
import matplotlib.pyplot as plt
import geopandas
import pandas as pd

# %%
# Read shapefile from disk. Returns GeoDataFrame object
states = geopandas.read_file('data/usa-states-census-2014.shp')
type(states) # Check GeoDataFrame object

# %%
# Display first few lines of dataset
states.head() 

# %%
# Display CRS of shapefile (WGS 84)
states.crs
# Mercator projection (EPSG:3395) is the standard for Web mapping apps
states = states.to_crs("EPSG:3395")

# %%
# Plotting Shapefiles
states.explore()

# %%
# Plotting sample dataset
from geopandas import GeoDataFrame
#from geopandas import points_from_xy
from shapely.geometry import Point, Polygon

df = pd.read_csv('simplemaps_uscities_basicv1.74\\uscities.csv')

# Convert lat,long to x,y
#geometry = points_from_xy(df['lat'],df['lng'])

# point = [Point((41,-87))]
# point_df = GeoDataFrame()

geometry = [Point(xy) for xy in zip(df['lng'], df['lat'])]
# geomtry_lat = [i for i in geometry[0]]
# geometry_long = [j for j in geometry[1]]
geo_df = GeoDataFrame(df, 
                      crs = "EPSG:4326",
                      geometry = geometry)
geo_df.head()



""" # Pandas dataframe -> GeoDataFrame
df2 = GeoDataFrame(df, geometry=geometry)
df2.head() """


# %%

#statemap = states.explore()
# df2.set_crs("EPSG:3395")
# df2.explore(m = statemap,
#             column = 'density')

#geo_df.explore(m = statemap, column = 'density')
#states.explore()
#geo_df[geo_df['density']].explore()
#fix, ax = plt.subplots(figsize = (15, 15))
#states.plot(ax = ax)
#geo_df[geo_df['density'] > 10000].plot(ax = ax)


# %%
#states.explore()
statemap = states.explore()
geo_df[geo_df['density']>1000].explore(m = statemap, color = 'green')

# %%
