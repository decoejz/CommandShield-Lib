import matplotlib.pyplot as plt
from definition import order, algorithms


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
            plt.title(f"{app} - {op.capitalize()}")
            plt.xlabel("Message Size (bytes)", fontsize=24, fontdict={"weight": "bold"})
            plt.ylabel(f"Time {"Log"if log_data else ""} (μs)")
            plt.xticks(fontsize=20)
            plt.yticks(fontsize=20)
            plt.legend(fontsize=20)
            plt.grid(True)
            plt.subplots_adjust(
                left=0.07, right=0.994, top=0.99, bottom=0.108, wspace=0.2, hspace=0.2
            )

    plt.show()
