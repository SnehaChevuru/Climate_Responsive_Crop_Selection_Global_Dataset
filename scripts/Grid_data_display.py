# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:38:05 2024

@author: Chevu001
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

   
def plot_yield_cwr(ax, data, title, show_ylabel=False, show_xlabel=False, label_fontsize=32, tick_fontsize=24):
    custom_palette = {
        'mag2': 'red',  
        'mag3': 'blue',
        'mag4': 'green',
        'mag5': 'purple',
        'mag6': 'orange',
        'mag7': 'pink',
        'mag8': 'brown'
    }

    sns.scatterplot(ax=ax, data=data, x='CWR', y='Yield', hue='Cul', style='Sowing_Date', palette=custom_palette, s=150, legend=False)
    
    if show_ylabel:
        ax.set_ylabel('Yield (t/ha)', fontsize=label_fontsize)
    else:
        ax.set_ylabel('')

    if show_xlabel:
        ax.set_xlabel('Crop water consumption (mm)', fontsize=label_fontsize)
    else:
        ax.set_xlabel('')

    ax.set_xlim(150, 650)
    ax.set_ylim(0, 18)
    ax.set_xticks([200, 300, 400, 500, 600])
    ax.tick_params(axis='x', labelsize=tick_fontsize)
    ax.tick_params(axis='y', labelsize=tick_fontsize)
    ax.set_title(title, fontsize=label_fontsize)
        
    
def load_and_preprocess(file_path):
    """Load and preprocess the dataset."""
    df = pd.read_csv(file_path, sep=',')
    # Keep relevant columns and convert Yield to t/ha
    df = df[['GCM', 'RCP', 'Year', 'Cul', 'Yield', 'CWR', 'Sow']]
    df['Yield'] = df['Yield'].astype(int) / 1000
    df['CUL_SOW'] = df['Cul'] + '-' + df['Sow']
    df['Sowing_Day'] = df['CUL_SOW'].apply(lambda x: x.split('-')[1])  # Extract the day (e.g., '15', '25')
    df['Sowing_Month'] = df['CUL_SOW'].apply(lambda x: x.split('-')[-1])  # Extract the month (e.g., 'April', 'May')

    # Combine day and month for a new 'Sowing_Date' column
    df['Sowing_Date'] = df['Sowing_Day'] + '-' + df['Sowing_Month']
    
    return df


def main():
    # File paths for the datasets
    file_path1 = r"grid\P1_40_25_-91_75_Ir.csv"
    file_path2 = r"grid\P2_40_25_-91_75_Ir.csv"
    file_path3 = r"grid\P3_40_25_-91_75_Ir.csv"
    file_path4 = r"grid\P4_40_25_-91_75_Ir.csv"
    file_path5 = r"grid\P5_40_25_-91_75_Ir.csv"
    file_path6 = r"grid\P6_40_25_-91_75_Ir.csv"
    file_path7 = r"grid\P7_40_25_-91_75_Ir.csv"
    file_path01 = r"grid\P1_40_25_-91_75_Rf.csv"
    file_path02 = r"grid\P2_40_25_-91_75_Rf.csv"
    file_path03 = r"grid\P3_40_25_-91_75_Rf.csv"
    file_path04 = r"grid\P4_40_25_-91_75_Rf.csv"
    file_path05 = r"grid\P5_40_25_-91_75_Rf.csv"
    file_path06 = r"grid\P6_40_25_-91_75_Rf.csv"
    file_path07 = r"grid\P7_40_25_-91_75_Rf.csv"
    
    # Load and preprocess data
    data1 = load_and_preprocess(file_path1)
    data2 = load_and_preprocess(file_path2)
    data3 = load_and_preprocess(file_path3)
    data4 = load_and_preprocess(file_path4)
    data5 = load_and_preprocess(file_path5)
    data6 = load_and_preprocess(file_path6)
    data7 = load_and_preprocess(file_path7)
    data01 = load_and_preprocess(file_path01)
    data02 = load_and_preprocess(file_path02)
    data03 = load_and_preprocess(file_path03)
    data04 = load_and_preprocess(file_path04)
    data05 = load_and_preprocess(file_path05)
    data06 = load_and_preprocess(file_path06)
    data07 = load_and_preprocess(file_path07)
    
    # data_list = [data1, data2, data3, data4, data5, data6, data7, data01, data02, data03, data04, data05, data06, data07]
    data_list = [data1, data01, data2, data02, data3, data03, data4, data04, data5, data05, data6, data06, data7, data07]
    titles = [
    '1961-1980', '1961-1980', '1981-2000', '1981-2000', '2001-2020', '2001-2020',
    '2021-2040', '2021-2040', '2041-2060', '2041-2060', '2061-2080', '2061-2080',
    '2081-2100', '2081-2100']
    idx = [1,3,5,7,9,11,13,2,4,6,8,10,12]
    
    # Create figure and set size
    fig, axes = plt.subplots(nrows=7, ncols=2, figsize=(30, 38), sharex=True, sharey=True)
    
    # for ax, data, title in zip(axes.flat, data_list, titles):
    #     plot_yield_cwr(ax, data, title)
   
    for i, (ax, data, title) in enumerate(zip(axes.flat, data_list, titles)):
       row, col = divmod(i, 2)
       show_ylabel = (col == 0)
       show_xlabel = (row == 6)
       plot_yield_cwr(ax, data, title, show_ylabel=show_ylabel, show_xlabel=show_xlabel) 
   
       
    plt.tight_layout()
    plt.show()

# Call the main function
if __name__ == "__main__":
    main()


