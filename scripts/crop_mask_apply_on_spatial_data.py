import xarray as xr

# Open datasets
ds_yield = xr.open_dataset("output_prod_yield.nc")  ## generated from convert Txt_to_Ncfile.py
ds_mask  = xr.open_dataset("maize_masked_irr.nc")  ## generated from crop_mask_script_generte_from_harvested_area.py

# Apply mask
masked_yield = ds_yield["Yield"].where(ds_mask["mask"] == 1)

# Save output
masked_yield.to_dataset(name="yield").to_netcdf("yield_masked.nc")

# Close files
ds_yield.close()
ds_mask.close()
