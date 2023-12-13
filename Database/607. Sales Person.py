import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(company, orders, on='com_id', how='inner')
    red_id = merged[merged['name'] == 'RED'].sales_id.unique()

    return sales_person[~sales_person['sales_id'].isin(red_id)][['name']]