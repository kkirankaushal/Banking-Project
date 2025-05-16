import pandas as pd
import os

# Set the base directory
base_path = Path("use relative path to your data folder")

# Load CSV files
df_online = pd.read_excel(os.path.join(base_path, 'full_1000_shopnames_mapped_Online.xlsx'))
df_offline_freq = pd.read_csv(os.path.join(base_path, 'offlinewithhash_shopname_frequency_with_parentname.csv'))
df_top_offline = pd.read_csv(os.path.join(base_path, 'top_1000_offline_shopnames_with_parents.csv'))

# Define standardization mapping for parent names
standard_parent_names = {
    'WAL-MART': 'Walmart',
    'Wal-Mart': 'Walmart',
    'Walmart Inc': 'Walmart',
    'AMAZON': 'Amazon',
    'AMZN': 'Amazon',
    'AMZN.COM': 'Amazon',
    'Amazon.com': 'Amazon',
    'PRIMENOWTIPS': 'Amazon',
    'AMAZON PRIME': 'Amazon',
    'PRIMEPANTRY': 'Amazon',
    'AMAZON MARK': 'Amazon',
    'VERIZONWRLSS': 'T-Mobile',
    'VERIZON': 'T-Mobile',
    'T-MOBILE': 'T-Mobile',
    'TMOBILE': 'T-Mobile',
    'Grubhub': 'Grubhub',
    'YELP-GRUBHUB': 'Grubhub',
    'GUM.CO/CC': 'Gumroad',
    'GUMROAD.CO': 'Gumroad',
    'GUMROAD': 'Gumroad',
    'AT&T': 'AT&T',
    'GOFNDME': 'GoFundMe',
    'NETFLIX': 'Netflix',
    'UBER': 'Uber',
    'SQUARE': 'Square',
    'IKEA': 'Ikea',
    'CHEWY': 'Chewy',
    'CHWYINC': 'Chewy',
    'ADOBE': 'Adobe',
    'VUDU': 'Vudu',
    'SPOTIFY': 'Spotify',
    'CRUMBL': 'Crumbl',
    'EBAY': 'eBay',
    'TARGET': 'Target',
    'DISCORD': 'Discord',
    'INSTACART': 'Instacart',
    'DOORDASH': 'DoorDash',
    'DELIVERY': 'DoorDash',
    'UPWORK': 'Upwork',
    'LINKEDINPRE': 'LinkedIn',
    'LINKEDIN PRE': 'LinkedIn',
    'NIKE': 'Nike',
    'COSTCO': 'Costco',
    'WALMART': 'Walmart',
    'MACYS': 'Macy\'s',
    'SEPHORA': 'Sephora',
    'REI': 'REI',
    'SHEIN': 'Shein',
    'DELTA': 'Delta Airlines',
    'AMTRAK': 'Amtrak',
    'GEICO': 'GEICO',
    'BLOCKCHAIN': 'Blockchain.com',
    # Add more as needed
}

# Normalize function
def normalize_parent_name(name):
    if pd.isna(name):
        return name
    name_clean = name.strip().upper()
    for key in standard_parent_names:
        if key.upper() in name_clean:
            return standard_parent_names[key]
    return name.strip()

# Apply normalization
df_online['parent name'] = df_online['parent name'].apply(normalize_parent_name)
df_offline_freq['parent name'] = df_offline_freq['parent name'].apply(normalize_parent_name)
df_top_offline['parent name'] = df_top_offline['parent name'].apply(normalize_parent_name)

# Save cleaned files
df_online.to_csv(os.path.join(base_path, 'cleaned_full_1000_shopnames_mapped_Online.csv'), index=False)
df_offline_freq.to_csv(os.path.join(base_path, 'cleaned_offlinewithhash_shopname_frequency_with_parentname.csv'), index=False)
df_top_offline.to_csv(os.path.join(base_path, 'cleaned_top_1000_offline_shopnames_with_parents.csv'), index=False)

print("Parent name standardization complete and files saved.")
