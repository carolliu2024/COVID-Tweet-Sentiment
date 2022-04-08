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

df = pd.read_excel('data\Sentiment-19_State_Data.xlsx')
#df = pd.read_excel('covid_confirmed_usafacts.xlsx')
df.head()

# %%
# Renaming files
map_data = states.rename(index=str, columns={"NAME": "Name"})
map_data.head() # Check renaming worked

# %% Merge states Geodata with dataset
#merged = states.set_index('NAME').join(df.set_index('State'))

merged = map_data.join(df.set_index('State'), on='Name')
#merged = states.set_index('Name').join(df.set_index('State'))
merged.head()

# %% Matplotlib prep work for Mapping

#  Set variables to map

# Dominant emotions: Happy, angry, surprise, sad, fear
# Get states with dominant emotion as happy,angry,etc
happy = merged[merged['Dominant Emotion'] == 'Happy'] 
angry = merged[merged['Dominant Emotion'] == 'Angry']
surprise = merged[merged['Dominant Emotion'] == 'Surprise']
sad = merged[merged['Dominant Emotion'] == 'Sad']
fear = merged[merged['Dominant Emotion'] == 'Fear']

#%% Create Map

# Display dominant emotion too?
merged.explore(tooltip=['Name',
                        'Happy', 
                        'Angry', 
                        'Surprise', 
                        'Sad', 
                        'Fear'])

senti_map = merged.explore(tooltip=['Name',
                                    'Happy', 
                                    'Angry', 
                                    'Surprise', 
                                    'Sad', 
                                    'Fear'],
                         style_kwds = dict(fill=False))
# merged.explore(column = var,
#                cmap = 'plasma', 
#                scheme = 'EqualInterval') 

# %%
sad.explore(column = 'Sad', 
            cmap = 'Blues', 
            m = senti_map,
            tooltip=['Name',
                    'Happy', 
                    'Angry', 
                    'Surprise', 
                    'Sad', 
                    'Fear'],
            scheme='BoxPlot')
fear.explore(column = 'Fear', 
            cmap = 'Reds', 
            m = senti_map,
            tooltip=['Name',
                    'Happy', 
                    'Angry', 
                    'Surprise', 
                    'Sad', 
                    'Fear'],
            scheme='BoxPlot')
                    
surprise.explore(column = 'Surprise', 
            cmap = 'Greens', 
            m = senti_map,
            tooltip=['Name',
                    'Happy', 
                    'Angry', 
                    'Surprise', 
                    'Sad', 
                    'Fear'],
            scheme='BoxPlot')

# %%
senti_map.save('senti_map.html')
# %%
