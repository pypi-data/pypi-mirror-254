from collections import Counter
from pkg_pyknnclassifier.find_neighbors import find_neighbors
import numpy as np
import pandas as pd


def predict(train_X, train_y, unlabel_df, pred_method = "hard", k=3):
    """
    This function predicts the labels of the unlabled observations based on the similarity score calculated from Euclidean distance.

    Parameters
    ----------
    train_X : pd.DataFrame
        The data frame containing labeled observations, but without the label.

    train_y : numpy.array
        The array containing labels in the training dataset

    unlabel_df : pd.DataFrame
        The data frame containing unlabeld observations.

    pred_method : str
        'soft' or 'hard'.

    k : int
        The number of nearest neighbors to consider for making predictions.

    Returns
    -------
    array
        An array containing predicted labels for the observations.

    Examples
    --------
    df = pd.DataFrame({'A':[0.5, 0.2, 0.4],
                       'B':[0.3, 0.2, 0.5]})
    predict(df)
    """

    # Check if train_X and train_y have the same number of rows
    if len(train_X) != len(train_y):
        raise ValueError("train_X and train_y must have the same number of rows.")
    
    # Check if pred_method is either 'hard' or 'soft'
    if pred_method not in ["hard", "soft"]:
        raise ValueError("pred_method must be either 'hard' or 'soft'.")
    
    # Check if k is positive and less than the number of labeled examples
    if not (0 < k <= len(train_X)):
        raise ValueError("k must be positive and less than or equal to the number of labeled examples.")

    # Initializing list to track the predictions
    predictions = []
    X_array = train_X.values
    unlabel_array = unlabel_df.values

    # Loop through each observation
    for data_point in unlabel_array:
        neighbors_idxs = find_neighbors(X_array, data_point, k)
        neighbor_labels = train_y[neighbors_idxs]
        cnt = Counter(neighbor_labels)

        if pred_method == "hard":
            label = cnt.most_common()[0][0]
            predictions.append(label)
        if pred_method == "soft":
            if k > 1:
                prob = cnt.most_common()[0][1] / (
                    cnt.most_common()[0][1] + cnt.most_common()[1][1]
                )
            else:
                prob = 1
            predictions.append(prob)

    # Return the predicted labels
    return np.array(predictions)
