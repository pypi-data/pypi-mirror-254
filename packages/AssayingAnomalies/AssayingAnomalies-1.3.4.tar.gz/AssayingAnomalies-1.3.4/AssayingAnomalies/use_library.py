"""
This file contains a tutorial on how to implement various basic asset pricing techniques using the Toolkit. These
include univariate sorts, bivariate sorts, Fama-MacBeth regressions, and accounting for transaction costs.
"""

import pandas as pd
import numpy as np
import AssayingAnomalies.Functions as aa
import os
import json
from AssayingAnomalies.config import Config


# First load in your parameters
params = Config.load_params()

ret = pd.read_csv(params.crspFolder + os.sep + 'ret.csv', index_col=0).astype(float)
me = pd.read_csv(params.crspFolder + os.sep + 'me.csv', index_col=0).astype(float)
BM = pd.read_csv(params.compFolder + os.sep + 'BM.csv', index_col=0).astype(float)
dates = pd.read_csv(params.crspFolder + os.sep + 'dates.csv', index_col=0).astype(float)
NYSE = pd.read_csv(params.crspFolder + os.sep + 'NYSE.csv', index_col=0).astype(float)
ff = pd.read_csv(params.crspFolder + os.sep + 'ff.csv', index_col=0).astype(float)
