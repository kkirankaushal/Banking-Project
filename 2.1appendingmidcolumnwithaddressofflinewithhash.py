import pandas as pd
import os

# File paths
base_path = Path("use relative path to your data folder")
#input_file = '/mmfs1/projects/f8d7c0/2024-25/Gate City Bank/Kiran/Processed_Offlinewithash.csv'
output_file = '/mmfs1/projects/f8d7c0/2024-25/Gate City Bank/Kiran/Processed_OfflineWithHash_Filled.csv'

# Remove the output file if it exists
if os.path.exists(output_file):
    os.remove(output_file)

# Function to extract GarbageValue from text after '#', excluding last word
def extract_garbage_value_from_hash(txn_desc):
    try:
        after_hash = txn_desc.split('#', 1)[1].strip()
        words = after_hash.split()
        if len(words) > 1:
            return ' '.join(words[:-1])  # Remove last word (e.g. state+country)
        else:
            return after_hash
    except:
        return ''

# Process the CSV in chunks
chunk_size = 500000
for chunk in pd.read_csv(input_file, chunksize=chunk_size):
    chunk.columns = chunk.columns.str.strip()

    # Generate GarbageValue
    chunk['GarbageValue'] = chunk['TXN_DESCRIPTION'].apply(extract_garbage_value_from_hash)

    # Fill TERM_ADDR with GarbageValue if it's empty
    chunk['TERM_ADDR'] = chunk.apply(
        lambda row: row['GarbageValue'] if pd.isna(row['TERM_ADDR']) or str(row['TERM_ADDR']).strip() == '' else row['TERM_ADDR'],
        axis=1
    )

    # Append chunk to the output file
    chunk.to_csv(output_file, mode='a', index=False, header=not os.path.exists(output_file))

print(f"Done! Filled file saved to:\n{output_file}")
