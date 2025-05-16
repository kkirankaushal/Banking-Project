import pandas as pd
from pathlib import Path

# File path
file_path = Path("/mmfs1/projects/f8d7c0/2024-25/Gate City Bank/Kiran/Processed_Online_With_ParentName_Classified.csv")

# Load dataset
df = pd.read_csv(file_path)

# --- SubShop Extraction Functions ---
def extract_sq_subshop(desc):
    if isinstance(desc, str) and desc.upper().startswith("SQ *"):
        parts = desc.split("*", 1)[-1].strip().split()
        return " ".join(parts[:2]) if parts else None
    return None

def extract_paypal_subshop(desc):
    if isinstance(desc, str) and desc.upper().startswith("PAYPAL *"):
        parts = desc.split("*", 1)[-1].strip().split()
        return parts[0] if parts else None
    return None

# --- Filter and Process ---
# SQ * rows
sq_df = df[df["TXN_DESCRIPTION"].str.upper().str.startswith("SQ *")].copy()
sq_df["SubShop"] = sq_df["TXN_DESCRIPTION"].apply(extract_sq_subshop)

# PAYPAL * rows
paypal_df = df[df["TXN_DESCRIPTION"].str.upper().str.startswith("PAYPAL *")].copy()
paypal_df["SubShop"] = paypal_df["TXN_DESCRIPTION"].apply(extract_paypal_subshop)

# Combine
combined_df = pd.concat([sq_df, paypal_df], ignore_index=True)

# Save to Excel
output_file = "/mmfs1/projects/f8d7c0/2024-25/Gate City Bank/Kiran/SQ_PAYPAL_SubShop_Combined.xlsx"
combined_df.to_excel(output_file, index=False)

# Output row count
print(f"Total rows exported: {len(combined_df):,}")
print(f"File saved as: {output_file}")
