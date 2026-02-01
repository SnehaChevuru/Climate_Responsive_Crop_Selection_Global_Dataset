import pandas as pd
import numpy as np


input_file = "data/Irr/Maize_five_irr.txt"
output_file = "Maize_five_irr_productivity_metric.txt"

# Load the text file

df = pd.read_csv(input_file, delim_whitespace=True, usecols=["Lat", "Lon", "Yield", "CWR", "RCP", 'Cultivar', 'Sowing'])

# Drop potential header repetition if present in the first row (optional)
df = df[df.iloc[:, 0] != df.columns[0]]

print(df.head())
print(df['Lat'].size)

numeric_cols = ['Lat', 'Lon', 'Yield', 'CWR']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')


#df = df[df['RCP'] == 'ssp370']

# Debugging step: Print NaN count before grouping 'Cultivar', 'Sowing'
print("Missing values before grouping:\n", df.isna().sum())

# Remove NaN values from Yield and CWR before proceeding
#df = df.dropna(subset=['Yield', 'CWR'])

# Group by Lat, Lon, Cultivar, and Sowing and compute the mean Yield and Water Consumption over 20 years (time slice)
grouped_df = df.groupby(['Lat', 'Lon', 'Cultivar', 'Sowing'], as_index=False).agg({
    'Yield': 'mean',
    'CWR': 'mean'
})

# Debugging step: Print NaN count after grouping
print("Missing values after grouping:\n", grouped_df.isna().sum())

# Ensure Yield has no NaN before using idxmax()
grouped_df = grouped_df.dropna(subset=['Yield'])

# Find the maximum average yield for each Lat, Lon (productivity) and for reliability minimum yield from all cultivar and sowing combination 
max_yield_df = grouped_df.loc[grouped_df.groupby(['Lat', 'Lon'])['Yield'].idxmax(), ['Lat', 'Lon', 'Yield', 'CWR', 'Cultivar', 'Sowing']]

# Save to file
max_yield_df.to_csv(output_file, sep='\t', index=False)

print("Processing complete! File saved as:", output_file)

