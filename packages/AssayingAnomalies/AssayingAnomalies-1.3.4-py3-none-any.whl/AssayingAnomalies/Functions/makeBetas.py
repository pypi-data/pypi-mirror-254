import pandas as pd
import numpy as np
import os
from datetime import datetime
import statsmodels.api as sm
from statsmodels.regression.rolling import RollingOLS


def makeBetas(params):
    # Timekeeping
    print(f"\nNow working on making the betas. Run started at {datetime.now()}\n")

    crsp_path = params.crspFolder + os.sep
    daily_crsp_path = params.daily_crsp_folder + os.sep
    ff_path = params.ff_data_folder + os.sep

    "Start with the Frazzini - Pedersen betas"
    print(f"\nMaking Frazzini-Pedersen (2014) betas first.\n")

    # load necessary inputs
    dret = pd.read_csv(daily_crsp_path + 'dret.csv', index_col=0).astype(float)
    ff = pd.read_csv(crsp_path + 'ff.csv', index_col=0).astype(float)
    dff = pd.read_csv(ff_path + 'dff.csv', index_col=0).astype(float)
    ret = pd.read_csv(crsp_path + 'ret.csv', index_col=0).astype(float)

    # Convert to datetime indices
    dret.index = pd.to_datetime(dret.index, format='%Y%m%d')
    dff.index = pd.to_datetime(dff['dates'], format='%Y%m%d')
    ret.index = pd.to_datetime(ret.index.astype(int), format='%Y%m')

    # Store the excess stock returns
    rptdRf = np.tile(dff['rf'], (ret.shape[1], 1)).T
    dxret = dret - rptdRf

    # Store the 3-day excess returns and market returns
    # dret3 = (1 + dxret).rolling(window=3).cumprod() - 1
    dret3 = (1 + dxret).shift(1) * (1 + dxret).shift(2) * (1 + dxret).shift(3) - 1
    dmkt3 = (1 + dff['mkt']).shift(1) * (1 + dff['mkt']).shift(2) * (1 + dff['mkt']).shift(3) - 1

    # Compute rolling 1-year standard deviations
    stock_std = np.log(1 + dxret).rolling(window=252, min_periods=120).std()
    mkt_std = np.log(1 + dff['mkt']).rolling(window=252, min_periods=120).std()

    # Compute rolling 5-year correlations of 3-day excess returns with 3-day market returns
    corr = np.log(1 + dret3).rolling(window=252 * 5, min_periods=750).corr(np.log(1 + dmkt3))

    # Calculate beta = rho * (sigma_i / sigma_m)
    betas = corr * stock_std / np.tile(mkt_std, (dret.shape[1], 1)).T

    # Apply the shrinkage towards 1; Reduce the impact of extreme values.
    bfp = 0.6 * betas + 0.4

    print("\nNow making Ivo's OLS, Dimson Correction, Vasicek shrinkage, 'standard', and Ivo Welch betas.\n")

    """
    Ivo's OLS benchmark - 1 year of daily data, 1 mkt lag, no shrinkage.
    Dimson correction - add one more lag of mkt.
    Vasicek shrinkage - similar to what LSY use.
    Standard - 1 market lag, shrinkage to 1.
    Ivo Welch's betas
    """
    # Calculate lagged market returns
    lagged_dmkt = pd.DataFrame(dff['mkt'], index=dff.index).shift(1)

    # Calculate the Ivo Welch winsorized excess returns
    lower_bound = -2 * dff['mkt']
    upper_bound = 4 * dff['mkt']

    # Winsorize the excess returns data
    # Note: `clip` method is used for winsorization
    dxret_winsorized = dxret.clip(lower=lower_bound, upper=upper_bound, axis=0)

    # Create empty arrays to store the betas
    betas_ols = np.empty_like(dret)
    betas_dim = np.empty_like(dret)
    betas_sw = np.empty_like(dret)
    betas_vck = np.empty_like(dret)

    # Create empty arrays to store OLS standard errors
    betas_ols_serrors = np.empty_like(dret)

    # Create lagged excess return matrix
    x1 = pd.DataFrame(sm.add_constant(dff['mkt']), index=dret.index)
    x2 = x1.merge(lagged_dmkt, how='outer', on=x1.index).iloc[:, 1:]
    x2.index = dret.index

    # Calculate OLS, Dimson , and Ivo Welch betas
    for i, permno in enumerate(dret.columns[1:]):
        # Benchmark OLS betas
        # betas_ols[:, i] = RollingOLS(dxret.iloc[:, i], x1, window=252, min_nobs=120).fit(params_only=True).params.iloc[:, 1]
        res = RollingOLS(dxret.iloc[:, i], x1, window=252, min_nobs=120).fit()
        betas_ols[:, i] = res.params.iloc[:, 1]
        betas_ols_serrors[:, i] = res.bse.iloc[:, 1]

        # Dimson correction - add 1 lag of mkt
        res = RollingOLS(dxret.iloc[:, i], x2, window=252, min_nobs=120).fit(params_only=True).params
        betas_dim[:, i] = res.iloc[:, 1] + res.iloc[:, 2]

        # Ivo's betas - use the winsorized returns (dxretw)
        betas_sw[:, i] = RollingOLS(dxret_winsorized.iloc[:, i], x1, window=252, min_nobs=120).fit(params_only=True).params.iloc[:, 1]

    # Calculate the Vasicek shrinkage betas
    for i in range(betas_ols.shape[0]):  # Loop over time periods
        sigmaSqI = betas_ols_serrors[i, :] ** 2
        sigmaSqT = np.nanvar(betas_ols[i, :])
        wvck = sigmaSqT / (sigmaSqI + sigmaSqT)
        mean_beta = np.nanmean(betas_ols[i, :])
        betas_vck[i, :] = wvck * betas_ols[i, :] + (1 - wvck) * mean_beta

    # Calculate standard betas
    betas_std = 0.6*betas_dim + 0.4

    pd.DataFrame(betas_std, index=dret.index, columns=dret.columns).to_csv(crsp_path + 'betas_std.csv')
    pd.DataFrame(betas_ols, index=dret.index, columns=dret.columns).to_csv(crsp_path + 'betas_ols.csv')
    pd.DataFrame(betas_sw, index=dret.index, columns=dret.columns).to_csv(crsp_path + 'betas_sw.csv')
    pd.DataFrame(betas_vck, index=dret.index, columns=dret.columns).to_csv(crsp_path + 'betas_vck.csv')
    pd.DataFrame(betas_dim, index=dret.index, columns=dret.columns).to_csv(crsp_path + 'betas_dim.csv')

    print(f"Set-up is complete. Run ended at {datetime.now()}")
