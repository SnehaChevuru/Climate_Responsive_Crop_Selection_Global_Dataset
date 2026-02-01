# Climate_Responsive_Crop_Selection_Global_Dataset

**Author:** Sneha Chevuru  
**ORCID:** https://orcid.org/0000-0002-3873-649X  
**Project:** GoNexus  
**Faculty:** Faculty of Geoscience  
**Department:** Department of Physical Geography  
**Date:** 03 July 2025  

---

## 1. Dataset Description

This dataset provides global-scale information on **climate-responsive crop variety selection and sowing dates** for six major crops, simulated under historical and future climate conditions using the **WOFOST crop model**.

The dataset is intended to support research on **crop adaptation, climate impacts, and food security**.

---

## 2. Spatial and Temporal Coverage

- **Spatial coverage:** Global (excluding Greenland)  
- **Spatial resolution:** 0.5° × 0.5° (~64,055 grid cells)  

- **Temporal coverage:** 1961–2100  
- **Time slices (20-year periods):**  
  - one   - 1961–1980  
  - two   - 1981–2000  
  - three - 2001–2020  
  - four  - 2021–2040  
  - five  - 2041–2060  
  - six   - 2061–2080  
  - seven - 2081–2100  

---

## 3. Crops and Cultivars Included

### Crops
- Maize  
- Soybean  
- Winter wheat  
- Spring wheat  
- Rice (season 1; `Rice1`)  
- Rice (season 2; `Rice2`)  

### Cultivars (varieties)
The numbers indicate distinct cultivars defined by crop-specific physiological parameters.

- **Maize:** 7 cultivars (`mag2`–`mag8`)  
- **Soybean:** 7 cultivars (`soy1`–`soy7`)  
- **Winter wheat:** 9 cultivars (`wwh1`–`wwh9`)  
- **Spring wheat:** 9 cultivars (`swh1`–`swh9`)  
- **Rice1 & Rice2:** 9 cultivars (`rice1`–`rice9`)  

---

## 4. Cultivar Parameter Files (`.cab`)

Cultivar-specific parameters are provided in **`.cab` format**, organized by crop.

Each `.cab` file contains:
- Definitions of crop ecotypes and cultivars
- Temperature requirements (minimum, optimum, maximum)
- Temperature sums for phenological development stages
- Biomass conversion efficiency
- Biomass partitioning to plant organs

These parameters are used as inputs to the WOFOST crop model.  
For detailed cultivar background, users are referred to the original cultivar source literature.

---

## 5. Simulation Conditions

- **Irrigated**
- **Rainfed**

Both conditions are provided separately.

---

## 6. Data Format and Content

- **File format:** tab-delimited `.txt` files  
- **Organization:**  
  - One file per **crop × time slice × management condition**
- Each file contains:
  - All cultivar and sowing date combination under
  - Climate realization information
  - Simulated yield, biomass, and water use

---

## 7. Climate Sampling (LHS)

Latin Hypercube Sampling (LHS) was applied to select the representative sample from the number of climate realizations:

- **Future periods:**  
  - 300 realizations (5 GCMs × 3 SSPs × 20 years)  
  - 20 representative realizations selected per grid cell

- **Historical period:**  
  - 100 realizations (5 GCMs × historical × 20 years)  
  - 20 realizations selected per grid cell

The selected realizations correspond to specific combinations of **GCM, scenario, and year**.

---

## 8. Directory Structure / Repository content 

data/                  # Contains two zip folder (Irrigated.zip and Rainfed.zip). Each zip folder has crop-specific TXT files for each time slice
- Irrigated.zip # Crop-specific TXT files (irrigated)
- Rainfed.zip # Crop-specific TXT files (rainfed)

data/crop_variety/     # Contains crop-specific variety/cultivar information
- *.cab # Cultivar parameter files

crop_masks/               
- *.nc # Crop-specific harvested area masks

Hy_month/
- *.nc # Start month of hydrological year

LHS/     # Contains the LHS sample for each grid cell per time slice in a zip folder. Includes information on year, respective GCM, RCP-SSP scenario, precipitation (kg m-2 s-1) and temperature (°C) over each hydrological year.
- *.zip # LHS climate samples per time slice

README.md — This file

---

## 9. File Naming Convention   

{cropname}\_{period}\_{condition}.txt

**cropname:** Maize, Soybean, Springwheat, Winterwheat, Rice1, Rice2

**period:** one (1961–1980), two (1981–2000), three (2001–2020), four (2021–2040), five (2041–2060), six (2061–2080), seven (2081–2100)

**condition:** `irr` = Irrigated and `rf` = Rainfed

**Example filename:**
Maize_five_irr.txt - Maize data, 2041–2060, irrigated scenario

---

## 10. Variable Description    

**Documentation of Variables**
|Variable	|          Description|
|----------|-------------|
|Lat	   |           Latitude of the grid cell (decimal degrees)|
|Lon	    |          Longitude of the grid cell (decimal degrees)|
|Cultivar	 |     Crop variety used; corresponds to variety definitions in data/crop_variety/|
|Sowing	    |          Sowing/planting date (MM-DD format)|
|GCM	       |       Global Climate Model used for the simulation|
|RCP	        |      Climate scenario: RCP-SSP combination (e.g., ssp370, ssp585)|
|Year	        |      Simulation year|
|Yield	       |       Crop yield (kg/ha)|
|CWR	         |     Crop water requirement or consumption (mm)|
|Biomass	     |         Total aboveground crop biomass (kg/ha)|

---

## 11. Example Usage     

```python
import pandas as pd

# Load a sample file (e.g., Maize data for 2041–2060, irrigated)

df = pd.read_csv("Maize_five_irr.txt", sep="\t")
df.head()

Lat     Lon     Cultivar        Sowing  GCM     RCP     Year    Yield   CWR     Biomass
49.75   -106.75 mag8    05-25   ipsl-cm6a-lr    ssp370  2060    7612.99 598.573 19739.45
33.25   -115.75 mag7    04-25   ipsl-cm6a-lr    ssp585  2051    2940.68 386.768 10161.2
42.25   -95.75  mag4    05-20   ipsl-cm6a-lr    ssp585  2050    9324.06 474.566 16373.74
32.75   -112.25 mag8    04-22   mpi-esm1-2-hr   ssp126  2052    4284.47 555.038 14148.45
32.25   -93.75  mag4    04-01   ukesm1-0-ll     ssp126  2045    9956.89 376.867 17736.13
32.25   -94.25  mag3    03-25   gfdl-esm4       ssp126  2046    7174.36 305.221 13555.29
46.25   -100.25 mag5    05-10   mri-esm2-0      ssp585  2059    8617.01 389.376 16976.52
42.25   -95.25  mag7    05-01   ukesm1-0-ll     ssp585  2057    5855.93 452.314 15111.25
43.25   -92.25  mag4    05-20   ipsl-cm6a-lr    ssp370  2056    11229.0 450.767 18771.42

```
---
## 12. Code Availability

  Scripts used to generate and process the dataset are available on GitHub and are referenced in the accompanying manuscript.

---

## 13. Citation

If you use this dataset in your work, please cite the accompanying publication and DOI link.
https://doi.org/10.24416/UU01-8V0A4N

---


