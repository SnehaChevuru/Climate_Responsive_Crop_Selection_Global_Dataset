# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:33:51 2025

@author: Chevu001
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

########## Irrigtaed Analysis #############

df = pd.read_excel(r"validation_data\RY_ir_M.xlsx")
df = df.drop(["Unnamed: 0","OBJECTID"], axis =1)
df.set_index("S_NAME", inplace = True)
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]
# Rename the first 20 columns with the generated names
df.columns.values[0:20] = column_names
df.replace(0,np.nan, inplace=True)
count = df.count(axis =1)
df['Count'] =count
df = df[df.Count >2]
df = df.drop(['Count'], axis =1)

df.head(2)

df1 = pd.read_excel(r"validation_data\M_SA_irr.xlsx")
df1 = df1.drop(["Unnamed: 0","OBJECTID"], axis =1)
df1.set_index("S_NAME", inplace = True)
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]

# Rename the first 20 columns with the generated names
df1.columns.values[0:20] = column_names

df1.head(2)

merg =pd.merge(df,df1, on="S_NAME")
merg.head(2)


RY = merg.iloc[:,0:20]
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]

# Rename the first 20 columns with the generated names
RY.columns.values[0:20] = column_names
RY = RY.reset_index()
RY.head(2)

SA1 = merg.iloc[:, 20:40]
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]

# Rename the first 20 columns with the generated names
SA1.columns.values[0:20] = column_names
SA1 = SA1.reset_index()
SA1.head(2)



RY[["County","State"]] = RY.S_NAME.str.split(",",expand= True)
RY = RY.drop(["S_NAME","County"], axis = 1)
RY = RY.groupby("State").mean()
RY= RY.reset_index()
RY = RY.drop(labels =[1], axis =0)
RY.set_index("State", inplace = True)
RY.head(6)


ryt = RY.mean(axis =0)
ryt = ryt/1000
ryrt = ryt.reset_index()
ryrt.columns.values[0:2] = ["TIME","Yield_ry"]

SA = SA1
SA[["County","State"]] = SA.S_NAME.str.split(",",expand= True)
SA = SA.drop(["S_NAME","County"], axis = 1)
SA.set_index("State", inplace = True)
SA = SA.astype(float)
SA = SA.groupby("State").mean()
SA= SA.reset_index()
SA = SA.drop(labels =[1], axis =0)
SA.set_index("State", inplace = True)
SA.head(2)

wt = SA.mean(axis =0)
wt = wt/1000
wrt = wt.reset_index()
wrt.columns.values[0:2] = ["TIME","Yield_w"]


######Soybean######

Sdf = pd.read_excel(r"validation_data\RY_ir_S.xlsx")
Sdf = Sdf.drop(["Unnamed: 0","OBJECTID"], axis =1)
Sdf.set_index("S_NAME", inplace = True)
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]
# Rename the first 20 columns with the generated names
Sdf.columns.values[0:20] = column_names
Sdf.replace(0,np.nan, inplace=True)
count = Sdf.count(axis =1)
Sdf['Count'] =count
Sdf = Sdf[Sdf.Count >2]
Sdf = Sdf.drop(['Count'], axis =1)

Sdf.head(2)

Sdf1 = pd.read_excel(r"validation_data\S_SA_irr.xlsx")
Sdf1 = Sdf1.drop(["Unnamed: 0","OBJECTID"], axis =1)
Sdf1.set_index("S_NAME", inplace = True)
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]

# Rename the first 20 columns with the generated names
Sdf1.columns.values[0:20] = column_names

Sdf1.head(2)

Smerg =pd.merge(Sdf,Sdf1, on="S_NAME")
Smerg.head(2)



SRY = Smerg.iloc[:,0:20]
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]

# Rename the first 20 columns with the generated names
SRY.columns.values[0:20] = column_names
SRY = SRY.reset_index()
SRY.head(2)

SSA1 = Smerg.iloc[:, 20:40]
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]

# Rename the first 20 columns with the generated names
SSA1.columns.values[0:20] = column_names
SSA1 = SSA1.reset_index()
SSA1.head(2)



