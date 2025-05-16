import pandas as pd
from pathlib import Path

# Load cleaned CSV
#input_path = Path("/mmfs1/projects/f8d7c0/2024-25/Gate City Bank/Kiran/SQ_PAYPAL_SubShop_Cleaned.csv")
base_path = Path("use relative path to your data folder")
df = pd.read_csv(input_path)

# Select required columns
columns_to_keep = [
    "State", "Country", "ShopName", "Industry_Category", "Cities", "Parent Name",
    "SICSUBCD_Flag", "ParentName_Flag", "ShopName_Flag", "TERM_ADDR_Flag",
    "Online_Indicator", "Composite_Key", "SubShop"
]
df = df[columns_to_keep].copy()

# Optional: normalize casing for grouping
df["State"] = df["State"].astype(str).str.upper().str.strip()
df["Cities"] = df["Cities"].astype(str).str.upper().str.strip()
df["SubShop"] = df["SubShop"].astype(str).str.upper().str.strip()
df["Parent Name"] = df["Parent Name"].astype(str).str.upper().str.strip()

# Aggregation logic
agg_df = df.groupby(
    ["State", "Cities", "SubShop", "Parent Name", "Industry_Category", "Online_Indicator"]
).agg(
    Transaction_Count=('Composite_Key', 'count'),
    Unique_Shops=('ShopName', pd.Series.nunique)
).reset_index()

# Save aggregated output
output_path = input_path.with_name("SQ_PAYPAL_SubShop_Aggregated.csv")
agg_df.to_csv(output_path, index=False)

print(f"Aggregated file saved at: {output_path}")
