import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import statistics
import json
from definition import *


def extract_stats(data, scenario, alg):
    mean_stats = statistics.mean(data)
    median_stats = statistics.median(data)
    mode_stats = statistics.mode(data)

    try:
        modes_stats = statistics.multimode(data)
    except AttributeError:
        pass

    print()
    print("==================")
    print("=== Statistics ===")
    print(f"{RED}Scenario: {scenario}, Algorithm: {alg.upper()}{RESET}")
    print(f"Mean: {BLUE}{mean_stats}{RESET}")
    print(f"Median: {BLUE}{median_stats}{RESET}")
    print(f"Mode: {BLUE}{mode_stats}{RESET}")
    print(f"All modes: {BLUE}{modes_stats}{RESET}")


data_file = "data/mission_time.json"

# Open JSON file and read data
with open(data_file, "r") as f:
    scenarios = json.load(f)


colors = [algorithms[alg]["color"] for alg in algorithms]


for s in scenarios:
    df_stacked = pd.DataFrame(
        {
            "algorithm": np.repeat(
                list(scenarios[s].keys()),
                [len(values) for values in scenarios[s].values()],
            ),
            "time": np.concatenate(list(scenarios[s].values())),
        }
    )

    plt.figure(figsize=(10, 6))
    sns.violinplot(
        x="algorithm",
        y="time",
        hue="algorithm",
        legend=False,
        data=df_stacked,
        palette=colors,
        alpha=color_alpha,
    )
    # Set font sizes for axes labels and ticks
    plt.title(f"Scenario {s} - Time Consumption")
    plt.xlabel("Algorithm", fontsize=24, fontdict={"weight": "bold"})
    plt.ylabel("Time (s)", fontsize=24, fontdict={"weight": "bold"})
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    for alg in scenarios[s].keys():
        extract_stats(scenarios[s][alg], s, alg)

plt.show()
