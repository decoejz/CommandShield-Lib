import pandas as pd

dataframes = []

for s in range(1, 4):
    df = pd.read_csv(f"./scenario{s}/all.csv", header=None)
    dataframes.append(df)

output_file = f"./all.csv"
combined_df = pd.DataFrame()

# Concatenate all dataframes
combined_df = pd.concat(dataframes, axis=0, ignore_index=True)

# Save the combined dataframe to a new CSV file
combined_df.to_csv(output_file, index=False, header=False)
