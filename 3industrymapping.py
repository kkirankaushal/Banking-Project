import pandas as pd

# Path to SIC mapping
#sic_file = '/mmfs1/projects/f8d7c0/2024-25/Gate City Bank/Kiran/Official_SIC_Codes_List.csv'
base_path = Path("use relative path to your data folder")
# Load and clean SIC list
sic_df = pd.read_csv(sic_file)
sic_df.columns = sic_df.columns.str.strip()
sic_df['SIC Code'] = sic_df['SIC Code'].astype(str).str.extract(r'(\d+)', expand=False).str.zfill(4)
sic_df.rename(columns={'SIC Code': 'SICSUBCD', 'Description': 'Industry_Category'}, inplace=True)

# List of files to process
files = [
    'Processed_OfflineWithHash_Filled.csv',
    'Processed_Offline_Filled.csv'
    'Processed_Online_Filled.csv
]

base_path = '/mmfs1/projects/f8d7c0/2024-25/Gate City Bank/Kiran/'

# Loop through files and merge
for fname in files:
    input_file = base_path + fname
    output_file = input_file.replace('.csv', '_WithIndustry.csv')

    print(f" Processing: {fname}")

    df = pd.read_csv(input_file)
    df.columns = df.columns.str.strip()

    # Clean SICSUBCD column
    df['SICSUBCD'] = df['SICSUBCD'].astype(str).str.extract(r'(\d+)', expand=False).str.zfill(4)

    # Merge with SIC mapping
    df = df.merge(sic_df, on='SICSUBCD', how='left')

    # Save to new file
    df.to_csv(output_file, index=False)
    print(f"Saved with industry category: {output_file}")