for i, row in SRY.iterrows():
    for col in SRY.columns[1:]:
        if pd.isna(row[col]):
            SSA1.at[i, col] = np.nan
            

##### dropping delware due ot less data

SRY[["County","State"]] = SRY.S_NAME.str.split(",",expand= True)
SRY =SRY.drop(["S_NAME","County"], axis = 1)
SRY.set_index("State", inplace = True)
SRY = SRY.groupby("State").mean()
SRY= SRY.reset_index()
SRY = SRY.drop(labels =[1], axis =0)
SRY.set_index("State", inplace = True)


Sryt = SRY.mean(axis =0)
Sryt = Sryt/1000
Sryrt = Sryt.reset_index()
Sryrt.columns.values[0:2] = ["TIME","Yield_Sry"]

SSA = SSA1
SSA[["County","State"]] = SSA.S_NAME.str.split(",",expand= True)
SSA = SSA.drop(["S_NAME","County"], axis = 1)
SSA.set_index("State", inplace = True)
SSA = SSA.astype(float)
SSA = SSA.groupby("State").mean()
SSA= SSA.reset_index()
SSA = SSA.drop(labels =[1], axis =0)
SSA.set_index("State", inplace = True)


Swt = SSA.mean(axis =0)
Swt = Swt/1000
Swrt = Swt.reset_index()
Swrt.columns.values[0:2] = ["TIME","Yield_Sw"]


######Wheat######
Wdf = pd.read_excel(r"validation_data\RY_ir_WW.xlsx")
Wdf = Wdf.drop(["Unnamed: 0","OBJECTID"], axis =1)
Wdf.set_index("S_NAME", inplace = True)
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]
# Rename the first 20 columns with the generated names
Wdf.columns.values[0:20] = column_names
Wdf.replace(0,np.nan, inplace=True)
count = Wdf.count(axis =1)
Wdf['Count'] =count
Wdf = Wdf[Wdf.Count >2]
Wdf = Wdf.drop(['Count'], axis =1)

Wdf.head(2)

Wdf1 = pd.read_excel(r"validation_data\W_SA_irr.xlsx")

Wdf1 = Wdf1.drop(["Unnamed: 0","OBJECTID"], axis =1)
Wdf1.set_index("S_NAME", inplace = True)
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]

# Rename the first 20 columns with the generated names
Wdf1.columns.values[0:20] = column_names

Wdf1.head(2)

Wmerg =pd.merge(Wdf,Wdf1, on="S_NAME")
Wmerg.head(2)



WRY = Wmerg.iloc[:,0:20]
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]

# Rename the first 20 columns with the generated names
WRY.columns.values[0:20] = column_names
WRY = WRY.reset_index()
WRY.head(2)

WSA1 = Wmerg.iloc[:, 20:40]
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]

# Rename the first 20 columns with the generated names
WSA1.columns.values[0:20] = column_names
WSA1 = WSA1.reset_index()
WSA1.head(2)



for i, row in WRY.iterrows():
    for col in WRY.columns[1:]:
        if pd.isna(row[col]):
            WSA1.at[i, col] = np.nan
        

WRY[["County","State"]] = WRY.S_NAME.str.split(",",expand= True)
WRY = WRY.drop(["S_NAME","County"], axis = 1)
WRY = WRY.groupby("State").mean()
WRY.head(6)

Wryt = WRY.mean(axis =0)
Wryt = Wryt/1000
Wryrt = Wryt.reset_index()
Wryrt.columns.values[0:2] = ["TIME","Yield_Wry"]

WSA = WSA1
WSA[["County","State"]] = WSA.S_NAME.str.split(",",expand= True)
WSA = WSA.drop(["S_NAME","County"], axis = 1)
WSA.set_index("State", inplace = True)
WSA = WSA.astype(float)
WSA = WSA.groupby("State").mean()
WSA.head(2)

Wwt = WSA.mean(axis =0)
Wwt = Wwt/1000
Wwrt = Wwt.reset_index()
Wwrt.columns.values[0:2] = ["TIME","Yield_Ww"]



############## Rainfed Analyisis ###########

