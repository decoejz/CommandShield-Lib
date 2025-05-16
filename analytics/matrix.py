import pandas as pd
import seaborn as sns
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

algorithms = ["RSA", "ECDSA", "EDDSA"]


def correlation_analysis(data):
    """
    Generate graphs for the given data.
    Parameters:
    data (dict): A dictionary containing the split data for Autopilot and GroundControl.
    The structure of the dictionary is as follows:
    {
        'Autopilot': {
            'sign': DataFrame,
            'verify': DataFrame
        },
        'GroundControl': {
            'sign': DataFrame,
            'verify': DataFrame
        }
    }
    Returns:
    None
    """

    for app in data.keys():
        for op in data[app].keys():
            for alg in algorithms:
                # raw_data[raw_data["algorithm"] != "NO_SIGN"]
                operation = data[app][op].copy()
                operation = operation[operation["algorithm"] == alg]
                operation = operation.drop(["app", "algorithm"], axis=1)

                if op == "verify":
                    operation = operation.drop(["valid"], axis=1)

                correlation = operation.corr()
                print(f"Correlation matrix for {app} - {op} - {alg}:")
                print(correlation)

            # mask = np.triu(np.ones_like(correlation, dtype=bool))

            # cmap = sns.diverging_palette(230, 20, as_cmap=True)

            # sns.heatmap(
            #     correlation,
            #     mask=mask,
            #     cmap=cmap,
            #     vmax=0.3,
            #     center=0,
            #     square=True,
            #     linewidths=0.5,
            #     cbar_kws={"shrink": 0.5},
            # )

            # plt.show()

    # qgc_verify = data["GroundControl"]["verify"].copy()
    # print(qgc_verify.head())
    # qgc_verify["app"] = qgc_verify["app"].apply(
    #     lambda x: 0 if x == "GroundControl" else 1
    # )
    # qgc_verify["valid"] = qgc_verify["valid"].apply(
    #     lambda x: 0 if x == "INVALID" else 1
    # )
    # qgc_verify["algorithm"] = qgc_verify["algorithm"].apply(map_algorithm)

    # df_analysis = qgc_verify[qgc_verify["algorithm"] == "RSA"].drop(
    #     ["app", "valid", "algorithm"], axis=1
    # )
    # correlation = df_analysis.corr()
    # print(correlation)

    # df_analysis = qgc_verify[qgc_verify["algorithm"] == "RSA"].drop(
    #     ["app", "valid", "algorithm"], axis=1
    # )
    # correlation = df_analysis.corr()
    # print(correlation)

    # df_analysis = qgc_verify[qgc_verify["algorithm"] == "RSA"].drop(
    #     ["app", "valid", "algorithm"], axis=1
    # )
    # correlation = df_analysis.corr()
    # print(correlation)

    # df_analysis = qgc_verify[qgc_verify["algorithm"] == "RSA"].drop(
    #     ["app", "valid", "algorithm"], axis=1
    # )
    # correlation = df_analysis.corr()
    # print(correlation)
    # plot = sn.heatmap(correlation, annot=True, fmt=".1f", linewidths=0.6)
    # plt.show()
