# %%
import antigravity
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

df = pd.read_excel('data\Sentiment-19_State_Data.xlsx')
#df = pd.read_excel('covid_confirmed_usafacts.xlsx')
df.head()

# %% Merge states Geodata with dataset
merged = states.set_index('NAME').join(df.set_index('State'))
merged.head()

# %% Matplotlib prep work for Mapping

#  Set variables to map

# Dominant emotions: Happy, angry, surprise, sad, fear
happy = merged[merged['Dominant Emotion'] == 'Happy']
angry = merged[merged['Dominant Emotion'] == 'Angry']
surprise = merged[merged['Dominant Emotion'] == 'Surprise']
sad = merged[merged['Dominant Emotion'] == 'Sad']
fear = merged[merged['Dominant Emotion'] == 'Fear']

#%% Create Map

sent_map = merged.explore()

# merged.explore(column = var,
#                cmap = 'plasma', 
#                scheme = 'EqualInterval') 
# ax.set_title('Total Covid Cases as of 3/10/22')

# %%
# Messy Colorbar labels 
# merged.explore(column = var,
#                cmap = 'plasma')

# %%
