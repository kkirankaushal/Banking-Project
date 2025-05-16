import pandas as pd
import os

# Base path where the files are located
#base_path = '/mmfs1/projects/f8d7c0/2024-25/Gate City Bank/Kiran/'
base_path = Path("use relative path to your data folder")

# Files with classified data
classified_files = [
    'Processed_Online_With_ParentName_Classified.csv',
    'Processed_Offline_With_ParentName_Classified.csv',
    'Processed_Offlinewithhash_With_ParentName_Classified.csv'
]

# Function to generate composite key
def add_composite_key(df):
    # Fill missing values with 'NA' to ensure clean key
    df = df.fillna('NA')
    
    # Ensure all required columns are present
    required_cols = ['SICSUBCD', 'Parent Name', 'ShopName', 'TERM_ADDR', 'Online_Indicator']
    for col in required_cols:
        if col not in df.columns:
            df[col] = 'NA'

    # Create the composite key
    df['Composite_Key'] = (
        df['SICSUBCD'].astype(str).str.strip() + '||' +
        df['Parent Name'].astype(str).str.strip() + '||' +
        df['ShopName'].astype(str).str.strip() + '||' +
        df['TERM_ADDR'].astype(str).str.strip() + '||' +
        df['Online_Indicator'].astype(str).str.strip()
    )
    
    return df

# Apply to all files
for file in classified_files:
    file_path = os.path.join(base_path, file)
    df = pd.read_csv(file_path, encoding='utf-8', on_bad_lines='skip')
    df = add_composite_key(df)
    df.to_csv(file_path, index=False)
    print(f"Composite key added to: {file}")
