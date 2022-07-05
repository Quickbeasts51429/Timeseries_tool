from netCDF4 import Dataset
import numpy as np
import pandas as pd 

# Reading in the netCDF file
data = Dataset(r'D:\GeoDeltaLabs Projects\Handling netCDF files with Python\Temparature Data\1961.nc', 'r')

# Storing the lat and lon data into the variables 
lat = data.variables['lat'][:]
lon = data.variables['lon'][:]

# Storing the lat and lon of Katmandu, Nepal into variables 
lat_katmandu =  27.697817
lon_katmandu =  85.329806

# Squared difference of lat and lon 
sq_diff_lat = (lat - lat_katmandu)**2
sq_diff_lon = (lon - lon_katmandu)**2

# Identifying the index of the minimum value for lat and lon 
min_index_lat = sq_diff_lat.argmin()
min_index_lon = sq_diff_lon.argmin()

temp = data.variables['tave']

# Creating an empty pandas dataframe
starting_date = data.variables['time'].units[14:24]
ending_date = data.variables['time'].units[14:18] + '-12-31'
date_range = pd.date_range(start = starting_date, end = ending_date)
df = pd.DataFrame(0, columns = ['Temparature'], index = date_range)

dt = np.arange(0, data.variables['time'].size)

for time_index in dt:
    df.iloc[time_index] = temp[time_index,min_index_lat ,min_index_lon]

# Saving the time series into a csv
df.to_csv('temparature_Katmandu.csv')