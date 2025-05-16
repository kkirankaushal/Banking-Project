import pandas as pd
import os

# Define the base path
#base_path = '/mmfs1/projects/f8d7c0/2024-25/Gate City Bank/Kiran/'
base_path = Path("use relative path to your data folder")

# Load both files
df_offline_processed = pd.read_csv(os.path.join(base_path, 'Processed_OfflineWithHash_Filled_WithIndustry_Cities.csv'))
df_offline_parent = pd.read_csv(os.path.join(base_path, 'cleaned_offlinewithhash_shopname_frequency_with_parentname.csv'), encoding='ISO-8859-1')

# Normalize ShopName just in case (optional but helps with mismatches)
df_offline_processed['ShopName'] = df_offline_processed['ShopName'].astype(str).str.strip()
df_offline_parent['ShopName'] = df_offline_parent['ShopName'].astype(str).str.strip()

# Merge the files on ShopName
df_offline_merged = df_offline_processed.merge(
    df_offline_parent[['ShopName', 'Parent Name']],
    on='ShopName',
    how='left'
)

# Save the output file
output_file = os.path.join(base_path, 'Processed_Offlinewithhash_With_ParentName.csv')
df_offline_merged.to_csv(output_file, index=False)

print(f"Done! Merged file saved at: {output_file}")
