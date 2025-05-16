import pandas as pd
import os

# Define base path
#base_path = '/mmfs1/projects/f8d7c0/2024-25/Gate City Bank/Kiran/'
base_path = Path("use relative path to your data folder")

# Load both files
df_processed = pd.read_csv(os.path.join(base_path, 'Processed_Online_Filled_WithIndustry_Cities.csv'))
df_parent = pd.read_csv(os.path.join(base_path, 'cleaned_full_1000_shopnames_mapped_Online.csv'))

# Merge parent name into the processed file on ShopName
df_merged = df_processed.merge(df_parent[['ShopName', 'Parent Name']], on='ShopName', how='left')

# Save the new file with parent names
df_merged.to_csv(os.path.join(base_path, 'Processed_Online_With_ParentName.csv'), index=False)

print("Parent names mapped and saved to 'Processed_Online_With_ParentName.csv'")
