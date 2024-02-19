import pandas as pd
import numpy as np
import os
from .rank_with_nan import rank_with_nan


def fill_missing_tcosts(params, tcosts):

    # Set path
    crsp_path = params.crspFolder + os.sep

    # Load variabled we need
    me = pd.read_csv(crsp_path + 'me.csv', index_col=0).astype(float)
    rme = rank_with_nan(me)

    IffVOL3 = pd.read_csv(crsp_path + 'IffVOL3.csv', index_col=0)
    rIVOL = rank_with_nan(IffVOL3)

    # Iterate over each date
    for date in range(rme.shape[0]):
        # Get the ranks for me and IVOL for this date
        rme_row = rme[date]
        rIVOL_row = rIVOL[date]

        # Calculate the differences in ranks for each pair of stocks
        # The result is a DataFrame where each cell [i, j] is the difference in rank between stock i and stock j
        rme_diff = rme_row[:, np.newaxis] - rme_row
        rIVOL_diff = rIVOL_row[:, np.newaxis] - rIVOL_row

        # Calculate Euclidean distance
        euclidean_distance = np.sqrt(rme_diff ** 2 + rIVOL_diff ** 2)

        # Fill diagonals with np.inf to avoid self-matching
        np.fill_diagonal(euclidean_distance, np.inf)

        # Replace nan values with np.inf in the euclidean_distance array
        euclidean_distance[np.isnan(euclidean_distance)] = np.inf

        # Closes matches
        min_indices = np.argmin(euclidean_distance, axis=1)

        # Select NaN values in tcosts_raw for this date
        mask = tcosts.iloc[date].isna()

        # Update NaN values using values from the closest match
        tcosts.iloc[date, mask] = tcosts.iloc[date, min_indices[mask]].values

    return tcosts

