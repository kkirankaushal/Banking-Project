import pandas as pd
from pathlib import Path

# Path to your data folder
base_path = Path("use relative path to your data folder")

# Input files
files = {
    "offline_main": "Processed_Offline_With_ParentName_Classified.csv",
    "offline_hash": "Processed_Offlinewithhash_With_ParentName_Classified.csv",
    "online": "Processed_Online_With_ParentName_Classified.csv"
}

# Load and tag source
df_list = []
for tag, fname in files.items():
    df = pd.read_csv(base_path / fname)
    df["Source_File"] = tag
    df_list.append(df)

# Combine all into one
df_all = pd.concat(df_list, ignore_index=True)
df_all.columns = [col.strip().replace(" ", "_") for col in df_all.columns]

# Normalize key fields
for col in ["Parent_Name", "ShopName", "State", "Cities", "Industry_Category"]:
    if col in df_all.columns:
        df_all[col] = df_all[col].fillna("Unknown").astype(str).str.upper().str.strip()

# Fix Online indicator
df_all["Online_Indicator"] = df_all["Online_Indicator"].fillna(0).astype(int)

# Classification flags
flag_cols = ["ParentName_Flag", "ShopName_Flag", "TERM_ADDR_Flag", "SICSUBCD_Flag"]
for flag in flag_cols:
    df_all[flag] = df_all[flag].fillna(0).astype(int)

# Classification logic
def classify(row):
    flags = [row[f] for f in flag_cols]
    if all(f == 1 for f in flags):
        return "Match"
    elif any(f == 0 for f in flags):
        return "Mismatch"
    else:
        return "No Parent Name"

df_all["Classification_Status"] = df_all.apply(classify, axis=1)

# Add transaction count
df_all["Transaction_Count"] = 1

# Count failures
df_all["ShopName_Fail_Count"] = (df_all["ShopName_Flag"] == 0).astype(int)
df_all["ParentName_Fail_Count"] = (df_all["ParentName_Flag"] == 0).astype(int)
df_all["TERM_ADDR_Fail_Count"] = (df_all["TERM_ADDR_Flag"] == 0).astype(int)
df_all["SICSUBCD_Fail_Count"] = (df_all["SICSUBCD_Flag"] == 0).astype(int)

# Grouping fields
group_fields = [
    "Parent_Name", "ShopName", "State", "Cities",
    "Industry_Category", "Online_Indicator", "Classification_Status"
]

# Aggregation
df_agg = df_all.groupby(group_fields).agg({
    "Transaction_Count": "sum",
    "ShopName_Fail_Count": "sum",
    "ParentName_Fail_Count": "sum",
    "TERM_ADDR_Fail_Count": "sum",
    "SICSUBCD_Fail_Count": "sum"
}).reset_index()

# Save output
output_file = base_path / "agg_merchant_clean_with_flags.csv"
df_agg.to_csv(output_file, index=False)

print(f"Final enriched table saved to: {output_file}")
print(f"Rows: {len(df_agg):,}")
