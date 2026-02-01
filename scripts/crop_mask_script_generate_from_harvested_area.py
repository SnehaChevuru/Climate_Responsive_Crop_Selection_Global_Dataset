import xarray as xr
import numpy as np

# Load the NetCDF file
file_path = "crop_masks/maize_irr_area.nc" (MIRCA harvested area)
ds = xr.open_dataset(file_path)

# Select the variable to mask 
var_name = "Band1"  
data = ds[var_name]

# Create the mask: Convert non-NaN and non-zero values to 1, otherwise 0
mask = xr.where(np.isnan(data) | (data == 0), np.nan, 1)

# Create a new dataset to store the mask
mask_ds = xr.Dataset({f"{var_name}_mask": mask})

# Save the mask dataset as a new NetCDF file
mask_file_path = "mai_masked_irr.nc"
mask_ds.to_netcdf(mask_file_path)

print(f"Masked NetCDF file saved as {mask_file_path}")
