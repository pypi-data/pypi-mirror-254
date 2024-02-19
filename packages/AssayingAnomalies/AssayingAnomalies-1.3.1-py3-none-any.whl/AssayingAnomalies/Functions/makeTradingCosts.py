import numpy as np
import pandas as pd
import os
from glob import glob
from scipy.stats.mstats import winsorize
from datetime import datetime
from .makeGibbs import makeGibbs
from .makeCorwinSchultz import makeCorwinSchultz
from .makeAbdiRanaldi import makeAbdiRanaldi
from .makeKyleObizhaeva import makeKyleObizhaeva
from .make_hf_effective_spreads import *
from .rank_with_nan import rank_with_nan
from .fill_missing_tcosts import fill_missing_tcosts


def makeTradingCosts(params):
    # Timekeeping
    print(f"\nNow working on creating the transaction costs. Run started at {datetime.now()}\n")

    # Store the general and daily CRSP data path
    crsp_path = params.crspFolder + os.sep
    daily_path = params.daily_crsp_folder + os.sep
    hf_path = params.hf_effective_spreads_folder + os.sep

    # Store the tcost types
    # tcostsType = params.tcostsType
    tcostsType = 'full'

    # Check if correct tcosts input selected
    if tcostsType not in ['full', 'lf_combo', 'gibbs']:
        print(f"params.tcostsType is {tcostsType} but should be one of the folowing: \"full\", \"lf_combo\", \"gibbs\"")

    # Initialize dictionary to hold trading costs. CorwinSchultz = hl, AbdiRanaldi = chl, KyleObizhaeva = vov
    effSpreadStruct = {'gibbs': None,
                       'hl': None,
                       'chl': None,
                       'vov': None,
                       'hf_spreads_ave': None
                       }

    "Check for Gibbs file"
    # Construct the file search pattern
    search_pattern = os.path.join(params.data_folder, '**', 'crspgibbs.csv')

    # Find all files matching the pattern
    gibbs_file_list = glob(search_pattern, recursive=True)  # recursive=True searches the subdirectories as well

    # Check if any files were found
    if not gibbs_file_list:
        raise FileNotFoundError('Gibbs input file does not exist. Gibbs trading cost estimate cannot be constructed.')
    else:
        file_path = gibbs_file_list[0]

    "Create Gibbs spreads"
    # path to file with Hasbrouck effective spread estimates
    effSpreadStruct['gibbs'] = pd.DataFrame(makeGibbs(params, file_path))  # :TODO:Fix change makeGibbs to it returns dataframe instead of  numpy array.

    if tcostsType in ['lf_combo', 'full']:
        effSpreadStruct['hl'] = makeCorwinSchultz(params)
        effSpreadStruct['chl'] = makeAbdiRanaldi(params)
        effSpreadStruct['vov'] = makeKyleObizhaeva(params)

    if tcostsType == 'full':
        search_pattern = os.path.join(params.data_folder, '**', 'hf_monthly_pre_2003.csv')
        hf_file_list = glob(search_pattern, recursive=True)
        if not hf_file_list:
            raise FileNotFoundError('High-frequency trading cost input file does not exist. High-frequency trading '
                                    'cost estimate cannot be constructed prior to 2003.')
        else:
            get_hf_spreads_data(params)
            make_hf_effective_spreads(params)
            extend_hf_effective_spreads(params)
            effSpreadStruct['hf_spreads_ave'] = pd.read_csv(hf_path + 'hf_monthly.csv', index_col=0)

    # Winsorize by keeping anything between 0 and 99.9th percentiles.
    for key in effSpreadStruct.keys():
        flat_values = effSpreadStruct[f'{key}'].to_numpy().flatten()
        winsorized_values = winsorize(flat_values, limits=[0, 0.001], nan_policy='omit')
        effSpreadStruct[f'{key}'] = pd.DataFrame(winsorized_values.reshape(effSpreadStruct[f'{key}'].shape))

    # Check if we need to adjust some of the tcost measures
    if tcostsType.lower() == 'gibbs':
        # No need to worry about the rest
        tcosts_raw = effSpreadStruct['gibbs'] / 2
        # tcosts_raw.to_csv(crsp_path + 'tcosts_raw.csv')
        tcosts_raw.to_parquet(crsp_path + 'tcosts_raw.parquet')
    else:
        exchcd = pd.read_csv(crsp_path + 'exchcd.csv', index_col=0).astype(float)
        exchcd.index = pd.to_datetime(exchcd.index.astype(int), format='%Y%m')

        # Excluding NASDAQ stocks prior to 1983 for Gibbs and VoV
        # Create a mask for dates before 1983 and exchange code being 3
        years = np.tile(exchcd.index.year, (len(exchcd.columns), 1)).T
        mask = (exchcd == 3) & (years < 1983)
        temp = effSpreadStruct['gibbs'].to_numpy()
        temp[mask] = np.nan
        effSpreadStruct['gibbs'] = temp
        temp = effSpreadStruct['vov'].to_numpy()
        temp[mask] = np.nan
        effSpreadStruct['vov'] = temp

        # Excluding Nasdaq stocks prior to 1993 for HL and CHL
        mask = (exchcd == 3) & (years < 1993)
        temp = effSpreadStruct['hl'].to_numpy()
        temp[mask] = np.nan
        effSpreadStruct['hl'] = temp
        temp = effSpreadStruct['chl'].to_numpy()
        temp[mask] = np.nan
        effSpreadStruct['chl'] = temp

        # Excluding AMEX stocks prior to 1962 for all
        mask = (exchcd == 3) & (years < 1962)
        for key in ['gibbs', 'hl', 'chl', 'vov']:
            temp = effSpreadStruct[key]
            temp[mask] = np.nan
            effSpreadStruct[key] = pd.DataFrame(temp)

        # In the matlab code, reshapedEffSpreadRaw is a long vetor containing the average trading cost for each
        # permno for each month across the 4 lf measures. However, this is then reshaped back to a matrix. I
        EffSpreadRaw = pd.concat([effSpreadStruct['gibbs'], effSpreadStruct['hl'], effSpreadStruct['chl'],
                                  effSpreadStruct['vov']], axis=0).groupby(level=0).mean()

        # Update the average trading costs with the high frequency estimates where available.
        mask = np.isfinite(effSpreadStruct['hf_spreads_ave'])
        EffSpreadRaw[mask] = effSpreadStruct['hf_spreads_ave']

        # Need to divide the effective spreads by 2, because this is the tcost measure (half-spread!)
        tcosts_raw = EffSpreadRaw / 2

        # Store the raw tcosts
        # tcosts_raw.to_csv(crsp_path + 'tcosts_raw.csv')
        tcosts_raw.to_parquet(crsp_path + 'tcosts_raw.parquet')

    tcosts = fill_missing_tcosts(params, tcosts_raw)
    # tcosts.to_csv(crsp_path + 'tcosts.csv')
    tcosts.to_parquet(crsp_path + 'tcosts.parquet')

    # Do the FF trading costs calculation here too # :TODO Make the makeFFTcosts function.
    # makeFFTcosts()

    # Timekeeping
    print(f"Trading costs construction run ended at {datetime.now()}")



