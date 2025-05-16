import pandas as pd
import os
import re

# File paths
base_path = Path("use relative path to your data folder")
#input_file = '/mmfs1/projects/f8d7c0/2024-25/Gate City Bank/Kiran/Processed_Online.csv'
output_file = '/mmfs1/projects/f8d7c0/2024-25/Gate City Bank/Kiran/Processed_Online_Filled.csv'

# Remove existing output file if present
if os.path.exists(output_file):
    os.remove(output_file)

# Define a function to extract GarbageValue
def extract_garbage_value(txn_desc):
    try:
        after_star = txn_desc.split('*', 1)[1].strip()
        words = after_star.split()
        if len(words) > 1:
            return ' '.join(words[:-1])  # Remove the last word (e.g., NDUS)
        else:
            return after_star
    except:
        return ''

# Process the file in chunks
chunk_size = 500000
for chunk in pd.read_csv(input_file, chunksize=chunk_size):
    chunk.columns = chunk.columns.str.strip()

    # Generate GarbageValue
    chunk['GarbageValue'] = chunk['TXN_DESCRIPTION'].apply(extract_garbage_value)

    # Fill TERM_ADDR with GarbageValue if it's missing
    chunk['TERM_ADDR'] = chunk.apply(
        lambda row: row['GarbageValue'] if pd.isna(row['TERM_ADDR']) or str(row['TERM_ADDR']).strip() == '' else row['TERM_ADDR'],
        axis=1
    )

    # Save to output
    chunk.to_csv(output_file, mode='a', index=False, header=not os.path.exists(output_file))

print(f"Done! Cleaned file saved to:\n{output_file}")
