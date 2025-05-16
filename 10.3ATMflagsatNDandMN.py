import pandas as pd
from pathlib import Path

# Step 1: Load your data
#file_path = Path("/mmfs1/projects/f8d7c0/2024-25/Gate City Bank/Kiran/ND_MN_Cities_With_ATM_Flag.csv")
base_path = Path("use relative path to your data folder")
df = pd.read_csv(file_path)

# Step 2: Normalize and clean key columns
df["Cities"] = df["Cities"].astype(str).str.upper().str.strip()
df["State"] = df["State"].astype(str).str.upper().str.strip()

# Step 3: Replace "NAN" string with actual missing value and drop missing cities
df["Cities"] = df["Cities"].replace("NAN", pd.NA)
df = df.dropna(subset=["Cities"])

# Step 4: Define city-to-correct-state mapping for known conflicts
fix_state = {
    "ADAMS": "ND",
    "ALEXANDRIA": "MN",
    "APPLE VALLEY": "MN",
    "BISMARCK": "ND",
    "BUFFALO": "MN",
    "CALEDONIA": "MN",
    "CARRINGTON": "ND",
    "CLEVELAND": "MN",
    "COLUMBUS": "ND",
    "CROSBY": "MN",
    "CRYSTAL": "MN",
    "DAWSON": "MN",
    "DEVILS LAKE": "ND",
    "DICKINSON": "ND",
    "ELGIN": "ND",
    "ELK RIVER": "MN",
    "ELLENDALE": "ND",
    "FARGO": "ND",
    "FERGUS FALLS": "MN",
    "GARRISON": "ND",
    "GOLDEN VALLEY": "MN",
    "GRAND FORKS": "ND",
    "JAMESTOWN": "ND",
    "LEONARD": "ND",
    "LUVERNE": "MN",
    "MANDAN": "ND",
    "MAPLETON": "ND",
    "MARION": "ND",
    "MAYVILLE": "ND",
    "MCGREGOR": "MN",
    "MEDINA": "ND",
    "MINOT": "ND",
    "MOORHEAD": "MN",
    "ROGERS": "MN",
    "SAUK RAPIDS": "MN",
    "ST. CLOUD": "MN",
    "UNDERWOOD": "MN",
    "WAHPETON": "ND",
    "WAITE PARK": "MN",
    "WEST FARGO": "ND",
    "WHITE EARTH": "MN",
    "WILLISTON": "ND"
}

# Step 5: Apply the corrections
df["State"] = df.apply(
    lambda row: fix_state[row["Cities"]] if row["Cities"] in fix_state else row["State"],
    axis=1
)

# Step 6: Save corrected row-level file
corrected_file = file_path.parent / "ND_MN_Cities_With_ATM_Flag_Corrected.csv"
df.to_csv(corrected_file, index=False)
print(f"Saved cleaned row-level file: {corrected_file}")

# Step 7: Aggregate by key dimensions for Tableau dashboard
group_fields = ["Cities", "State", "Industry_Category", "Parent Name", "Online_Indicator", "ATM_Present"]

df_agg = df.groupby(group_fields).agg({
    "Transaction_Count": "sum"
}).reset_index()

# Step 8: Save the aggregated file
agg_file = file_path.parent / "agg_ND_MN_Cities.csv"
df_agg.to_csv(agg_file, index=False)
print(f"Saved updated aggregated file: {agg_file}")
