import pandas as pd
# Load maize data for 2041–2060 under irrigated conditions
df = pd.read_csv("Maize_five_irr.txt", sep="\t")
# Filter for the contiguous United States (example)
usa_df = df[
    (df["Lat"] >= 25) & (df["Lat"] <= 50) &
    (df["Lon"] >= -125) & (df["Lon"] <= -65)
]
usa_df.head()

##This approach allows users to efficiently subset the global dataset to specific regions of interest.
