import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Load the world map data
world = gpd.read_file('New folder\d08cac2fa3f6338d84ea-ebe3d2a4eda405775a860d251974e1f08cbe4f48.zip')

# Load the city data
cities = pd.read_csv(r'New folder\train.csv')
# below we define the specfic points we want to plot X & Y, these are saved in 'geometry
GTA = cities[cities['Descript'] == 'GRAND THEFT FROM LOCKED AUTO']
Robbery = cities[cities['Descript'] == 'ROBBERY ON THE STREET WITH A GUN']
Murder = cities[cities['Descript'] == 'AGGRAVATED ASSAULT WITH A KNIFE']

geometry_GTA = gpd.points_from_xy(GTA['X'], GTA['Y'])
geometry_Rob = gpd.points_from_xy(Robbery['X'], Robbery['Y'])
geometry_kill = gpd.points_from_xy(Murder['X'], Murder['Y'])



#cities_gdf is the saved dataframe with all the points
GTA_gdf = gpd.GeoDataFrame(GTA, geometry=geometry_GTA)
Rob_gdf = gpd.GeoDataFrame(Robbery, geometry=geometry_Rob)
Kill_gdf = gpd.GeoDataFrame(Murder, geometry=geometry_kill)


#sets the boundary for the points on the screen so it dosent go out of bounds
#below is the boundaries of sf in real life. From the east most point to west most point is repped in 0 & 1 
# ****do this below to draw boundaries of yr map ****
sf_extent = (-122.517, -122.355, 37.707, 37.832)
#so these lines make sure to display the dots within the san fran map limit and makes 
#sure it displays the dots in the map and not on a line graph

print(cities['Category'] == 'AGGRAVATED ASSAULT WITH A KNIFE')

fig, ax = plt.subplots(figsize=(10, 5))
# below we plot the map of san fran
world.plot(ax=ax, color='lightgray', alpha=0.5)
#below we define the maximum limtis points can be plotted on the map 
ax.set_xlim(sf_extent[0], sf_extent[1])
ax.set_ylim(sf_extent[2], sf_extent[3])
# here we plot the points of crimes
GTA_gdf.plot(ax=ax, color='blue', markersize=5)
Rob_gdf.plot(ax=ax, color='red', markersize=5)
Kill_gdf.plot(ax=ax, color='green', markersize=5)



plt.xlabel('Longitude')
plt.ylabel('Latitude')
legend_el = [Line2D([0], [0], color='blue', markersize=5, label='Car Thefts in blue')]
legend_el1 = [Line2D([100], [0], color='red', markersize=5, label='Armed Robberys in red')]
legend_el2 = [Line2D([100], [0], color='green', markersize=5, label='Stabbings in green')]

legend_gta=ax.legend(handles=legend_el, loc = 'upper right')
legend_rob=ax.legend(handles=legend_el1, loc = 'upper left')
legend_stab=ax.legend(handles=legend_el2, loc = 'lower right')

#add artists ensures that both legends are displayed and not only the most recent one
ax.add_artist(legend_gta)
ax.add_artist(legend_rob)
ax.add_artist(legend_stab)

plt.title('San Francisco with Crime Points')
plt.show()
