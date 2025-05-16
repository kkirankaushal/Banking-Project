import pandas as pd

# Define the file path
#file_path = "/mmfs1/projects/f8d7c0/2024-25/Gate City Bank/Kiran/ND_MN_Filtered_Data_With_Source.csv"
df = pd.read_csv(file_path)
base_path = Path("use relative path to your data folder")

# List of valid city names to check within TERM_ADDR
city_list = [
    "Fargo", "West Fargo", "Moorhead", "Mayville", "Wahpeton", "Fergus Falls",
    "Grand Forks", "Jamestown", "Alexandria", "Park River", "Carrington",
    "Devils Lake", "Waite Park", "Sauk Rapids", "St. Cloud", "Bismarck", 
    "Mandan", "Elk River", "Minot", "Mohall", "Dickinson", "Hettinger", "Williston"
]

# Ensure proper string types
df["Cities"] = df["Cities"].fillna("").astype(str)
df["TERM_ADDR"] = df["TERM_ADDR"].astype(str)

# Mask for rows where Cities is blank
mask_empty_city = df["Cities"].str.strip() == ""

# Attempt to fill missing Cities from TERM_ADDR
for city in city_list:
    match_mask = mask_empty_city & df["TERM_ADDR"].str.contains(city, case=False, na=False)
    df.loc[match_mask, "Cities"] = city

# Save the updated file
output_file = "/mmfs1/projects/f8d7c0/2024-25/Gate City Bank/Kiran/ND_MN_Cities_Filled_From_TERMADDR.csv"
df.to_csv(output_file, index=False)

print(f"Cities column filled and saved to: {output_file}")
