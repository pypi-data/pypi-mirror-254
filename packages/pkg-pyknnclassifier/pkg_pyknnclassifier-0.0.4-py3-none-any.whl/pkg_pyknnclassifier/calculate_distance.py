import numpy as np


def calculate_distance(obs_1, obs_2, method="Euclidean"):
    """
    This function calculates the Euclidean distance between two observations for the KNN model to find the similarity score.

    Parameters
    ----------
    obs_1 : array
        An array containing the features of the first observation.
    obs_2 : array
        An array containing the features of the second observation.
    method : str, optional
        The distance metric to use. Default is "Euclidean".
        Possible values: "Euclidean", "Manhattan", "Chebyshev".

    Returns
    -------
    float
        Float representing a euclidean distance between two observations.

    Examples
    --------
    obs_1 = [0.81, 0.2, -0.86, 0.08]
    obs_2 = [-0.39, 0.24, -0.77, 0.17]
    dist = calculate_distance(obs_1, obs_2)
    print(f"Euclidean Distance between two observations is {dist}")
    """

    if not isinstance(obs_1, (list, np.ndarray)) or not isinstance(obs_2, (list, np.ndarray)):
        raise TypeError("Input must be a list or numpy array")
    
    if len(obs_1) != len(obs_2):
        raise ValueError("Failed length test")
    
    obs_1, obs_2 = np.array(obs_1), np.array(obs_2)

    # Check for the distance metrics that the user would like to use
    if method == "Manhattan":
        distance = np.sum(np.abs(np.array(obs_1) - np.array(obs_2)))
    elif method == "Chebyshev":
        distance = np.max(np.abs(np.array(obs_1) - np.array(obs_2)))
    elif method == "Euclidean":
        distance = (np.sum((np.array(obs_1) - np.array(obs_2)) ** 2)) ** 0.5
    else:
        raise ValueError("invalid method")

    # Returning distance calculated based on the distance metrics chosen
    return distance
