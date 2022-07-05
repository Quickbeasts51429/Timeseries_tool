from netCDF4 import Dataset
import numpy as np

# Reading in the netCDF file 
data = Dataset(r'D:\GeoDeltaLabs Projects\Handling netCDF files with Python\Temparature Data\1961.nc', 'r')

# Displaying the names of the variables
print(data.variables.keys())

# Accessing the variables
lon = data.variables['lon']
print(lon)

lat = data.variables['lat']
print(lat)

time = data.variables['time']
print(time)

tave = data.variables['tave']
print(tave)

# Accessing the data from the variables
time_data = data.variables['time'][:]
print(time_data)

lon_data = data.variables['lon'][:]
print(lon_data)

lat_data = data.variables['lat'][:]
print(lat_data)


