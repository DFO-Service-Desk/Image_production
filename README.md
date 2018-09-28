# Image_production
Mapping of data


# CONCEPTS website

Images production for CONCEPTS website

## Data input

GIOPS Daily Images: average of the first 24 hrs of forecast [0-24]

GIOPS 10d forecast: daily average for the 10 days of forecast [0-24, 24-48, 48-72…]
 
Animations are produced using the 10 plots from the GIOPS 10d forecast

## Regions

Arctic zoom coordinates:

[66.854593725666, -127.31241594006615], [67.27130760980332, -54.83951460589132], [67.63068535797869, 53.47604143072642], [67.43513534183177, 129.00978351534692]
 
Atlantic:

[39.92459761658699, -74.89700973033904], [40.05926969760134, -19.525915980339025], [71.30700407995491, -20.404822230339036], [71.13725323231671, -75.95169723033902]
 
Pacific:

[61.782285969603606, -159.43181574344632], [47.23272693335352, -159.60759699344632], [47.23272693335352, -121.63884699344632], [61.823814620677126, -122.07830011844631]
 
## Data output
	
Variable format : input--NetCDF, output--.png

Model Depth : 0, sub-surface (-15 ou 50 meters)
	
variables : Temperature, currents, salinity, Ice concentration (only Arctic and Atlanctic)

Regions : Arctic, Atlantic, Pacific,
	
![map setting (left bar)](https://github.com/DFO-Service-Desk/Image_production/blob/master/giops_ac_temp_240.png "Map Example")  

![map setting (left bar)](https://github.com/DFO-Service-Desk/Image_production/blob/master/giops_ac_salinity_240.png "Map Example")  

![map setting (left bar)](https://github.com/DFO-Service-Desk/Image_production/blob/master/giops_ac_icefraction_240.png "Map Example")  

