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
            plt.xlabel("Message Size (bytes)")
            plt.ylabel(f"Time {"Log"if log_data else ""} (μs)")
            plt.legend()
            plt.grid(True)

    plt.show()
