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

######### Processing #########
for i, row in RY.iterrows():
    for col in RY.columns[1:]:
        if pd.isna(row[col]):
            SA1.at[i, col] = np.nan


RY[["County","State"]] = RY.S_NAME.str.split(",",expand= True)
RY = RY.drop(["S_NAME","County"], axis = 1)
RY.set_index("State", inplace = True)
RY = RY.groupby("State").mean()
RY= RY.reset_index()
RY.set_index("State", inplace = True)
RY.head(6)

rys = RY.mean(axis=1)
rys = rys/1000
ryrs = rys.reset_index()
ryrs.columns.values[0:2] = ["OBJECTID","Yield_ry"]


SA = SA1
SA[["County","State"]] = SA.S_NAME.str.split(",",expand= True)
SA = SA.drop(["S_NAME","County"], axis = 1)
SA.set_index("State", inplace = True)
SA = SA.astype(float)
SA = SA.groupby("State").mean()
SA= SA.reset_index()
SA.set_index("State", inplace = True)
SA.head(2)

ws = SA.mean(axis=1)
ws = ws.astype(int)/1000
wrs = ws.reset_index()
wrs.columns.values[0:2] = ["OBJECTID","Yield_w"]


######Soybean######

Sdf = pd.read_excel(r"validation_data\RY_ir_S.xlsx")
Sdf = Sdf.drop(["Unnamed: 0","OBJECTID"], axis =1)
Sdf.set_index("S_NAME", inplace = True)
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]
# Rename the first 20 columns with the generated names
Sdf.columns.values[0:20] = column_names


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
            

##### dropping texas due ot less data

SRY[["County","State"]] = SRY.S_NAME.str.split(",",expand= True)
SRY =SRY.drop(["S_NAME","County"], axis = 1)
SRY.set_index("State", inplace = True)
SRY = SRY.groupby("State").mean()
SRY= SRY.reset_index()
SRY = SRY.drop(labels =[4], axis =0)
SRY.set_index("State", inplace = True)

Srys = SRY.mean(axis=1)
Srys = Srys/1000
Sryrs = Srys.reset_index()
Sryrs.columns.values[0:2] = ["OBJECTID","Yield_Sry"]


SSA = SSA1
SSA[["County","State"]] = SSA.S_NAME.str.split(",",expand= True)
SSA = SSA.drop(["S_NAME","County"], axis = 1)
SSA.set_index("State", inplace = True)
SSA = SSA.astype(float)
SSA = SSA.groupby("State").mean()
SSA= SSA.reset_index()
SSA = SSA.drop(labels =[4], axis =0)
SSA.set_index("State", inplace = True)

Sws = SSA.mean(axis=1)
Sws = Sws.astype(int)/1000
Swrs = Sws.reset_index()
Swrs.columns.values[0:2] = ["OBJECTID","Yield_Sw"]



######Wheat######
Wdf = pd.read_excel(r"validation_data\RY_ir_WW.xlsx")
Wdf = Wdf.drop(["Unnamed: 0","OBJECTID"], axis =1)
Wdf.set_index("S_NAME", inplace = True)
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]
# Rename the first 20 columns with the generated names
Wdf.columns.values[0:20] = column_names


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

Wrys = WRY.mean(axis=1)
Wrys = Wrys/1000
Wryrs = Wrys.reset_index()
Wryrs.columns.values[0:2] = ["OBJECTID","Yield_Wry"]


WSA = WSA1
WSA[["County","State"]] = WSA.S_NAME.str.split(",",expand= True)
WSA = WSA.drop(["S_NAME","County"], axis = 1)
WSA.set_index("State", inplace = True)
WSA = WSA.astype(float)
WSA = WSA.groupby("State").mean()
WSA.head(2)

Wws = WSA.mean(axis=1)
Wws = Wws.astype(int)/1000
Wwrs = Wws.reset_index()
Wwrs.columns.values[0:2] = ["OBJECTID","Yield_Ww"]



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
         

####### dropping NEW MEXICO as there is no reported data #######
RY_rf[["County","State"]] = RY_rf.S_NAME.str.split(",",expand= True)
RY_rf =RY_rf.drop(["S_NAME","County"], axis = 1)
RY_rf = RY_rf.groupby("State").mean()
RY_rf= RY_rf.reset_index()
RY_rf = RY_rf.drop(labels =[4], axis =0)
RY_rf.set_index("State", inplace = True)

