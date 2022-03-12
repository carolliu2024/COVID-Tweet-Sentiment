# %%
import matplotlib.pyplot as plt
import geopandas
import pandas as pd

# %%
# Read shapefile from disk. Returns GeoDataFrame object
states = geopandas.read_file('data/usa-states-census-2014.shp') # Create map outline, no data
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
# Load sample dataset (Confirmed Covid Cases by state as of 3/10/22)
from geopandas import GeoDataFrame

df = pd.read_excel('cases_example\covid_confirmed_usafacts.xlsx', sheet_name="total_cases")
#df = pd.read_excel('covid_confirmed_usafacts.xlsx')
df.head()

# %%
# Cleaning and joining dataframes
map_data = df.rename(index=str, columns={"Row Labels": "State Abbreviation",
                                         "Sum of 3/10/2022":"Total Covid Cases"})
map_data.head()

# %% Merge states Geodata with dataset
merged = states.set_index('STUSPS').join(map_data.set_index('State Abbreviation'))
merged.head()

# %% Matplotlib prep work for Mapping

#  Set variable to map
var = 'Total Covid Cases'

# Set chloropleth range
vmin, vmax = 1000000, 20000000 #UNUSED

# Create figure, axes for map to be drawn in
#fig = plt.subplots(1, figsize = (10, 6))

#%% Create Map
merged.explore(column = var,
               cmap = 'plasma', 
               scheme = 'EqualInterval') 
# ax.set_title('Total Covid Cases as of 3/10/22')

# %%
# Messy Colorbar labels 
merged.explore(column = var,
               cmap = 'plasma')

# %%
