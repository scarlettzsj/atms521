# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
from scipy.stats import ttest_1samp

filein1='/data/zhuowang/a/zhuowang/ATMS521/Data/detrend.nino34.ascii.txt'
filein2='/data/zhuowang/a/zhuowang/ATMS521/Data/precip.mon.mean.nc'

n34 = pd.read_csv(filein1, header=0, sep="\s+") # Read N34 data
n34 = n34.loc[(n34['YR'] >= 1979) & (n34['YR'] <= 2020)] # Select particular years
n34['rolling'] = n34['ANOM'].rolling(3, min_periods=3, center=True).mean() # Compute 3-month mean

# Select Jan of every year, which will give us the DJF seasonal means 
n34 = n34.dropna().loc[n34['MON'] == 1]
n34 = n34.set_index('YR') # Set years as index

n34['norm'] = (n34['rolling'] - n34['rolling'].mean())/np.std(n34['rolling']) # Compute normalized anomalies

#select El Nino and La Nina years
en_years = ...
ln_years = ...


#Load the netCDF file and read precip
ds = xr.open_dataset(filein2)
precip = ds['precip'].sel(time=slice('1979-01-01','2020-12-01'))

# Mask the data to only include the DJF season
tmp = precip.where(precip['time.season'] == 'DJF').rolling(min_periods=3, center=True, time=3).mean()

# Calculate the DJF seasonal mean for each year
pcp_djf = tmp.dropna(dim='time')

# Calculate anomalies by subtracting the long-term mean from each seasonal mean
pcp_anom = ....

# Get EN and LN DJF precip
pcp_en = pcp_anom.sel(time=pcp_anom.time.dt.year.isin(en_years))
pcp_ln = pcp_anom.sel(time=pcp_anom.time.dt.year.isin(ln_years))

# Calculate the composite mean and perform the t-test
pcpm_en = pcp_en.mean(dim='time')
t_en,p_en = ...

pcpm_ln = pcp_ln.mean(dim='time')
t_ln,p_ln = ...

# Plotting using Cartopy and save the figure
.....
