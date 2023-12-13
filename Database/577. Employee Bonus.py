import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employee, bonus, on='empId', how='left')
    res = merged.query('bonus < 1000 or bonus.isnull()')

    return res[['name', 'bonus']]