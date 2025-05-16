import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
from definition import *


def graph_generator(data, log_data=False):
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
            operation = data[app][op]

            # Prepare the data for plotting
            plt.figure(figsize=(10, 6))

            for alg in order:
                alg_data = operation[operation["algorithm"] == alg]

                if not alg_data.empty:
                    plt.plot(
                        alg_data["len"],
                        alg_data["time"],
                        marker=algorithms[alg]["marker"],
                        color=algorithms[alg]["color"],
                        label=alg,
                        linestyle="",
                    )
                    if log_data:
                        plt.yscale("log")

            # Customize the plot
            plt.title(
                f"{"Logarithmic " if log_data else ""}Time Performance ({app} - {op.capitalize()})"
            )
            plt.xlabel("Message Size (bytes)")
            plt.ylabel(f"Time {"Log"if log_data else ""} (μs)")
            plt.legend()
            plt.grid(True)

    plt.show()


def boxplot_generator_backup(data, log_data=False):
    """
    Generate a boxplot for the GroundControl verify operation based on the time.
    Parameters:
    data (dict): A dictionary containing the split data for Autopilot and GroundControl.
    Returns:
    None
    """
    for app in data.keys():
        for op in data[app].keys():
            operation = data[app][op]

            if not operation.empty:
                operation.boxplot(
                    column="time",
                    by="algorithm",
                    grid=True,
                    showfliers=False,
                    widths=0.6,
                    patch_artist=True,
                    boxprops=dict(facecolor="white", color="black"),
                    medianprops=dict(color="red", linewidth=2),
                    whiskerprops=dict(color="black"),
                    capprops=dict(color="blue", linewidth=2),
                )
                if log_data:
                    plt.yscale("log")

                # Customize the plot
                plt.title(
                    f"{"Logarithmic " if log_data else ""}Boxplot of Time ({app} - {op.capitalize()})"
                )
                plt.suptitle("")  # Remove the default Pandas title
                plt.xlabel("Algorithm")
                plt.ylabel(f"Time {"Log"if log_data else ""} (μs)")
                plt.grid(True)

    plt.show()


def boxplot_generator(data, log_data=False):
    """
    Generate a boxplot for the GroundControl verify operation based on the time.
    Parameters:
    data (dict): A dictionary containing the split data for Autopilot and GroundControl.
    Returns:
    None
    """
    for app in data.keys():
        for op in data[app].keys():
            operation = data[app][op]

            if not operation.empty:
                operation["algorithm"] = pd.Categorical(
                    operation["algorithm"], categories=order, ordered=True
                )
                operation.boxplot(
                    column="time",
                    by="algorithm",
                    grid=True,
                    showfliers=False,
                    widths=0.6,
                    patch_artist=True,
                    boxprops=dict(facecolor="white", color="black"),
                    medianprops=dict(color="red", linewidth=2),
                    whiskerprops=dict(color="black"),
                    capprops=dict(color="blue", linewidth=2),
                )
                if log_data:
                    plt.yscale("log")

                plt.title(
                    f"{"Logarithmic " if log_data else ""}Boxplot of Time ({app} - {op.capitalize()})"
                )
                plt.suptitle("")  # Remove the default Pandas title
                plt.xlabel("Algorithm")
                plt.ylabel(f"Time {"Log"if log_data else ""} (μs)")
                plt.grid(True)

    plt.show()


def violin_generator(data, log_data=False):
    """
    Generate a boxplot for the GroundControl verify operation based on the time.
    Parameters:
    data (dict): A dictionary containing the split data for Autopilot and GroundControl.
    Returns:
    None
    """
    for app in data.keys():
        for op in data[app].keys():
            operation = data[app][op]

            plt.figure(figsize=(10, 6))

            for alg in order:
                alg_data = operation[operation["algorithm"] == alg]

                # print(f"Operation: {operation.head()}")
                if not alg_data.empty:
                    # operation.boxplot(column="time", by="algorithm", grid=True)
                    sns.violinplot(
                        x="algorithm",
                        y="time",
                        data=alg_data,
                        color=algorithms[alg]["color"],
                    )

                    if log_data:
                        plt.yscale("log")

                    # Customize the plot
                    plt.title(
                        f"{"Logarithmic " if log_data else ""}Violin plot of Time ({app} - {op.capitalize()})"
                    )
                    plt.suptitle("")  # Remove the default Pandas title
                    plt.xlabel("Algorithm")
                    plt.ylabel(f"Time {"Log"if log_data else ""} (μs)")
                    plt.grid(True)

    plt.show()


def hist_generator(data, log_data=False):
    """
    Generate histograms for the given data.
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
            operation = data[app][op]

            # Prepare the data for plotting
            plt.figure(figsize=(10, 6))

            for alg in order:
                alg_data = operation[operation["algorithm"] == alg]

                if not alg_data.empty:
                    plt.hist(
                        alg_data["time"],
                        bins=30,
                        histtype="step",  # Apenas contorno (sem preenchimento)
                        linewidth=2,  # Espessura da linha
                        color=algorithms[alg]["color"],  # Cor do contorno
                        alpha=1,
                        label=alg,
                    )
                    if log_data:
                        plt.yscale("log")

            # Customize the plot
            plt.title(
                f"{"Logarithmic " if log_data else ""}Histogram of Time ({app} - {op.capitalize()})"
            )
            plt.xlabel(f"Time {"Log"if log_data else ""} (μs)")
            plt.ylabel("Frequency")
            plt.legend()
            plt.grid(True)

    plt.show()