###Maize####
df_rf = pd.read_excel(r"validation_data\RY_rf_M.xlsx")
df_rf = df_rf.drop(["Unnamed: 0","OBJECTID"], axis =1)
df_rf.set_index("S_NAME", inplace = True)
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]
# Rename the first 20 columns with the generated names
df_rf.columns.values[0:20] = column_names
df_rf.replace(0,np.nan, inplace=True)



df1_rf = pd.read_excel(r"validation_data\M_SA_rf.xlsx")
df1_rf = df1_rf.drop(["Unnamed: 0","OBJECTID"], axis =1)
df1_rf.set_index("S_NAME", inplace = True)
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]

# Rename the first 20 columns with the generated names
df1_rf.columns.values[0:20] = column_names


merg_rf =pd.merge(df_rf,df1_rf, on="S_NAME")
merg_rf.head(2)

RY_rf = merg_rf.iloc[:,0:20]
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]

# Rename the first 20 columns with the generated names
RY_rf.columns.values[0:20] = column_names
RY_rf = RY_rf.reset_index()

SA1_rf = merg_rf.iloc[:, 20:40]
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]

# Rename the first 20 columns with the generated names
SA1_rf.columns.values[0:20] = column_names
SA1_rf = SA1_rf.reset_index()


for i, row in RY_rf.iterrows():
    for col in RY_rf.columns[1:]:
        if pd.isna(row[col]):
            SA1_rf.at[i, col] = np.nan
         


RY_rf[["County","State"]] = RY_rf.S_NAME.str.split(",",expand= True)
RY_rf =RY_rf.drop(["S_NAME","County"], axis = 1)
RY_rf = RY_rf.groupby("State").mean()

ryt_rf = RY_rf.mean(axis =0)
ryt_rf = ryt_rf/1000
ryrt_rf = ryt_rf.reset_index()
ryrt_rf.columns.values[0:2] = ["TIME","Yield_ry"]

SA_rf = SA1_rf
SA_rf[["County","State"]] = SA_rf.S_NAME.str.split(",",expand= True)
SA_rf = SA_rf.drop(["S_NAME","County"], axis = 1)
SA_rf.set_index("State", inplace = True)
SA_rf = SA_rf.astype(float)
SA_rf = SA_rf.groupby("State").mean()


wt_rf = SA_rf.mean(axis =0)
wt_rf = wt_rf/1000
wrt_rf = wt_rf.reset_index()
wrt_rf.columns.values[0:2] = ["TIME","Yield_w"]

####Soybean####

Sdf_rf = pd.read_excel(r"validation_data\RY_rf_S.xlsx")
Sdf_rf = Sdf_rf.drop(["Unnamed: 0","OBJECTID"], axis =1)
Sdf_rf.set_index("S_NAME", inplace = True)
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]
# Rename the first 20 columns with the generated names
Sdf_rf.columns.values[0:20] = column_names
Sdf_rf.replace(0,np.nan, inplace=True)
count = Sdf_rf.count(axis =1)
Sdf_rf['Count'] =count
Sdf_rf = Sdf_rf[Sdf_rf.Count >4]
Sdf_rf = Sdf_rf.drop(['Count'], axis =1)


Sdf1_rf = pd.read_excel(r"validation_data\S_SA_rf.xlsx")

Sdf1_rf = Sdf1_rf.drop(["Unnamed: 0","OBJECTID"], axis =1)
Sdf1_rf.set_index("S_NAME", inplace = True)
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]

# Rename the first 20 columns with the generated names
Sdf1_rf.columns.values[0:20] = column_names

Smerg_rf =pd.merge(Sdf_rf,Sdf1_rf, on="S_NAME")


SRY_rf = Smerg_rf.iloc[:,0:20]
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]

# Rename the first 20 columns with the generated names
SRY_rf.columns.values[0:20] = column_names
SRY_rf = SRY_rf.reset_index()

SSA1_rf = Smerg_rf.iloc[:, 20:40]
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]

# Rename the first 20 columns with the generated names
SSA1_rf.columns.values[0:20] = column_names
SSA1_rf = SSA1_rf.reset_index()


