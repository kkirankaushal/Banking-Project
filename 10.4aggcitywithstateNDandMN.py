import pandas as pd
import os

# Base path
base_path = Path("use relative path to your data folder")

# Load all classified files
online = pd.read_csv(os.path.join(base_path, "Processed_Online_With_ParentName_Classified.csv"))
offline = pd.read_csv(os.path.join(base_path, "Processed_Offline_With_ParentName_Classified.csv"))
offline_hash = pd.read_csv(os.path.join(base_path, "Processed_Offlinewithhash_With_ParentName_Classified.csv"))

# Combine all
df = pd.concat([online, offline, offline_hash], ignore_index=True)
df.columns = df.columns.str.strip()  # Clean whitespace

# If 'SIC code' exists, ensure it's string type
if "SIC code" in df.columns:
    df["SIC code"] = df["SIC code"].astype(str)

# Fix: use 'State' instead of 'Abbreviation'
agg_city_state = df.groupby(
    ["Parent Name", "Cities", "State", "Online_Indicator"]
).size().reset_index(name="Transaction Count")

# Save
agg_city_path = os.path.join(base_path, "agg_city_with_state.csv")
agg_city_state.to_csv(agg_city_path, index=False)

print("agg_city_with_state.csv created successfully.")
