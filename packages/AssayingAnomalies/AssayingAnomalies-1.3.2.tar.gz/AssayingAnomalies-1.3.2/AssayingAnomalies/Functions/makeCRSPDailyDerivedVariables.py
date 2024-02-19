import numpy as np
import pandas as pd
from datetime import datetime
import os
import statsmodels.api as sm
from multiprocessing import Pool
import dask.dataframe as dd
from .getFFDailyFactors import getFFDailyFactors


def parallel_compute_ivol(i, j, col_index, ind1, ind3, dret, dmkt, dff3):
    # Regression for 1-month residual
    X = sm.add_constant(dmkt[ind1])  # Add a constant term
    y = dret.loc[ind1, j]
    model = sm.OLS(y.values, X.values, missing='drop')
    results = model.fit()
    ivol = np.sqrt(np.mean(results.resid ** 2))

    # Regression for FF3 1-month residual
    X_ff3 = dff3.loc[ind1]
    y = dret.loc[ind1, j]
    model_ff3 = sm.OLS(y.values, X_ff3.values, missing='drop')
    results_ff3 = model_ff3.fit()
    iffvol = np.sqrt(np.mean(results_ff3.resid ** 2))

    # Regression for 3-month residual
    X = sm.add_constant(dmkt[ind3])  # Add a constant term
    y = dret.loc[ind3, j]
    model = sm.OLS(y.values, X.values, missing='drop')
    results = model.fit()
    ivol3 = np.sqrt(np.mean(results.resid ** 2))

    # Regression for FF3 3-month residual
    X_ff3 = dff3.loc[ind3]
    y = dret.loc[ind3, j]
    model_ff3 = sm.OLS(y.values, X_ff3.values, missing='drop')
    results_ff3 = model_ff3.fit()
    iffvol3 = np.sqrt(np.mean(results_ff3.resid ** 2))

    return i, col_index, ivol, iffvol, ivol3, iffvol3


def parallel_compute_ivol(i, col_index, y1, X1, y3, X3, Xf1, Xf3):
    # Regression for 1-month residual
    # X = sm.add_constant(dmkt[ind1])  # Add a constant term
    # y = dret.loc[ind1, j]
    model = sm.OLS(y1, X1, missing='drop')
    results = model.fit()
    ivol = np.sqrt(np.mean(results.resid ** 2))

    # Regression for FF3 1-month residual
    # X_ff3 = dff3.loc[ind1]
    # y = dret.loc[ind1, j]
    model_ff3 = sm.OLS(y1, Xf1, missing='drop')
    results_ff3 = model_ff3.fit()
    iffvol = np.sqrt(np.mean(results_ff3.resid ** 2))

    # Regression for 3-month residual
    # X = sm.add_constant(dmkt[ind3])  # Add a constant term
    # y = dret.loc[ind3, j]
    model = sm.OLS(y3, X3, missing='drop')
    results = model.fit()
    ivol3 = np.sqrt(np.mean(results.resid ** 2))

    # Regression for FF3 3-month residual
    # X_ff3 = dff3.loc[ind3]
    # y = dret.loc[ind3, j]
    model_ff3 = sm.OLS(y3, Xf3, missing='drop')
    results_ff3 = model_ff3.fit()
    iffvol3 = np.sqrt(np.mean(results_ff3.resid ** 2))

    return i, col_index, ivol, iffvol, ivol3, iffvol3


