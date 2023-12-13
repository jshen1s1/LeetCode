import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    uniq_loc = insurance.drop_duplicates(subset=['lat', 'lon'], keep=False)
    #print(uniq_loc)
    not_uniq_2015 = insurance[insurance.duplicated(subset=['tiv_2015'], keep=False) == True]
    #print(not_uniq_2015)
    insurance = insurance.loc[insurance.pid.isin(uniq_loc.pid) & insurance.pid.isin(not_uniq_2015.pid)]
    return insurance[['tiv_2016']].sum().to_frame('tiv_2016').round(2)