import pandas as pd
import re
from pathlib import Path

# File path
#file_path = Path("/mmfs1/projects/f8d7c0/2024-25/Gate City Bank/Kiran/SQ_PAYPAL_SubShop_Combined.xlsx")
base_path = Path("use relative path to your data folder")
# Load data
df = pd.read_excel(file_path)
df.columns = df.columns.str.strip()

# Define keywords to truncate
address_keywords = [
    "STREET", "ST", "ROAD", "RD", "AVENUE", "AVE", "DRIVE", "DR", 
    "LANE", "LN", "BLVD", "PLACE", "PL", "SUITE", "UNIT", "WAY", "COURT", "CT"
]

# Combine as regex pattern
addr_pattern = r'\b(?:' + '|'.join(address_keywords) + r')\b'

# Define the cleaning function
def clean_subshop(garbage, city):
    if not isinstance(garbage, str):
        return None
    garbage = garbage.upper().strip()

    # Remove city if present
    if isinstance(city, str):
        city_upper = city.upper().strip()
        if city_upper in garbage:
            garbage = garbage.replace(city_upper, "").strip()

    # Remove at first number (includes number)
    garbage = re.split(r"\d", garbage)[0].strip()

    # Truncate at known address keywords
    garbage = re.split(addr_pattern, garbage)[0].strip()

    # Remove web/email fragments
    garbage = re.split(r"[@\.]", garbage)[0].strip()

    # Final clean-up: remove stray commas, dashes, etc.
    garbage = re.sub(r"[,\-]+$", "", garbage).strip()

    return garbage if garbage else None

# Apply cleaning
df["SubShop"] = df.apply(lambda row: clean_subshop(row["GarbageValue"], row["Cities"]), axis=1)

# Save as CSV
output_path = file_path.with_name("SQ_PAYPAL_SubShop_Cleaned.csv")
df.to_csv(output_path, index=False)

print(f"Cleaned CSV saved at: {output_path}")
