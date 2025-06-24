import numpy as np
import pandas as pd

def rounding(x):
    return np.round(x).astype(int)

def binary_encode(x):
    binary_ft = ['gender', 'family_overweight_history']
    x = pd.DataFrame(x, columns=binary_ft)
    return x.replace({'Male': 1, 'Female': 0, 'yes': 1, 'no': 0}).values
