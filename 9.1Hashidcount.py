import pandas as pd
import os

# Base path to the files
base_path = Path("use relative path to your data folder")

# File names
files = [
    "Processed_Offline_With_ParentName_Classified.csv",
    "Processed_Offlinewithhash_With_ParentName_Classified.csv",
    "Processed_Online_With_ParentName_Classified.csv"
]

# Load and combine all files
dfs = [pd.read_csv(os.path.join(base_path, file)) for file in files]
combined_df = pd.concat(dfs, ignore_index=True)

# Clean column names
combined_df.columns = combined_df.columns.str.strip()

# Total rows
total_rows = len(combined_df)

# Unique values
unique_parents = combined_df["Parent Name"].nunique()
unique_hashes = combined_df["HASHED_MERCH_ID"].nunique()

# Anomalous HASHED_MERCH_IDs (shared by >1 parent)
hash_parent_counts = combined_df.groupby("HASHED_MERCH_ID")["Parent Name"].nunique()
anomaly_count = hash_parent_counts[hash_parent_counts > 1].count()
anomaly_pct = (anomaly_count / unique_hashes) * 100

# Classification percentages
flag_cols = ["Online_Indicator", "TERM_ADDR_Flag", "ShopName_Flag", "ParentName_Flag", "SICSUBCD_Flag"]
classification_percentages = {
    flag: (combined_df[flag].sum() / total_rows) * 100 for flag in flag_cols
}

# Output
print(f"Total Rows: {total_rows}")
print(f"Unique Parent Names: {unique_parents}")
print(f"Unique HASHED_MERCH_IDs: {unique_hashes}")
print(f"Anomalous HASHED_MERCH_IDs: {anomaly_count} ({anomaly_pct:.2f}%)")

print("\n Classification Completion Rates:")
for flag, pct in classification_percentages.items():
    print(f"   {flag}: {pct:.2f}%")

