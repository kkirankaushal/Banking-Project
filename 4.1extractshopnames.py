import pandas as pd
import re

# Define the base path to your files
base_path = Path("use relative path to your data folder")
#base_path = '/mmfs1/projects/f8d7c0/2024-25/Gate City Bank/Kiran/'

# Function to extract ShopName for Online transactions
def extract_shopname_online(txn_desc):
    """Extracts ShopName for Online transactions: everything before '*' or '.com'."""
    match = re.split(r'\*|\.com', txn_desc, maxsplit=1, flags=re.IGNORECASE)
    return match[0].strip() if match else txn_desc

# Function to extract ShopName for Offlinewithash transactions
def extract_shopname_offlinewithash(txn_desc):
    """Extracts ShopName for Offlinewithash transactions: everything before '#'."""
    match = txn_desc.split('#', 1)
    return match[0].strip() if match else txn_desc

# Function to extract ShopName for Offline transactions
def extract_shopname_offline(txn_desc):
    """Extracts ShopName for Offline transactions: first two words, skipping numeric second word."""
    words = txn_desc.split()
    if len(words) > 1 and words[1].isalpha():
        return f"{words[0]} {words[1]}"
    return words[0]

# Function to process each file
def process_file(file_name, extraction_function):
    """Reads a CSV, applies the extraction function, and saves to a new CSV."""
    file_path = base_path + file_name
    df = pd.read_csv(file_path)
    df['ShopName'] = df['TXN_DESCRIPTION'].apply(extraction_function)
    output_file = base_path + 'Processed_' + file_name
    df.to_csv(output_file, index=False)
    print(f"Processed {file_name} and saved to {output_file}")

# Process each file with the corresponding extraction function
process_file('Online.csv', extract_shopname_online)
process_file('Offlinewithash.csv', extract_shopname_offlinewithash)
process_file('Offline.csv', extract_shopname_offline)
