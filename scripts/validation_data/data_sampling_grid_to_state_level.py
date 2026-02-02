import pandas as pd
import matplotlib.pylab as pltb

#Datasets processing

#dataset 1
df=pd.read_csv("Maize_2000_2019.txt", sep ="\t") 

### this file can be generted by selecting the cultivar and sowing date combination from the dataset. 
#####Please refer to Chevuru, S., Van Beek, R. L., Van Vliet, M. T., Aerts, J. P., & Bierkens, M. F. (2025). Relevance of feedbacks between water availability and crop systems using a coupled hydrological–crop growth model. Hydrology and Earth System Sciences, 29(17), 4219-4239.



#df.drop([0], inplace = True)

df = df.astype(float)


#concat two datasets

df["Year"] =df["Year"].astype(str)
#df = df.dropna()
df = df[["Lat","Lon","Year","TWSO"]]

df = df.groupby(['Lat','Lon', 'Year'])['TWSO'].mean().unstack()

# Generate column names for the first 16 columns
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]

# Rename the first 20 columns with the generated names
df.columns.values[0:20] = column_names
df = df.reset_index()
df = df.dropna()
df["Lat"] =df["Lat"].astype(float)
df["Lon"] =df["Lon"].astype(float)

#Getting the area of the crop mask

mask=pd.read_csv("validation_data/m_ir_mask.csv",sep=";")
mask = mask[["lat","lon","Band1"]]
mask.columns.values[0:3] = ["Lat","Lon","mask"]
mask["Lat"] =mask["Lat"].round(2)
mask["Lon"] =mask["Lon"].round(2)

Mask = pd.merge(df, mask, on= ["Lat","Lon"])

#Counties areas; to match the grids that fall on the counties
SA=pd.read_excel("validation_data/shapearea.xlsx")
SA=SA[["Avg_lat", "Avg_lon", "OBJECTID","Shape_Area"]]
SA.columns.values[0:4] =["Lat","Lon","OBJECTID","Shape_Area"]
SA["Lat"] =SA["Lat"].astype(float)
SA["Lon"] =SA["Lon"].astype(float)
SA["OBJECTID"] =SA["OBJECTID"].astype(int)
SA["Shape_Area"] =SA["Shape_Area"].astype(float)
SA["Lat"] =SA["Lat"].round(2)
SA["Lon"] =SA["Lon"].round(2)


dfw = pd.merge(Mask,SA, on= ["Lat","Lon"])

#weighted average
def wavg(group, avg_name, weight_name, area_name):
    
    d= group[avg_name].astype(float)
    w= group[weight_name].astype(float)
    ia=group[area_name].astype(float)
    
    
    try:
        return (d*w*ia).sum()/(w*ia).sum()
    except ZeroDivisionError:
        return d.mean()

years = range(1979,2020)
summary = pd.DataFrame({f"TWSO_{year}": dfw.groupby("OBJECTID").apply(wavg, f"TWSO_{year}", "Shape_Area", "mask") for year in years})

# Rename columns
summary.columns = [f"TWSO_{year}" for year in years]
print(summary)

#extracting objectids
Re =pd.read_excel("validation_data/USA_county.xlsx")
Re=Re[["OBJECTID","S_NAME"]]

Id = pd.merge(summary,Re, on ="OBJECTID")
print(Id)

Id.to_excel("validation_data/M_SA_irr.xlsx")