def makeCRSPDailyDerivedVariables(params):
    # Timekeeping
    print(f"\nNow working on making CRSP daily derived variables. Run started at {datetime.now()}.\n")

    # set the path to crsp daily folder
    crsp_folder = params.crspFolder + os.sep

    # set the path to crsp daily folder
    daily_crsp_folder = params.daily_crsp_folder + os.sep

    # set the path to ff data folder
    ff_data_folder = params.ff_data_folder + os.sep

    "Make market capitalization"
    # dprc = pd.read_csv(daily_crsp_folder + 'dprc.csv', index_col=0)
    # dshrout = pd.read_csv(daily_crsp_folder + 'dshrout.csv', index_col=0)
    # dme = np.abs(dprc) * dshrout / 1000
    #
    # # replace zeros with nan
    # dme.replace(0, np.nan, inplace=True)
    # dme.to_csv(daily_crsp_folder + 'dme.csv')
    dme = np.abs(dd.read_parquet(daily_crsp_folder + 'dprc.parquet')) \
          * dd.read_parquet(daily_crsp_folder + 'dshrout.parquet') / 1000
    dme = dme.where(dme != 0, np.nan)
    dme = dme.compute()
    dme.to_parquet(daily_crsp_folder + 'dme.parquet')

    "Load the necessary data from storage"
    dret_x_dl = dd.read_parquet(daily_crsp_folder + 'dret_x_adj.parquet').compute()
    permno = pd.read_csv(crsp_folder + 'permno.csv', index_col=0)
    crsp_dsedelist = pd.read_csv(daily_crsp_folder + 'crsp_dsedelist.csv', index_col=0)

    "get permnos to drop"
    #get the indices of the permnos in crsp_msedelist.permno  that are NOT in permno
    mask = np.isin(crsp_dsedelist.permno, permno, invert=True)
    # get the permnos to remove
    toDrop = crsp_dsedelist.permno[mask]

    "drop these permnos from crsp_dsedelist dataframe"
    crsp_dsedelist = crsp_dsedelist.set_index('permno')
    crsp_dsedelist = crsp_dsedelist.drop(toDrop)
    #changing permnos back to a column instead of index
    crsp_dsedelist.reset_index(inplace=True)

    # The index of dret_x_dl is 'YYYY-MM-DD' but ddates is saved as 'YYYYMMDD', therefor I recreate the series to match.
    ddates = dd.read_parquet(daily_crsp_folder + 'crsp_dsf*.parquet', columns='date').unique().astype(str)
    ddates = ddates.compute()

    "fill in the delisting returns"
    dret = dret_x_dl.copy()
    for i in range(len(crsp_dsedelist)):
        # for i in range(500):
        "find the index in permno of ith permno in the delist dataframe"
        c = np.where(permno == crsp_dsedelist['permno'][i])[0][0]
        # print(c)
        "find the index in dates that corresponds to the delisting date of the ith permno"
        r_dt_ar = np.where(ddates == crsp_dsedelist['dlstdt'][i])[0]
        if r_dt_ar.size == 0:
            continue
        else:
            r_dt = r_dt_ar[0]
        # print(r_dt)
        "returns a series of row numbers in ret dataframe where the delisted permno has finite returns"
        r_last_array = np.where(np.isfinite(dret.iloc[:, c]) == True)[0]
        "check to see of the array is empty, and if it is, skip to the next iteration of the loop"
        if r_last_array.size == 0:
            continue
        else:
            "selects the last index, i.e., the row number of the final finite return for delisted permno"
            r_last = r_last_array[-1] + 1
            # print(r_last)
        if np.isfinite(dret.iloc[r_dt, c]):
            if r_last < len(ddates):
                "assigns the delisting return to the position following the last finite return"
                dret.iloc[(r_last), c] = crsp_dsedelist.dlret[i]
        else:
            dret.iloc[r_dt, c] = crsp_dsedelist.dlret[i]

    "Save the returns dataframe"
    # dret.to_csv(daily_crsp_folder + 'dret.csv')
    dret.columns = dret.columns.astype(str)
    dret.to_parquet(daily_crsp_folder + 'dret.parquet')

    "Adjust NASDAQ volume following Gao and Ritter (2010). See their Appendix B for more details"
    "To adjust the volume, we first need to create the daily exchange code matrix"
    exchcd = pd.read_csv(crsp_folder + 'exchcd.csv', index_col=0)
    exchcd.index = pd.to_datetime(exchcd.index.astype(int), format='%Y%m')
    ddates = pd.read_csv(daily_crsp_folder + 'ddates.csv', index_col=0).values.flatten().astype(int)
    ddates = pd.to_datetime(ddates, format='%Y%m%d')
    dexchcd = exchcd.reindex(ddates, method='ffill')
    dexchcd.to_parquet(daily_crsp_folder + 'dexchcd.parquet')

    # Slice dexchcd to match the size of dvol
    dvol = dd.read_parquet(daily_crsp_folder + 'dvol_x_adj.parquet').compute()
    dvol_columns = dd.read_parquet(daily_crsp_folder + 'dvol_x_adj.parquet').columns

    # Note: The adjusted_dvol computation assumes dvol data aligns exactly with dexchcd in structure and partitioning
    "Requires too much memory to do entire dataframe at once. Will try and go column by column."
    # Divide by 2 prior to Feb 2001
    # Divide by 1.8 for most of 2001
    # Divide by 1.6 for 2002 and 2003
    columns_to_process = dexchcd.columns[(dexchcd == 3).any()].to_list()
    for column in columns_to_process:
        print(column)
        col_index = dvol_columns.get_loc(column)
        # Since iterating over columns, I only need the row numbers where both conditions are satisfied for a particular column
        rows_first = np.where((dexchcd[column] == 3) & (dexchcd.index < pd.Timestamp('2001-02-01')))[0]
        rows_mid = np.where((dexchcd[column] == 3) & (dexchcd.index >= pd.Timestamp('20010201')) & (dexchcd.index < pd.Timestamp('20020101')))[0]
        rows_last = np.where((dexchcd[column] == 3) & (dexchcd.index >= pd.Timestamp('20020101')) & (dexchcd.index < pd.Timestamp('20040101')))[0]

        dvol.iloc[rows_first, col_index] = dvol.iloc[rows_first, col_index] / 2
        dvol.iloc[rows_mid, col_index] = dvol.iloc[rows_mid, col_index] / 1.8
        dvol.iloc[rows_last, col_index] = dvol.iloc[rows_last, col_index] / 1.6

    dvol.columns = dvol.columns.astype(str)
    dvol.to_parquet(daily_crsp_folder + 'dvol.parquet')

    "Download, clean up, and save the Fama-French factors from Ken French's website"
    getFFDailyFactors(params=params)

    "Make Amihud values"
    # first 12 month rolling amihud values

    # load the monthly returns, monthly price, and monthly dates, matrices
    ret = pd.read_csv(crsp_folder + 'ret.csv', index_col=0).astype(float)
    prc = pd.read_csv(crsp_folder + 'prc.csv', index_col=0).astype(float)
    dates = pd.read_csv(crsp_folder + 'dates.csv', index_col=0).astype(int)

    # replace zero-volume observations with nan and calculate dollar volume
    # dprc = pd.read_parquet(daily_crsp_folder + 'dprc.parquet')
    dprc = dd.read_parquet(daily_crsp_folder + 'dprc.parquet').compute()
    dollar_volume = np.abs(dprc) * np.abs(dvol)
    zeroVolInd = (dollar_volume == 0)
    dollar_volume[zeroVolInd] = np.nan

    # calculate the daily price impact
    dret = dd.read_parquet(daily_crsp_folder + 'dret.parquet').compute().astype(float)
    price_impact = np.divide(np.abs(dret), dollar_volume)

    # Take the absolute value of the monthly price and store the number of months
    prc = np.abs(prc)
    nmonths = len(ret.index)

    # Reload ddates in YYYYMMDD format
    ddates = pd.read_csv(daily_crsp_folder + 'ddates.csv', index_col=0).astype(int)

    # initialize amihud matrix
    amihud = np.full_like(ret, np.nan)

    # Calculate amihud
    if not params.remote_or_not:
        for i in range(11, nmonths):
            print(i)
            # Find the days in the last year
            start_date = dates.iloc[i - 11]
            end_date = dates.iloc[i]
            index_year = ((ddates // 100 >= start_date) & (ddates // 100 <= end_date))

            # Ensure index_year is a 1D boolean array
            index_year = index_year.values.flatten()

            # Store monthly price impact for last year
            last_yr_pi = price_impact[index_year].copy()

            # Apply the filters (200 obs & price > $5)
            idx_to_drop = np.isfinite(last_yr_pi).sum(axis=0) < 200
            idx_to_drop |= prc.iloc[i, :].values.flatten() <= 5
            last_yr_pi.iloc[:, idx_to_drop] = np.nan

            # Calculate the mean price impact for the last year, ignoring NaN values
            amihud[i, :] = np.nanmean(last_yr_pi, axis=0)
    else:
        def compute_amihud_for_month(i, start_date, end_date, ddates):
            global prc, price_impact  # Assuming prc and price_impact are available globally

            index_year = ((ddates // 100 >= start_date) & (ddates // 100 <= end_date))

            # Convert to 1D boolean array if needed
            index_year = index_year.values.flatten()

            # Use the index_year to slice price_impact for the relevant period
            last_yr_pi = price_impact[index_year].copy()

            # Apply your filters
            idx_to_drop = np.isfinite(last_yr_pi).sum(axis=0) < 200
            idx_to_drop |= prc.iloc[i, :].values.flatten() <= 5
            last_yr_pi.iloc[:, idx_to_drop] = np.nan

            # Calculate Amihud measure
            amihud_value = np.nanmean(last_yr_pi, axis=0)
            return i, amihud_value

        # Prepare your list of arguments based on date ranges
        args_list = [(i, dates.iloc[i - 11], dates.iloc[i], ddates) for i in range(11, nmonths)]

        # Execute in parallel
        with Pool(os.cpu_count()) as pool:
            results = pool.starmap(compute_amihud_for_month, args_list)

        for i, amihud_value in results:
            amihud[i, :] = amihud_value

    amihud = pd.DataFrame(amihud)
    amihud.index = dates.values.flatten()
    amihud.columns = permno.values.flatten().astype(str)
    amihud.to_parquet(crsp_folder + 'amihud.parquet')

    "Make other measures from the daily data"
    # Realized volatilities
    # Initialize the matrices
    n_months, n_stocks = ret.shape
    RVOL_matrices = {period: np.full((n_months, n_stocks), np.nan) for period in [1, 3, 6, 12, 36, 60]}
    dshvol = np.full_like(ret, np.nan)
    dshvolM = np.full_like(ret, np.nan)
    dretmax = np.full_like(ret, np.nan)
    dretmin = np.full_like(ret, np.nan)

    # First turn the dates and ddates dataframes into arrays
    ddates_array = ddates.values.flatten()
    dates_array = dates.values.flatten()

    # Find the first month index
    first_month_date = ddates_array[0] // 100
    if first_month_date in dates_array:
        first_month = np.where(dates_array == first_month_date)[0][0]
    else:
        raise ValueError("First month date not found in dates array")

    # Monthly loop range
    last_month = len(dates)

    # Calculate measures
    for i in range(first_month, last_month):
        for period, RVOL in RVOL_matrices.items():
            start_index = max(i - period + 1, 0)
            ind = (ddates_array // 100 >= dates_array[start_index]) & (ddates_array // 100 <= dates_array[i])

            # Ensure ind is a 1D boolean array and matches the number of rows in dret
            ind = ind.flatten()

            # Apply the indexing to the DataFrame
            selected_dret = dret.loc[ind, :]

            RVOL[i, :] = np.nanstd(selected_dret, axis=0)

        ind1 = (ddates_array // 100 == dates_array[i])

        # Ensure ind1 is a 1D boolean array and matches the number of rows in dvol
        ind1 = ind1.flatten()

        # Apply the indexing to the DataFrame
        selected_dvol = dvol.loc[ind1, :]

        dshvol[i, :] = np.nansum(selected_dvol, axis=0)
        dshvolM[i, :] = np.nanmax(selected_dvol, axis=0)
        dretmax[i, :] = np.nanmax(selected_dvol, axis=0)
        dretmin[i, :] = np.nanmin(selected_dvol, axis=0)

    # Save the matrices
    for period, RVOL_matrix in RVOL_matrices.items():
        filename = f'RVOL{period}.csv'
        RVOL_matrix = pd.DataFrame(RVOL_matrix)
        RVOL_matrix.to_csv(crsp_folder + filename)

    dshvol = pd.DataFrame(dshvol)
    dshvol.columns = dshvol.columns.astype(str)
    dshvol.to_parquet(crsp_folder + 'dshvol.parquet')

    dshvolM = pd.DataFrame(dshvolM)
    dshvolM.columns = dshvolM.columns.astype(str)
    dshvolM.to_parquet(crsp_folder + 'dshvolM.parquet')

    dretmax = pd.DataFrame(dretmax)
    dretmax.columns = dretmax.columns.astype(str)
    dretmax.to_parquet(crsp_folder + 'dretmax.parquet')

    dretmin = pd.DataFrame(dretmin)
    dretmin.columns = dretmin.columns.astype(str)
    dretmin.to_parquet(crsp_folder + 'dretmin.parquet')

    "Make IVOLs"
    # Load the FF factors
    dff = pd.read_csv(ff_data_folder + 'dff.csv', index_col=0).astype(float)
    dff3 = pd.read_csv(ff_data_folder + 'dff3.csv', index_col=0).astype(float)
    dff3.index = dff3['dates']
    dff3.drop(columns=['dates'], inplace=True)
    dmkt = dff['mkt'].copy()

    # Create the daily excess returns above Rf
    drf = dff['rf'].to_numpy()
    rf_mat = np.tile(drf, (len(ret.columns), 1)).T
    dxret = dret - rf_mat

    # Initialize the IVOL variables
    ivol = np.full_like(ret, np.nan)
    ivol3 = np.full_like(ret, np.nan)
    iffvol = np.full_like(ret, np.nan)
    iffvol3 = np.full_like(ret, np.nan)

    if params.remote_or_not:
        total_months = last_month - first_month
        batches = 15
        batch_size = max(total_months // batches, 1)
        for batch in range(batches):
            start_i = first_month + batch*batch_size
            end_i = min(start_i + batch_size, last_month)
            # Prepare a list of arguments for parallel processing
            arguments = []
            # for i in range(first_month, last_month):
            for i in range(start_i, end_i):
                print(i)
                ind1 = ((ddates.values.flatten() // 100) == dates.iloc[i, 0])
                ind3 = ((ddates.values.flatten() // 100) >= dates.iloc[max(i - 2, 0), 0]) & (
                        (ddates.values.flatten() // 100) <= dates.iloc[i, 0])
                hor_ind = np.isfinite(dxret.loc[ind1]).sum(axis=0) > 0
                X1 = sm.add_constant(dmkt[ind1].values)
                X1f = sm.add_constant(dff3.loc[ind1].values)
                X3 = sm.add_constant(dmkt[ind3].values)
                X3f = sm.add_constant(dff3.loc[ind3].values)

                for j in hor_ind[hor_ind].index:
                # for j in hor_ind[hor_ind].index[:5]:
                    col_index = dret.columns.get_loc(j)
                    y1 = dret.loc[ind1, j].values
                    y3 = dret.loc[ind3, j].values

                    arguments.append((i, col_index, y1, X1, y3, X3, X1f, X3f))

            # Run the computation in parallel
            with Pool(processes=params.num_cpus) as pool:
                results = pool.starmap(parallel_compute_ivol, arguments)

            # Unpack results and populate the matrices
            for res in results:
                i, col_index, ivol_val, iffvol_val, ivol3_val, iffvol3_val = res
                ivol[i, col_index] = ivol_val
                iffvol[i, col_index] = iffvol_val
                ivol3[i, col_index] = ivol3_val
                iffvol3[i, col_index] = iffvol3_val

    else:
        # Monthly loop range
        first_month_date = ddates.iloc[0, 0] // 100
        first_month = np.where(dates.values.flatten() == first_month_date)[0][0]
        last_month = len(dates)

        # Calculate IVOLs
        for i in range(first_month, last_month):
            # Find the 1- and 3-month daily indices
            ind1 = ((ddates.values.flatten() // 100) == dates.iloc[i, 0])
            ind3 = ((ddates.values.flatten() // 100) >= dates.iloc[max(i - 2, 0), 0]) & (
                    (ddates.values.flatten() // 100) <= dates.iloc[i, 0])

            # Stocks which we need to loop through
            hor_ind = dxret.iloc[ind1, :].apply(lambda x: np.isfinite(x).sum(), axis=0) > 0

            for j in hor_ind[hor_ind].index:
                # Get the integer index for the column
                col_index = dret.columns.get_loc(j)

                # Regression for 1-month residual
                X = sm.add_constant(dmkt[ind1])  # Add a constant term
                y = dret.loc[ind1, j]
                model = sm.OLS(y.values, X.values, missing='drop')
                results = model.fit()
                ivol[i, col_index] = np.sqrt(np.mean(results.resid ** 2))

                # Regression for FF3 1-month residual
                X_ff3 = dff3.loc[ind1]
                y = dret.loc[ind1, j]
                model_ff3 = sm.OLS(y.values, X_ff3.values, missing='drop')
                results_ff3 = model_ff3.fit()
                iffvol[i, col_index] = np.sqrt(np.mean(results_ff3.resid ** 2))

                # Regression for 3-month residual
                X = sm.add_constant(dmkt[ind3])  # Add a constant term
                y = dret.loc[ind3, j]
                model = sm.OLS(y.values, X.values, missing='drop')
                results = model.fit()
                ivol3[i, col_index] = np.sqrt(np.mean(results.resid ** 2))

                # Regression for FF3 3-month residual
                X_ff3 = dff3.loc[ind3]
                y = dret.loc[ind3, j]
                model_ff3 = sm.OLS(y.values, X_ff3.values, missing='drop')
                results_ff3 = model_ff3.fit()
                iffvol3[i, col_index] = np.sqrt(np.mean(results_ff3.resid ** 2))

    # Save the IVOLs as parquet files
    ivol = pd.DataFrame(ivol)
    ivol.columns = ivol.columns.astype(str)
    ivol.to_parquet(crsp_folder + 'IVOL.parquet')

    iffvol = pd.DataFrame(iffvol)
    iffvol.columns = iffvol.columns.astype(str)
    iffvol.to_parquet(crsp_folder + 'IffVOL.parquet')

    ivol3 = pd.DataFrame(ivol3)
    ivol3.columns = ivol3.columns.astype(str)
    ivol3.to_parquet(crsp_folder + 'IVOL3.parquet')

    iffvol3 = pd.DataFrame(iffvol3)
    iffvol3.columns = iffvol3.columns.astype(str)
    iffvol3.to_parquet(crsp_folder + 'IffVOL3.parquet')

    "Make CAR3s: Inilialize the CAR3 matrix, calculate abnormal returns, iterate through each month to compute the" \
    "CAR3 value for each stock at each announcement date"
    # load additional variables
    rdq = pd.read_csv(params.compFolder + os.sep + 'RDQ.csv', index_col=0)
    fqtr = pd.read_csv(params.compFolder + os.sep + 'FQTR.csv', index_col=0)
    nyse = pd.read_csv(params.crspFolder + os.sep + 'NYSE.csv', index_col=0)
    me = pd.read_csv(params.crspFolder + os.sep + 'me.csv', index_col=0)

    # For some reason RDQ and FQTR has an additional row at the beginning of the matrix. It doesn't correspond to any
    # date so I will check if this is the case and remove it.
    if pd.isna(rdq.index[0]):
        rdq = rdq.iloc[1:, :]

    if pd.isna(fqtr.index[0]):
        fqtr = fqtr.iloc[1:, :]

    # Only leave the announcement dates
    rdq = rdq.where(~fqtr.isna(), np.nan)

    # Initialize the CAR3 matrix
    CAR3 = np.full_like(rdq, np.nan)

    # Calculate the abnormal return (in excess of the market); (ret_{i,t} - ret_{mkt,t})
    rptdMkt_values = (1 + dmkt + drf).values
    rptdMkt = np.tile(rptdMkt_values, (len(me.columns), 1)).T
    dxret = 1 + dret - rptdMkt

    # Monthly loop range
    first_month = np.where(rdq.notna().sum(axis=1) > 0)[0][0]
    last_month = len(dates)

    # Loop over the months
    for i in range(first_month, last_month):
        # Find all the announcements in the current month
        idx_announcements = np.where(rdq.iloc[i, :].notna())[0]

        # Loop over the announcements
        for c in idx_announcements:
            permno = rdq.columns[c]  # Get the permno (column label) from rdq

            # Check if the permno is in the columns of dxret
            if permno in dxret.columns:
                dxret_col_index = dxret.columns.get_loc(permno)  # Find the corresponding column in dxret

                # Get the announcement date and find the corresponding row in ddates
                announcement_date = rdq.iloc[i, c]
                r = np.where(ddates == announcement_date)[0]

                # Calculate the CAR3 if we found a match
                if r.size > 0 and r[0] < len(ddates) - 1:
                    CAR3[i, c] = np.prod(dxret.iloc[r[0] - 1:r[0] + 2, dxret_col_index]) - 1

    # Fill the observations between quarters; Matlab uses a helper function, but this isn't necessary in Python
    CAR3 = pd.DataFrame(CAR3).ffill(axis=0)

    # Change the columns names to be integers
    ret.columns = [int(float(col)) for col in ret.columns]
    CAR3.columns = [int(float(col)) for col in rdq.columns]

    # Identify common columns between 'ret' and 'CAR3'
    common_columns = ret.columns.intersection(CAR3.columns)

    # Initialize a mask with False for all entries in CAR3
    idx_to_drop = pd.DataFrame(False, index=ret.index, columns=CAR3.columns)

    # Update the mask for common columns based on NaN values in 'ret'
    idx_to_drop.loc[:, common_columns] = ret[common_columns].isna()

    # Remove all observations where ret is nan
    CAR3[idx_to_drop] = np.nan

    # Save
    # CAR3.to_csv(crsp_folder + 'CAR3.csv')
    CAR3.columns = CAR3.columns.astype(str)
    CAR3.to_parquet(crsp_folder + 'CAR3.parquet')

    "Timekeeping"
    print(f"\nCRSP daily derived variables run ended at {datetime.now()}.\n")

    return


# makeCRSPDailyDerivedVariables(params=params)


