from raw import process_raw_data
from split_data import split_data
from graph import graph_generator, boxplot_generator, violin_generator, hist_generator
from matrix import correlation_analysis

scenario = 1
# csv_file_path = f"data/scenario{scenario}/all.csv"
csv_file_path = f"data/all.csv"

raw_data = process_raw_data(csv_file_path)
# removed_no_sign = raw_data[raw_data["algorithm"] != "NO_SIGN"]

splitted_data = split_data(raw_data)

# correlation_analysis(splitted_data)

graph_generator(splitted_data, True)
boxplot_generator(splitted_data, True)
violin_generator(splitted_data, True)
hist_generator(splitted_data, True)
