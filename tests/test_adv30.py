import numpy as np
import pandas as pd
from tech_signals_ibkr import calc_ADV30

def test_calc_adv30_no_volume():
    df = pd.DataFrame({"close": [1, 2, 3]})
    result = calc_ADV30(df)
    assert np.isnan(result)

def test_calc_adv30_with_volume():
    df = pd.DataFrame({"volume": [10, 20, 30, 40, 50]})
    assert calc_ADV30(df) == 30
