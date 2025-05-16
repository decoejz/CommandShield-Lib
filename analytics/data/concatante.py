import os
import pandas as pd

folder = "./scenario3"
output_file = f"{folder}/all.csv"

dataframes = []

# Iterate through files in the folder
combined_df = pd.DataFrame()

for algorithm in os.listdir(folder):
    if algorithm.endswith(".DS_Store"):
        continue
    for file_name in os.listdir(f"{folder}/{algorithm}"):
        if file_name.endswith(".csv"):
            file_path = f"{folder}/{algorithm}/{file_name}"
            df = pd.read_csv(file_path, header=None)
            dataframes.append(df)

# Concatenate all dataframes
combined_df = pd.concat(dataframes, axis=0, ignore_index=True)

# Save the combined dataframe to a new CSV file
combined_df.to_csv(output_file, index=False, header=False)