for i, row in SRY_rf.iterrows():
    for col in SRY_rf.columns[1:]:
        if pd.isna(row[col]):
            SSA1_rf.at[i, col] = np.nan
            

SRY_rf[["County","State"]] = SRY_rf.S_NAME.str.split(",",expand= True)
SRY_rf = SRY_rf.drop(["S_NAME","County"], axis = 1)
SRY_rf.set_index("State", inplace = True)
SRY_rf = SRY_rf.groupby("State").mean()
SRY_rf= SRY_rf.reset_index()
SRY_rf = SRY_rf.drop(labels =[1], axis =0)
SRY_rf.set_index("State", inplace = True)


Sryt_rf = SRY_rf.mean(axis =0)
Sryt_rf = Sryt_rf/1000
Sryrt_rf = Sryt_rf.reset_index()
Sryrt_rf.columns.values[0:2] = ["TIME","Yield_Sry"]

SSA_rf = SSA1_rf
SSA_rf[["County","State"]] = SSA_rf.S_NAME.str.split(",",expand= True)
SSA_rf = SSA_rf.drop(["S_NAME","County"], axis = 1)
SSA_rf.set_index("State", inplace = True)
SSA_rf = SSA_rf.astype(float)
SSA_rf = SSA_rf.groupby("State").mean()
SSA_rf= SSA_rf.reset_index()
SSA_rf = SSA_rf.drop(labels =[1], axis =0)
SSA_rf.set_index("State", inplace = True)


Swt_rf = SSA_rf.mean(axis =0)
Swt_rf = Swt_rf/1000
Swrt_rf = Swt_rf.reset_index()
Swrt_rf.columns.values[0:2] = ["TIME","Yield_Sw"]


#### Wheat####

Wdf_rf = pd.read_excel(r"validation_data\RY_rf_W.xlsx")
Wdf_rf = Wdf_rf.drop(["Unnamed: 0","OBJECTID"], axis =1)
Wdf_rf.set_index("S_NAME", inplace = True)

start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]
# Rename the first 20 columns with the generated names
Wdf_rf.columns.values[0:20] = column_names
Wdf_rf.replace(0,np.nan, inplace=True)
count = Wdf_rf.count(axis =1)
Wdf_rf['Count'] =count
Wdf_rf = Wdf_rf[Wdf_rf.Count >0]
Wdf_rf = Wdf_rf.drop(['Count'], axis =1)


Wdf1_rf = pd.read_excel(r"validation_data\W_SA_rf.xlsx")

Wdf1_rf = Wdf1_rf.drop(["Unnamed: 0","OBJECTID"], axis =1)
Wdf1_rf.set_index("S_NAME", inplace = True)
Wdf1_rf.replace(0,np.nan, inplace=True)
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]

# Rename the first 20 columns with the generated names
Wdf1_rf.columns.values[0:20] = column_names

Wmerg_rf =pd.merge(Wdf_rf,Wdf1_rf, on="S_NAME")

WRY_rf = Wmerg_rf.iloc[:,0:20]
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]

# Rename the first 20 columns with the generated names
WRY_rf.columns.values[0:20] = column_names
WRY_rf = WRY_rf.reset_index()

WSA1_rf = Wmerg_rf.iloc[:, 20:40]
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]

# Rename the first 20 columns with the generated names
WSA1_rf.columns.values[0:20] = column_names
WSA1_rf = WSA1_rf.reset_index()

for i, row in WRY_rf.iterrows():
    for col in WRY_rf.columns[1:]:
        if pd.isna(row[col]):
            WSA1_rf.at[i, col] = np.nan
        

WRY_rf[["County","State"]] = WRY_rf.S_NAME.str.split(",",expand= True)
WRY_rf = WRY_rf.drop(["S_NAME","County"], axis = 1)
WRY_rf = WRY_rf.groupby("State").mean()

Wryt_rf = WRY_rf.mean(axis =0)
Wryt_rf = Wryt_rf/1000
Wryrt_rf = Wryt_rf.reset_index()
Wryrt_rf.columns.values[0:2] = ["TIME","Yield_Wry"]

