import pandas as pd

# File path
#file_path = "/mmfs1/projects/f8d7c0/2024-25/Gate City Bank/Kiran/ND_MN_Cities_With_ATM_Flag_Corrected.xlsx"
base_path = Path("use relative path to your data folder")

# Cities from user input (state removed, all uppercase)
valid_cities = [
    "ALEXANDRIA", "BISMARCK", "CARRINGTON", "DEVILS LAKE", "DICKINSON",
    "ELK RIVER", "FARGO", "FERGUS FALLS", "GRAND FORKS", "HETTINGER",
    "JAMESTOWN", "MANDAN", "MAYVILLE", "MINOT", "MOHALL", "MOORHEAD",
    "PARK RIVER", "SAUK RAPIDS", "ST. CLOUD", "WAHPETON", "WAITE PARK",
    "WEST FARGO", "WILLISTON"
]

# Read all sheets
excel_file = pd.ExcelFile(file_path)
sheet_names = excel_file.sheet_names
updated_sheets = {}

for sheet in sheet_names:
    df = pd.read_excel(file_path, sheet_name=sheet)
    
    # Standardize city names
    df['Cities'] = df['Cities'].astype(str).str.upper().str.strip()
    
    # Update ATM_Present
    df['ATM_Present'] = df['Cities'].apply(lambda city: 1 if city in valid_cities else 0)
    
    updated_sheets[sheet] = df

# Save to a new file
output_path = "/mmfs1/projects/f8d7c0/2024-25/Gate City Bank/Kiran/ND_MN_Cities_ATM_Updated.xlsx"
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    for sheet_name, df in updated_sheets.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Done. ATM_Present updated using exact city list. Saved to:")
print(output_path)
