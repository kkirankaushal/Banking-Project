import pandas as pd

# Define full paths to the files
base_path = "/mmfs1/projects/f8d7c0/2024-25/Gate City Bank/Kiran/"
files = [
    "Processed_Online_With_ParentName_Classified.csv",
    "Processed_Offline_With_ParentName_Classified.csv",
    "Processed_Offlinewithhash_With_ParentName_Classified.csv"
]

# States to filter
states = ["ND", "MN"]

# Collect filtered data
combined_data = []

for file in files:
    file_path = base_path + file
    try:
        df = pd.read_csv(file_path)
        filtered_df = df[df["State"].isin(states)].copy()
        filtered_df["Source_File"] = file
        combined_data.append(filtered_df)
    except Exception as e:
        print(f"Error processing {file}: {e}")

# Combine and save
if combined_data:
    final_df = pd.concat(combined_data, ignore_index=True)
    output_file = base_path + "ND_MN_Filtered_Data_With_Source.csv"
    final_df.to_csv(output_file, index=False)
    print(f"File saved successfully at: {output_file}")
else:
    print("No data was filtered or files were missing.")