WSA_rf = WSA1_rf
WSA_rf[["County","State"]] = WSA_rf.S_NAME.str.split(",",expand= True)
WSA_rf = WSA_rf.drop(["S_NAME","County"], axis = 1)
WSA_rf.set_index("State", inplace = True)
WSA_rf = WSA_rf.astype(float)
WSA_rf = WSA_rf.groupby("State").mean()

Wwt_rf = WSA_rf.mean(axis =0)
Wwt_rf = Wwt_rf/1000
Wwrt_rf = Wwt_rf.reset_index()
Wwrt_rf.columns.values[0:2] = ["TIME","Yield_Ww"]


########### Plots ###############

years_columns = [f'{year}' for year in range(2000, 2020)]
years= years_columns

fig, ((ax0, ax1), (ax2, ax3), (ax4, ax5)) = plt.subplots(nrows=3, ncols=2, figsize=(12,10))


ax0.plot(years, ryrt.Yield_ry.loc[:],linestyle = "dashed", marker = 'o', color = 'green')
ax0.plot(years, wrt.Yield_w.loc[:],linestyle = "dashed", marker = 'D', color = 'blue')
ax0.set_ylabel("Maize Yield (t/ha)", fontsize=12)
ax0.set_xticks(years[::2])
ax0.set_ylim(0,16)
ax0.set_yticks(np.arange(0,16,2))
ax0.set_title("Irrigated", fontsize=12)
ax0.grid(True)

ax1.plot(years, ryrt_rf.Yield_ry.loc[:],linestyle = "dashed", marker = 'o', color = 'green')
ax1.plot(years, wrt_rf.Yield_w.loc[:],linestyle = "dashed", marker = 'D', color = 'blue')
ax1.set_xticks(years[::2])
ax1.set_ylim(0,16)
ax1.set_yticks(np.arange(0,16,2))
ax1.set_title("Rainfed", fontsize=12)
ax1.grid(True)

ax2.plot(years, Sryrt.Yield_Sry.loc[:],linestyle = "dashed", marker = 'o', color = 'green')
ax2.plot(years, Swrt.Yield_Sw.loc[:],linestyle = "dashed", marker = 'D', color = 'blue')
ax2.set_ylabel("Soybean Yield (t/ha)",fontsize=12)
ax2.set_xticks(years[::2])
ax2.set_ylim(0,6)
ax2.set_yticks(np.arange(0,6,1))
ax2.grid(True)

ax3.plot(years, Sryrt_rf.Yield_Sry.loc[:],linestyle = "dashed", marker = 'o', color = 'green')
ax3.plot(years, Swrt_rf.Yield_Sw.loc[:],linestyle = "dashed", marker = 'D', color = 'blue')
ax3.set_xticks(years[::2])
ax3.set_ylim(0,6)
ax3.set_yticks(np.arange(0,6,1))
ax3.grid(True)

ax4.plot(years, Wryrt.Yield_Wry.loc[:],linestyle = "dashed", marker = 'o', color = 'green')
ax4.plot(years, Wwrt.Yield_Ww.loc[:],linestyle = "dashed", marker = 'D', color = 'blue')
ax4.set_xlabel("Years",fontsize=12)
ax4.set_ylabel("Wheat Yield (t/ha)",fontsize=12)
ax4.set_xticks(years[::2])
ax4.set_ylim(0,8)
ax4.set_yticks(np.arange(0,8,1))
ax4.grid(True)

ax5.plot(years, Wryrt_rf.Yield_Wry.loc[:],linestyle = "dashed",marker = 'o', color = 'green')
ax5.plot(years, Wwrt_rf.Yield_Ww.loc[:],linestyle = "dashed", marker = 'D', color = 'blue')
ax5.set_xlabel("Years",fontsize=12)
ax5.set_xticks(years[::2])#, fontsize=12)
ax5.set_ylim(0,8)
ax5.set_yticks(np.arange(0,8,1))
ax5.grid(True)

plt.legend(['Reported Yield','WOFOST'], fontsize=10, loc='upper center', bbox_to_anchor=(0.5, -0.2), fancybox=True, shadow=True, ncol=4)
plt.tight_layout()
plt.show()
