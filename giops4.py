
#. ssmuse-sh -p eccc/crd/ccmr/EC-CAS/master/fstd2nc-deps_20170918

import os
from ftplib import FTP
import glob
import netCDF4 as nc
import datetime
from scipy.interpolate import interp1d
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import ntpath

filename='2018082812_240'
fh = nc.Dataset('2018082812_240_2D_ps5km60N.nc')
lons = fh.variables['longitude'][:]
lats = fh.variables['latitude'][:]
temp= fh.variables['votemper'][:]
fh.close()


# Get some parameters for the Stereographic Projection
lon_0 = lons.mean()
lat_0 = lats.mean()

#width=6000000,height=4500000,#lat_ts=40,lat_0=70,lon_0=270)

m = Basemap(projection='npstere', boundinglat=66,lon_0=273,resolution='l')         

# Because our lon and lat variables are 1D,
# use meshgrid to create 2D arrays
# Not necessary if coordinates are already in 2D arrays.
# lon, lat = np.meshgrid(lons, lats)
xi, yi = m(lons, lats)

fig=plt.figure(figsize=(10,10))

# Plot Data
#cs = m.pcolor(xi,yi,(np.squeeze(temp)-273),  vmin=-2, vmax=26)
m.drawcoastlines()
m.drawstates()
m.drawcountries()
m.fillcontinents(color='grey')

# Add Grid Lines
m.drawparallels(np.arange(-80., 81., 5.), labels=[1,0,0,0], fontsize=10)
m.drawmeridians(np.arange(-180., 181., 10.), labels=[0,0,0,1], fontsize=10)



#plt.title("Sea Surface Temperature: %s" % (filename),  fontsize=16)
plt.title("Sea Surface (0.5 m) 2018-08-28 00:00 UTC",  fontsize=16)

contours = m.contourf(xi,yi,(np.squeeze(temp)-273), levels=np.linspace(-2,26,26))#, colors='black'
#m.clabel(contours, inline=True, fontsize=8)
cbar = m.colorbar(contours, location='right',ticks=[-2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24,  26])
cbar.set_label('Temperature $(^{o}C)$', rotation=270, labelpad=40, y=0.45, fontsize=16)

plt.show()

#matplotlib.pyplot.savefig('giops_ac_240.png')

fig.savefig('giops_ac_240.png')
plt.close(fig) 

#origin = np.datetime64('0000-01-01', 'D') - np.timedelta64(1, 'D')
#date = serdate * np.timedelta64(1, 'D') + origin
