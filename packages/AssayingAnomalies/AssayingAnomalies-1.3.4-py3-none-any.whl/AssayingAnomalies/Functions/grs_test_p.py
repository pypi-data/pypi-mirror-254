import numpy as np
from scipy.stats import f


def grs_test_p(results):
    # Initialize a few variables
    pvals = np.ones(2)
    dfs = np.zeros((2, 2))
    Fstats = np.ones(2)

    # Store a few variables
    nPtfs = results['pret'].shape[1]
    nMonths = np.sum(np.isfinite(results['pret'][:, 0]))
    nFactors = results['nFactors']

    # Calculate the GRS stat for the full model
    # Get the degrees of freedom
    dfs[0, :] = [nPtfs, nMonths - nPtfs - nFactors]

    indFinite = np.isfinite(np.sum(results['pret'], axis=1)) & np.isfinite(np.sum(results['factors'], axis=1))

    # Calculate the numerator
    numer = results['alpha'][:nPtfs].T @ np.linalg.inv(np.cov(results['resid'][indFinite][:, :nPtfs].T)) @ \
            results['alpha'][:nPtfs]
    numer = numer / 100**2  # correct for percentage return multiplication

    # Calculate the denominator
    f_mat = results['factors'][indFinite] # the factor time series

    # for i in range(nFactors):
    #     f_mat.append(results['factorLoadings'][i][indFinite])
    #
    # f_mat = np.column_stack(f_mat)
    Ef = np.nanmean(f_mat, axis=0).reshape(-1, 1)
    denom = 1 + Ef.T @ np.linalg.inv(np.cov(f_mat, rowvar=False)) @ Ef

    # The statistic
    Fstats[0] = dfs[0, 1] / dfs[0, 0] * numer / denom

    pvals[0] = 1 - f.cdf(Fstats[0], dfs[0, 0], dfs[0, 1])

    # Calculate the GRS stat for the reduced model
    b = results['factorLoadings'].T
    # x = results['factorLoadings'][indFinite]
    x = f_mat.copy()
    a = np.tile(results['alpha'][:nPtfs], (np.sum(indFinite), 1)) / 100 # TODO:F Since alphas are already off by a factor of 100, this makes them off by another factor of 100. I need to correct this in estFactorRegs
    resid = results['resid'][indFinite, :nPtfs] # TODO:F residuals are not the same as those found in MATLAB.
    resxret = x @ b + a + resid

    # Calculate the numerator
    numer = results['xret'][:nPtfs].T @ np.linalg.inv(np.cov(resxret, rowvar=False)) @ results['xret'][:nPtfs]
    numer = numer / 100**2  # correct for percentage return multiplication
    denom = 1
    dfs[1, :] = [nPtfs, nMonths - nPtfs]

    # The statistic
    Fstats[1] = dfs[1, 1] / dfs[1, 0] * numer / denom
    pvals[1] = 1 - f.cdf(Fstats[1], dfs[1, 0], dfs[1, 1])

    return pvals, Fstats, dfs


# # Test the function
# import scipy.io
# import os
# from AssayingAnomalies import Config
# from AssayingAnomalies.Functions.makeBivSortInd import makeBivSortInd
#
# params = Config()
# params.prompt_user()
# params.make_folders()
# path = r"C:\Users\josh\OneDrive - University at Buffalo\Desktop\Spring_2023\AssayingAnomalies-main\AssayingAnomalies-main\Data" + os.sep
# R = scipy.io.loadmat(path + 'R.mat')['R']
# # R = pd.read_csv(path + 'R.csv', index_col=0)
# me = scipy.io.loadmat(path + 'me.mat')['me']
# NYSE = scipy.io.loadmat(path + 'NYSE.mat')['NYSE']
# ind1 = makeBivSortInd(me, 5, R, 5)
# ret = scipy.io.loadmat(path + 'ret.mat')['ret']
# dates = scipy.io.loadmat(path + os.sep + 'CRSP' + os.sep + 'dates.mat')['dates']
# dates = dates.flatten()
#
# # Run a univariate sort to get the underlying portfolios
# res = runUnivSort(params=params, ret=ret, ind=ind1, mcap=me, dates=dates)
