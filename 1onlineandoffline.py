import pandas as pd
import re

# Load your dataset
base_path = Path("use relative path to your data folder")
df = pd.read_csv(file_path)
df.columns = df.columns.str.strip()

# Ensure TXN_DESCRIPTION is string
df['TXN_DESCRIPTION'] = df['TXN_DESCRIPTION'].astype(str).str.strip()

# --- STEP 1: Extract last 4 characters into State/Country info ---
df['State_Country'] = df['TXN_DESCRIPTION'].str[-4:]
df['State'] = df['State_Country'].str[:2]
df['Country'] = df['State_Country'].str[-2:]

# --- STEP 2: Filter for US only ---
df_us = df[df['Country'].str.upper() == 'US'].copy()

# --- STEP 3: Classify Based on TXN_DESCRIPTION Patterns ---

# 1. Offline (contains #, not * or COM)
offline = df_us[
    df_us['TXN_DESCRIPTION'].str.contains('#') &
    ~df_us['TXN_DESCRIPTION'].str.contains(r'\*|COM', case=False)
].copy()

# 2. Online (contains * or COM)
online = df_us[
    df_us['TXN_DESCRIPTION'].str.contains(r'\*|COM', case=False)
].copy()

# 3. OfflineWithAsh (no #, no *, no COM)
offlinewithash = df_us[
    ~df_us['TXN_DESCRIPTION'].str.contains(r'#|\*|COM', case=False)
].copy()

# --- STEP 4: Save Outputs ---
offline.to_csv('Offline.csv', index=False)
online.to_csv('Online.csv', index=False)
offlinewithash.to_csv('OfflineWithAsh.csv', index=False)
import pandas as pd
import re

# Load your dataset
file_path = '/path/to/your/full_dataset.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)
df.columns = df.columns.str.strip()

# Ensure TXN_DESCRIPTION is a string
df['TXN_DESCRIPTION'] = df['TXN_DESCRIPTION'].astype(str).str.strip()

# Extract State_Country, State, and Country
df['State_Country'] = df['TXN_DESCRIPTION'].str[-4:]
df['State'] = df['State_Country'].str[:2]
df['Country'] = df['State_Country'].str[-2:]

# Filter for US transactions
df_us = df[df['Country'].str.upper() == 'US'].copy()

# Extract ShopName and GarbageValue
def extract_shopname_and_garbage(txn_desc):
    if '#' in txn_desc:
        parts = txn_desc.split('#', 1)
        shop_name = parts[0].strip()
        garbage_value = parts[1][:-4].strip() if len(parts[1]) > 4 else ''
    elif '*' in txn_desc:
        parts = txn_desc.split('*', 1)
        shop_name = parts[0].strip()
        garbage_value = parts[1][:-4].strip() if len(parts[1]) > 4 else ''
    elif 'COM' in txn_desc:
        parts = txn_desc.split('COM', 1)
        shop_name = parts[0].strip()
        garbage_value = parts[1][:-4].strip() if len(parts[1]) > 4 else ''
    else:
        shop_name = txn_desc[:-4].strip()
        garbage_value = ''
    return pd.Series([shop_name, garbage_value])

df_us[['ShopName', 'GarbageValue']] = df_us['TXN_DESCRIPTION'].apply(extract_shopname_and_garbage)

# Classify transactions
offline = df_us[df_us['TXN_DESCRIPTION'].str.contains('#') & ~df_us['TXN_DESCRIPTION'].str.contains(r'\*|COM', case=False)].copy()
online = df_us[df_us['TXN_DESCRIPTION'].str.contains(r'\*|COM', case=False)].copy()
offlinewithash = df_us[~df_us['TXN_DESCRIPTION'].str.contains(r'#|\*|COM', case=False)].copy()

# Save the datasets
offline.to_csv('Offline.csv', index=False)
online.to_csv('Online.csv', index=False)
offlinewithash.to_csv('OfflineWithAsh.csv', index=False)

print("Data split complete! Files saved as:")
print("- Offline.csv")
print("- Online.csv")
print("- OfflineWithAsh.csv")

print("Data split complete! Files saved as:")
print("- Offline.csv")
print("- Online.csv")
print("- OfflineWithAsh.csv")
