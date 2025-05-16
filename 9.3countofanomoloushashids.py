import pandas as pd
from pathlib import Path

# Step 1: Load your file
base_path = Path("use relative path to your data folder")
#file_path = Path("/mmfs1/projects/f8d7c0/2024-25/Gate City Bank/Kiran/anomalous_hash_parent_mismatch.csv")
df = pd.read_csv(file_path, low_memory=False)

# Step 2: Normalize key columns
cols_to_clean = ["Parent Name", "ShopName", "Cities", "Composite_Key", "Industry_Category"]
for col in cols_to_clean:
    df[col] = df[col].astype(str).str.upper().str.strip()

# Step 3: Count unique parent/shop names per hash
agg_counts = df.groupby("HASHED_MERCH_ID").agg({
    "Parent Name": pd.Series.nunique,
    "ShopName": pd.Series.nunique
}).reset_index()

# Step 4: Identify anomaly hash IDs
anomalous_ids = agg_counts[
    (agg_counts["Parent Name"] > 1) | (agg_counts["ShopName"] > 1)
]["HASHED_MERCH_ID"]

# Step 5: Filter anomalies
df_anomalies = df[df["HASHED_MERCH_ID"].isin(anomalous_ids)].copy()
df_anomalies["Transaction_Count"] = 1

# Step 6: Group by required fields including Online_Indicator
group_cols = [
    "HASHED_MERCH_ID", "Parent Name", "ShopName", "Cities", "Industry_Category",
    "Composite_Key", "Online_Indicator",  # <- Added here
    "ParentName_Flag", "ShopName_Flag", "TERM_ADDR_Flag", "SICSUBCD_Flag"
]

df_grouped = df_anomalies.groupby(group_cols).agg({
    "Transaction_Count": "sum"
}).reset_index()

# Step 7: Save the output
output_path = file_path.parent / "hash_id_parent_anomalies_only.csv"
df_grouped.to_csv(output_path, index=False)

print(f"File saved: {output_path}")
print(f"Unique anomalous HASHED_MERCH_IDs: {df_grouped['HASHED_MERCH_ID'].nunique()}")
