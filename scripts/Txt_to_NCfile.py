import pandas as pd
import numpy as np
import xarray as xr

df = pd.read_csv("Maize_five_irr_productivity_metric.txt", sep = "\t") ## generated from data_to_metric_productivity.py script 

#### Read crop productivity metrics from TXT file.
#### This file can be pre-filtered by:
####   - specific cultivar–sowing date combinations
####   - selected GCM–RCP scenario combinations
####   - chosen metric type (e.g. productivity, reliability, water-use efficiency)

print(df.head())
print(df['Lat'].size)

df['lat'] = df['Lat'].astype(str)
df['lon'] = df['Lon'].astype(str)
df = df.drop(columns =['Lat','Lon'])

print(df['lat'].size)
df = df[['lat','lon','Yield','CWR']]
#df = df[['lat','lon','Cultivar','Sowing']]
#df = df[['lat','lon','WUE','Yield','CWR']]


############ clone map creation #################
clone=pd.read_csv("globe_30arcmin.csv",sep=",")

#### The clone map defines the target global grid (0.5° / 30 arcmin resolution).
#### It contains all latitude–longitude combinations covering the globe.
#### This ensures that the output NetCDF:
####   - has a complete and consistent global grid
####   - includes grid cells even where no crop data exist
####   - assigns NaN values to locations without data
#### The clone map acts as a spatial template for the final NetCDF file.

clone["lat"] =clone["lat"].astype(str)
clone["lon"] =clone["lon"].astype(str)
print(clone.head())
print(clone['lat'].size)

#clone = clone.drop([['mask'] == 0], axis =1)  
#### (Optional) Remove grid cells where mask == 0
#### if a land-use or crop mask is applied

d = pd.merge(clone, df, on =["lat","lon"], how = "left")
#### Merge crop data onto the clone map using latitude and longitude.
#### Left join ensures that all global grid cells are retained.
#### Grid cells without crop data remain as NaN.

print(d.head())
print(d['lat'].size)

n = d.astype(float)
print(n.head())

n = n.set_index(['lat','lon'])

arr = n.to_xarray()

arr.to_netcdf("output_prod_yield.nc")