rys_rf = RY_rf.mean(axis=1)
rys_rf = rys_rf/1000
ryrs_rf = rys_rf.reset_index()
ryrs_rf.columns.values[0:2] = ["OBJECTID","Yield_ry"]


SA_rf = SA1_rf
SA_rf[["County","State"]] = SA_rf.S_NAME.str.split(",",expand= True)
SA_rf = SA_rf.drop(["S_NAME","County"], axis = 1)
SA_rf.set_index("State", inplace = True)
SA_rf = SA_rf.astype(float)
SA_rf = SA_rf.groupby("State").mean()
SA_rf= SA_rf.reset_index()
SA_rf = SA_rf.drop(labels =[4], axis =0)
SA_rf.set_index("State", inplace = True)


ws_rf = SA_rf.mean(axis=1)
ws_rf = ws_rf/1000
wrs_rf = ws_rf.reset_index()
wrs_rf.columns.values[0:2] = ["OBJECTID","Yield_w"]


####Soybean####

Sdf_rf = pd.read_excel(r"validation_data\RY_rf_S.xlsx")
Sdf_rf = Sdf_rf.drop(["Unnamed: 0","OBJECTID"], axis =1)
Sdf_rf.set_index("S_NAME", inplace = True)
start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]
# Rename the first 20 columns with the generated names
Sdf_rf.columns.values[0:20] = column_names



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
            
######## dropping Texas #########
SRY_rf[["County","State"]] = SRY_rf.S_NAME.str.split(",",expand= True)
SRY_rf = SRY_rf.drop(["S_NAME","County"], axis = 1)
SRY_rf.set_index("State", inplace = True)
SRY_rf = SRY_rf.groupby("State").mean()
SRY_rf= SRY_rf.reset_index()
SRY_rf = SRY_rf.drop(labels =[4], axis =0)
SRY_rf.set_index("State", inplace = True)


Srys_rf = SRY_rf.mean(axis=1)
Srys_rf = Srys_rf/1000
Sryrs_rf = Srys_rf.reset_index()
Sryrs_rf.columns.values[0:2] = ["OBJECTID","Yield_Sry"]


SSA_rf = SSA1_rf
SSA_rf[["County","State"]] = SSA_rf.S_NAME.str.split(",",expand= True)
SSA_rf = SSA_rf.drop(["S_NAME","County"], axis = 1)
SSA_rf.set_index("State", inplace = True)
SSA_rf = SSA_rf.astype(float)
SSA_rf = SSA_rf.groupby("State").mean()
SSA_rf= SSA_rf.reset_index()
SSA_rf = SSA_rf.drop(labels =[4], axis =0)
SSA_rf.set_index("State", inplace = True)

Sws_rf = SSA_rf.mean(axis=1)
Sws_rf = Sws_rf.astype(int)/1000
Swrs_rf = Sws_rf.reset_index()
Swrs_rf.columns.values[0:2] = ["OBJECTID","Yield_Sw"]


#### Wheat####

Wdf_rf = pd.read_excel(r"validation_data\RY_rf_W.xlsx")
Wdf_rf = Wdf_rf.drop(["Unnamed: 0","OBJECTID"], axis =1)
Wdf_rf.set_index("S_NAME", inplace = True)

start_year = 2000
num_years = 20
column_names = [f'TWSO_{start_year + i}' for i in range(num_years)]
# Rename the first 20 columns with the generated names
Wdf_rf.columns.values[0:20] = column_names


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
        
####### drooping North Dakota due to no reported data #####
WRY_rf[["County","State"]] = WRY_rf.S_NAME.str.split(",",expand= True)
WRY_rf = WRY_rf.drop(["S_NAME","County"], axis = 1)
WRY_rf = WRY_rf.groupby("State").mean()
WRY_rf= WRY_rf.reset_index()
WRY_rf = WRY_rf.drop(labels =[7], axis =0)
WRY_rf.set_index("State", inplace = True)

Wrys_rf = WRY_rf.mean(axis=1)
Wrys_rf = Wrys_rf/1000
Wryrs_rf = Wrys_rf.reset_index()
Wryrs_rf.columns.values[0:2] = ["OBJECTID","Yield_Wry"]


WSA_rf = WSA1_rf
WSA_rf[["County","State"]] = WSA_rf.S_NAME.str.split(",",expand= True)
WSA_rf = WSA_rf.drop(["S_NAME","County"], axis = 1)
WSA_rf.set_index("State", inplace = True)
WSA_rf = WSA_rf.astype(float)
WSA_rf = WSA_rf.groupby("State").mean()
WSA_rf= WSA_rf.reset_index()
WSA_rf = WSA_rf.drop(labels =[7], axis =0)
WSA_rf.set_index("State", inplace = True)


