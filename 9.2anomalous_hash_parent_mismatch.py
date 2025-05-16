import pandas as pd
import os

# Base path
base_path = Path("use relative path to your data folder")

# Files to load
files = [
    "Processed_Offline_With_ParentName_Classified.csv",
    "Processed_Offlinewithhash_With_ParentName_Classified.csv",
    "Processed_Online_With_ParentName_Classified.csv"
]

# Load and combine all files
df_list = [pd.read_csv(os.path.join(base_path, f), encoding='latin1') for f in files]
combined_df = pd.concat(df_list, ignore_index=True)

# Standardize column names
combined_df.columns = combined_df.columns.str.strip()

# Drop rows where HASHED_MERCH_ID or Parent Name is missing
combined_df = combined_df.dropna(subset=["HASHED_MERCH_ID", "Parent Name"])

# Group by hash and count unique parent names
parent_counts = combined_df.groupby("HASHED_MERCH_ID")["Parent Name"].nunique().reset_index()
parent_counts = parent_counts[parent_counts["Parent Name"] > 1]

# Filter original data for only anomalous hash ids
anomaly_df = combined_df[combined_df["HASHED_MERCH_ID"].isin(parent_counts["HASHED_MERCH_ID"])]

# Optional: sort for better readability
anomaly_df = anomaly_df.sort_values(["HASHED_MERCH_ID", "Parent Name", "State", "Cities"])

# Save to CSV
anomaly_df.to_csv(os.path.join(base_path, "anomalous_hash_parent_mismatch.csv"), index=False)

# Display how many such anomalies exist
print(f"🔍 Found {len(parent_counts)} HASHED_MERCH_IDs with multiple parent names.")
print("✅ Output saved as 'anomalous_hash_parent_mismatch.csv'")
