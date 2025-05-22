from raw import process_raw_data
from split_data import split_data
from graph import graph_generator
from violin import violin_generator
from correlation import correlation_analysis

# File path
csv_file_path = f"data/all.csv"

# Import and process the data
raw_data = process_raw_data(csv_file_path)
splitted_data = split_data(raw_data)

# Calculate and print the correlation matrix
correlation_analysis(splitted_data)

# Generate graphs and violin plots
graph_generator(splitted_data, True)
violin_generator(splitted_data, True)
