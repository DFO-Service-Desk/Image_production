# 2018/09/27
# corinne.bourgault-brunelle@dfo-mpo.gc.ca
# Ouvrir un fichier de forecasts et créer les cartes par régions et par variables

# . ssmuse-sh -p eccc/crd/ccmr/EC-CAS/master/fstd2nc-deps_20170918 (old)
# . ssmuse-sh -p eccc/crd/ccmr/EC-CAS/master/fstd2nc_0.20180821.0 (new)

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


# Netcdf GIOPS data :
# /space/hall2/sitestore/eccc/cmod/prod/hubs/suites/ops/gdps/g1/netcdf/prog/glboce
# utc_now = datetime.utcnow()
filename='2018082812_240'
fh = nc.Dataset('2018082812_240_2D_ps5km60N.nc')
lons = fh.variables['longitude'][:]
lats = fh.variables['latitude'][:]
temp= fh.variables['votemper'][:]
salinity= fh.variables['vosaline'][:]
iceconcentration= fh.variables['iiceconc'][:]
fh.close()



# ARCTIC REGION

# TEMPERATURE
fig=plt.figure(figsize=(10,10))
m = Basemap(projection='npstere', boundinglat=66,lon_0=273,resolution='l')         
xi, yi = m(lons, lats)
m.drawcoastlines()
m.drawstates()
m.drawcountries()
m.fillcontinents(color='grey')

# Add Grid Lines
m.drawparallels(np.arange(-80., 81., 5.), labels=[1,0,0,0], fontsize=10)
m.drawmeridians(np.arange(-180., 181., 10.), labels=[0,0,0,1], fontsize=10)

#plt.title("Sea Surface Temperature: %s" % (filename),  fontsize=16)
plt.title("Sea Surface (0.5 m) 2018-08-28 00:00 UTC",  fontsize=16)
contours = m.contourf(xi,yi,(np.squeeze(temp)-273), levels=np.linspace(-2,26,28))#, colors='black', m.clabel(contours, inline=True, fontsize=8)
cbar = m.colorbar(contours, location='right',ticks=[-2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24,  26])
cbar.set_label('Temperature $(^{o}C)$', rotation=270, labelpad=30, y=0.45, fontsize=16)

plt.show()
fig.savefig('giops_ac_temp_240.png')
plt.close(fig) 


# SALINTIY
fig=plt.figure(figsize=(10,10))
m = Basemap(projection='npstere', boundinglat=66,lon_0=273,resolution='l')         
xi, yi = m(lons, lats)
m.drawcoastlines()
m.drawstates()
m.drawcountries()
m.fillcontinents(color='grey')

# Add Grid Lines
m.drawparallels(np.arange(-80., 81., 5.), labels=[1,0,0,0], fontsize=10)
m.drawmeridians(np.arange(-180., 181., 10.), labels=[0,0,0,1], fontsize=10)

#plt.title("Sea Surface Temperature: %s" % (filename),  fontsize=16)
plt.title("Sea Surface (0.5 m) 2018-08-28 00:00 UTC",  fontsize=16)
contours = m.contourf(xi,yi,(np.squeeze(salinity)), levels=np.linspace(0,38,28))#, colors='black', m.clabel(contours, inline=True, fontsize=8)
cbar = m.colorbar(contours, location='right',ticks=[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])
cbar.set_label('Salinity $(PSU)$', rotation=270, labelpad=30, y=0.45, fontsize=16)

plt.show()
fig.savefig('giops_ac_salinity_240.png')
plt.close(fig) 

# ICECONCENTRATION
fig=plt.figure(figsize=(10,10))
m = Basemap(projection='npstere', boundinglat=66,lon_0=273,resolution='l')         
xi, yi = m(lons, lats)
m.drawcoastlines()
m.drawstates()
m.drawcountries()
m.fillcontinents(color='grey')

# Add Grid Lines
m.drawparallels(np.arange(-80., 81., 5.), labels=[1,0,0,0], fontsize=10)
m.drawmeridians(np.arange(-180., 181., 10.), labels=[0,0,0,1], fontsize=10)

# plt.title("Sea Surface Temperature: %s" % (filename),  fontsize=16)
plt.title("Sea Surface (0.5 m) 2018-08-28 00:00 UTC",  fontsize=16)
contours = m.contourf(xi,yi,(np.squeeze(iceconcentration)), levels=np.linspace(0,1,20))#, colors='black', m.clabel(contours, inline=True, fontsize=8)
cbar = m.colorbar(contours, location='right',ticks=[0,0.05,  0.1, 0.15, 0.2, 0.25, 0.3,  0.35,  0.4,0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75,  0.8, 0.85, 0.9, 0.95, 1])
cbar.set_label('Ice fraction', rotation=270, labelpad=30, y=0.45, fontsize=16)

plt.show()
fig.savefig('giops_ac_icefraction_240.png')
plt.close(fig) 



#from PIL import Image
#img = Image.open('/path/to/file', 'r')
#img_w, img_h = img.size
#background = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))
#bg_w, bg_h = background.size
#offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
#background.paste(img, offset)
#background.save('out.png')



# ATLANTIC REGION


# TEMPERATURE
fig=plt.figure(figsize=(10,10))

#m = Basemap(projection='npstere', boundinglat=66,lon_0=273,resolution='l')         
m = Basemap(width=6000000,height=4500000, resolution='l',projection='stere', lat_ts=30,lat_0=71,lon_0=-60)
xi, yi = m(lons, lats)
m.drawcoastlines()
m.drawstates()
m.drawcountries()
m.fillcontinents(color='grey')

# Add Grid Lines
m.drawparallels(np.arange(-80., 81., 5.), labels=[1,0,0,0], fontsize=10)
m.drawmeridians(np.arange(-180., 181., 10.), labels=[0,0,0,1], fontsize=10)

#plt.title("Sea Surface Temperature: %s" % (filename),  fontsize=16)
plt.title("Sea Surface (0.5 m) 2018-08-28 00:00 UTC",  fontsize=16)
contours = m.contourf(xi,yi,(np.squeeze(temp)-273), levels=np.linspace(-2,26,28))#, colors='black', m.clabel(contours, inline=True, fontsize=8)
cbar = m.colorbar(contours, location='right',ticks=[-2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24,  26])
cbar.set_label('Temperature $(^{o}C)$', rotation=270, labelpad=30, y=0.45, fontsize=16)

plt.show()
fig.savefig('giops_ac_temp_240.png')
plt.close(fig) 



# Plot Data

