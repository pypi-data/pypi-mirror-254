import pandas as pd
import itertools

def combinations(dict_in):

    """
    Parameters
    ----------
    dict_in : dict
        Dictionary containing independent variables and their values to test.

    Returns
    -------
    df : DataFrame
        Dataframe containing all possible independent variable value combinations
    """
    e = 0
    df = pd.DataFrame(columns=dict_in.keys())
    for element in itertools.product(*dict_in.values()):
        df.loc[e] = element
        e += 1
    return df
