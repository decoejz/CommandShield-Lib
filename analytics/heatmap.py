import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import json
from definition import order


data_file = "data/correlation_matrix.json"
with open(data_file, "r") as f:
    corr = json.load(f)

# Correlation data
df_heatmap = pd.DataFrame(corr, index=order)

# Heatmap generation
# sns.set(font_scale=1)
plt.figure(figsize=(8, 4))
sns.heatmap(
    df_heatmap,
    annot=True,
    cmap="coolwarm",
    center=0,
    fmt=".3f",
    linewidths=0.5,
    annot_kws={"fontsize": 20},
    cbar_kws={"shrink": 0.8},
)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.title("Pearson Correlation between message size and execution time")
plt.ylabel("Algorithm", fontsize=24, fontdict={"weight": "bold"})
plt.xlabel("Application and Operation", fontsize=21, fontdict={"weight": "bold"})
plt.tight_layout()
plt.xticks(rotation=0)
plt.yticks(rotation=0)
plt.show()
