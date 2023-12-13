import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    #salary['sex'] = salary['sex'].apply(lambda s: 'f' if s=='m' else 'm')

    return salary.replace({'f': 'm', 'm': 'f'})