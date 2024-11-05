import geopandas as gpd
import matplotlib.pyplot as plt



# geopandas works with vector data files (e.g., Shapefiles, GeoJSON, or other GIS-compatible formats
world = gpd.read_file('libraries\\ne_110m_admin_0_countries.shp')


world.plot (edgecolor='red', color='lightblue')
plt.title('world map with borders')
plt.show() 