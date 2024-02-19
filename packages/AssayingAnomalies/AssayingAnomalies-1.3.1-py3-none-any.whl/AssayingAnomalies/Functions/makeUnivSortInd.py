import numpy as np
import pandas as pd
from AssayingAnomalies.Functions.assignToPtf import assignToPtf


def makeUnivSortInd(var, ptfNumThresh, breaksFilterInd=None, portfolioMassInd=None):

    # Validate inputs
    if not (isinstance(var, pd.DataFrame) or isinstance(var, np.ndarray)):
        raise ValueError("Input 'var' must be a DataFrame or a NumPy array.")

    # Convert input DataFrame to Numpy array
    if isinstance(var, pd.DataFrame):
        var = var.values

    if not np.isscalar(ptfNumThresh) and not isinstance(ptfNumThresh, (np.ndarray, list)):
        raise ValueError("Input 'ptfNumThresh' must be a scalar, list, or a NumPy array.")

    if breaksFilterInd is not None:
        if not (isinstance(breaksFilterInd, pd.DataFrame) or isinstance(breaksFilterInd, np.ndarray)):
            raise ValueError("Input 'breaksFilterInd' must be a DataFrame, a NumPy array, or None.")
        if var.shape != breaksFilterInd.shape:
            raise ValueError(f"Input 'breaksFilterInd' has shape {breaksFilterInd.shape} but 'var' has shape {var.shape}.")

    if portfolioMassInd is not None:
        if not (isinstance(portfolioMassInd, pd.DataFrame) or isinstance(portfolioMassInd, np.ndarray)):
            raise ValueError("Input 'portfolioMassInd' must be a DataFrame, a NumPy array, or None.")
        if var.shape != portfolioMassInd.shape:
            raise ValueError("Input 'portfolioMassInd' must have the same shape as 'var'.")

    # If user passed a list instead of numpy array for ptfNumThresh, we will need to change it to numpy array
    if isinstance(ptfNumThresh, list):
        ptfNumThresh = np.array(ptfNumThresh)

    # Determine the breakpoints
    nPtfThresh = len(ptfNumThresh) if isinstance(ptfNumThresh, np.ndarray) else 1

    if nPtfThresh > 1:
        # User entered the breakpoints directly
        bpts = ptfNumThresh
    else:
        # User entered the number of portfolios, so we need to create the breakpoints
        bpts = np.nan * np.empty(ptfNumThresh - 1)
        for i in range(1, ptfNumThresh):
            bpts[i - 1] = i * 100 / ptfNumThresh

    # Check if we are doing cap-weighted breaks
    if portfolioMassInd is None:
        portfolioMassInd = np.ones(var.shape)
    if not np.array_equal(portfolioMassInd, 1):
        # In this case, the user entered a portfolio mass matrix (e.g., market cap)

        portfolioMassInd[np.isnan(var)] = np.nan

        # We'll sort on the variable first & calculate the cumulative market cap
        I = np.argsort(var, axis=1)
        r_ind = np.any(np.isfinite(var), axis=1)
        tempvar = np.empty(var.shape)
        tempvar[:] = np.nan

        for i in np.where(r_ind)[0]:
            temp = portfolioMassInd[i, I[i, :]]
            t_ind = np.isnan(temp)
            temp[t_ind] = 0
            temp = np.cumsum(temp)
            temp = temp / temp[-1]
            temp[t_ind] = np.nan
            tempvar[i, I[i, :]] = temp

        # Assign based on the breakpoints
        bpts = np.concatenate(([0], bpts)) / 100

        ind = np.zeros(var.shape)
        for i in bpts:
            ind = ind + (tempvar > i) # TODO:N Here is causing the RuntimeWarning. Change to np.where(~np.isnan(tempvar), tempvar > i, False)
    else:
        # In this case, we are not doing cap-weighting

        if breaksFilterInd is None:
            breaksFilterInd = np.ones(var.shape)

        # If breaksFilterInd is a matrix, we'll assign nan to observations
        # which we don't want to use for breakpoints (e.g., if breaksFilterInd
        # is an indicator of NYSE stocks, we'll make non-NYSE entries nan)
        if breaksFilterInd is not None:
            breaksFilterInd[breaksFilterInd == 0] = np.nan

        # Calculate the percentiles for var by multiplying by the
        # breaksFilterInd. By default, we'll just multiply by 1. if
        # breaksFilterInd is NYSE, then we only use NYSE stocks for the
        # breakpoints.
        pctileBpointsMat = np.nanpercentile(var * (breaksFilterInd if breaksFilterInd is not None else 1), bpts, axis=1).T

        # Pass the var matrix and the percentile breakpoints matrix to
        # assignToPtf, which returns the indicator matrix for the portfolios
        ind = assignToPtf(var, pctileBpointsMat)

    return ind


# saveFolder = r'/home/jlaws13/PycharmProjects/AssayingAnomalies_root/Data/CRSP/'
# me = pd.read_csv(saveFolder + 'me.csv', index_col=0).astype(float)
# NYSE = pd.read_csv(saveFolder + 'NYSE.csv', index_col=0)
# test_ind = makeUnivSortInd(-me, 10, breaksFilterInd=NYSE)
# test_ind = makeUnivSortInd(-me, [30, 70], breaksFilterInd=NYSE)
