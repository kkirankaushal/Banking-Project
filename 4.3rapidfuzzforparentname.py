import pandas as pd
from rapidfuzz import process, fuzz

# Load  file
df = pd.read_csv("/mmfs1/projects/f8d7c0/2024-25/Gate City Bank/Kiran/top_1000_offline_shopnames.csv")
df['ShopName'] = df['ShopName'].astype(str).str.strip().str.upper()

# Reference parent company list
parent_companies = [
    "Walmart", "Sam's Club", "Target", "Love's", "Costco", "CVS Health", "Walgreens",
    "McDonald's", "Burger King", "Dunkin Donuts", "Baskin Robbins", "Amazon", "PayPal",
    "Kroger", "Starbucks", "ALDI", "Safeway", "TJX Companies", "Ross Stores", "Best Buy",
    "The Home Depot", "Lowe's", "7-Eleven", "Circle K", "Pilot Flying J", "Chevron", "Shell",
    "ExxonMobil", "IHOP", "Denny's", "Arby's", "Jimmy John's", "Subway", "Sonic Drive-In",
    "Chipotle", "Panera Bread", "Domino's Pizza", "Papa John's", "Dollar General",
    "Dollar Tree", "Joann Stores", "AutoZone", "O'Reilly Auto Parts", "Sephora", "Apple",
    "FedEx", "UPS", "T-Mobile", "Verizon", "AT&T", "Cost Plus", "PetSmart", "GameStop",
    "Trader Joe's", "Panda Express", "CVS", "Wal-Mart", "H&M", "Marshalls", "HomeGoods",
    "Office Depot", "Goodwill", "Zaxby's", "Texas Roadhouse", "Caribou Coffee",
    "Academy Sports", "Ulta", "JoAnn Fabrics", "Kohl's", "KFC"
]

def get_closest_parent(shopname):
    result = process.extractOne(shopname, parent_companies, scorer=fuzz.partial_ratio)
    if result and result[1] >= 80:  # result[1] is the score
        return result[0]            # result[0] is the matched string
    return "Unknown"


# Apply logic
df['Parent Name'] = df['ShopName'].apply(get_closest_parent)

# Save the final result
output_path = "/mmfs1/projects/f8d7c0/2024-25/Gate City Bank/Kiran/top_1000_offline_shopnames_with_parents.csv"
df.to_csv(output_path, index=False)

print("Parent company names added!")
print(f"File saved to: {output_path}")
