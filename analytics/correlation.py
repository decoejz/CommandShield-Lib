from definition import order


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
            for alg in order:
                # raw_data[raw_data["algorithm"] != "NO_SIGN"]
                operation = data[app][op].copy()
                operation = operation[operation["algorithm"] == alg]
                operation = operation.drop(["app", "algorithm"], axis=1)

                if op == "verify":
                    operation = operation.drop(["valid"], axis=1)

                correlation = operation.corr()

                print(f"Correlation matrix for {app} - {op} - {alg}:")
                print(correlation)
