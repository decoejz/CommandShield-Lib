import matplotlib.pyplot as plt
import seaborn as sns
from definition import order, algorithms


def violin_generator(data, log_data=False):
    """
    Generate a boxplot for the GroundControl verify operation based on the time.
    Parameters:
    data (dict): A dictionary containing the split data for Autopilot and GroundControl.
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
    print("Generating violin plot...")
    for app in data.keys():
        for op in data[app].keys():
            operation = data[app][op]

            plt.figure(figsize=(10, 6))

            for alg in order:
                alg_data = operation[operation["algorithm"] == alg]

                if not alg_data.empty:
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
                    plt.xlabel("Algorithm", fontsize=24, fontdict={"weight": "bold"})
                    plt.ylabel(
                        f"Time {"Log"if log_data else ""} (μs)",
                        fontsize=24,
                        fontdict={"weight": "bold"},
                    )
                    plt.xticks(fontsize=20)
                    plt.yticks(fontsize=20)
                    plt.grid(True)
                    plt.subplots_adjust(
                        left=0.075,
                        right=0.995,
                        top=0.99,
                        bottom=0.11,
                        wspace=0.2,
                        hspace=0.2,
                    )

    plt.show()
