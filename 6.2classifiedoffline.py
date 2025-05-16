import pandas as pd
import os

# Define the path and file name
base_path = '/mmfs1/projects/f8d7c0/2024-25/Gate City Bank/Kiran/'
input_file = 'Processed_Offline_With_ParentName.csv'
output_file = 'Processed_Offline_With_ParentName_Classified.csv'

# Load the data
df = pd.read_csv(os.path.join(base_path, input_file))

# Add classification columns (1 = Yes, 0 = No)
df['SICSUBCD_Flag'] = df['SICSUBCD'].notna().astype(int)
df['ParentName_Flag'] = df['Parent Name'].notna().astype(int)
df['ShopName_Flag'] = df['ShopName'].notna().astype(int)
df['TERM_ADDR_Flag'] = df['TERM_ADDR'].notna().astype(int)
df['Online_Indicator'] = 0  # Because this is offline data

# Save the result
df.to_csv(os.path.join(base_path, output_file), index=False)

print("File created:", output_file)