Wws_rf = WSA_rf.mean(axis=1)
Wws_rf = Wws_rf.astype(int)/1000
Wwrs_rf = Wws_rf.reset_index()
Wwrs_rf.columns.values[0:2] = ["OBJECTID","Yield_Ww"]


####### Plots #########

states = ryrs.OBJECTID.to_list()
states0 = Wryrs.OBJECTID.to_list()
states1 = Sryrs.OBJECTID.to_list()
states2 = ryrs_rf.OBJECTID.to_list()
states3 = Wryrs_rf.OBJECTID.to_list()
states4 = Sryrs_rf.OBJECTID.to_list()

fig, ((ax0, ax1), (ax2, ax3), (ax4, ax5)) = plt.subplots(nrows=3, ncols=2, figsize=(14,10))
x=range(len(states))
x0=range(len(states0))
x1=range(len(states1))
x2=range(len(states2))
x3=range(len(states3))
x4=range(len(states4))
width = 0.4


ax0.bar(x, ryrs.Yield_ry, width = width, label = 'RY', color = 'green')
ax0.bar(np.array(x) +width, wrs.Yield_w,width = width, label =  'SA', color = 'blue')
ax0.set_ylabel("Maize Yield (t/ha)",fontsize=12)
ax0.set_xticks(np.array(x)+ 1.5*width,states, rotation=30, fontsize = 8)
ax0.set_ylim(0,15)
ax0.set_yticks(np.arange(0,15,2))
ax0.set_title("Irrigated", fontsize=12)

ax1.bar(x2, ryrs_rf.Yield_ry, width = width, label = 'RY', color = 'green')
ax1.bar([i+width for i in x2], wrs_rf.Yield_w,width = width, label =  'SA', color = 'blue')
ax1.set_xticks([i + 1.5*width for i in x2],states2, rotation=30, fontsize = 8)
ax1.set_ylim(0,15)
ax1.set_yticks(np.arange(0,15,2))
ax1.set_title("Rainfed", fontsize=12)

ax2.bar(x1, Sryrs.Yield_Sry, width = width, label = 'RY', color = 'green')
ax2.bar([i+width for i in x1], Swrs.Yield_Sw,width = width, label =  'SA', color = 'blue')
ax2.set_ylabel("Soybean Yield (t/ha)",fontsize=12)
ax2.set_xticks([i + 1.5*width for i in x1],states1, rotation=30, fontsize = 8)
ax2.set_ylim(0,6)
ax2.set_yticks(np.arange(0,6,1))


ax3.bar(x4, Sryrs_rf.Yield_Sry, width = width, label = 'RY', color = 'green')
ax3.bar([i+width for i in x4], Swrs_rf.Yield_Sw,width = width, label =  'SA', color = 'blue')
ax3.set_xticks([i + 1.5*width for i in x4],states4, rotation=30, fontsize = 8)
ax3.set_ylim(0,6)
ax3.set_yticks(np.arange(0,6,1))

ax4.bar(x0, Wryrs.Yield_Wry, width = width, label = 'RY', color = 'green')
ax4.bar([i+width for i in x0], Wwrs.Yield_Ww,width = width, label =  'SA', color = 'blue')### dropping Delware due to less data ##########
ax4.set_xlabel("States",fontsize=12)
ax4.set_ylabel("Wheat Yield (t/ha)",fontsize=12)
ax4.set_xticks([i + 1.3*width for i in x0],states0, rotation=30, fontsize = 8)
ax4.set_ylim(0,8)
ax4.set_yticks(np.arange(0,8,1))

ax5.bar(x3, Wryrs_rf.Yield_Wry, width = width, label = 'RY', color = 'green')
ax5.bar([i+width for i in x3], Wwrs_rf.Yield_Ww,width = width, label =  'SA', color = 'blue')
ax5.set_xlabel("States",fontsize=12)
ax5.set_xticks([i + 1.3*width for i in x3],states3, rotation=30, fontsize = 8)
ax5.set_ylim(0,8)


legend = plt.legend(['Reported Yield', 'WOFOST'], fontsize=10, loc='lower center', bbox_to_anchor=(0.5, -0.7), fancybox=True, shadow=True, ncol=4)
fig.subplots_adjust(hspace=0.4, wspace=0.3)

plt.tight_layout()
plt.show()