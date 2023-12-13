import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    '''
    ordered = orders.groupby('customer_number')['order_number'].count().reset_index()
    res = ordered[ordered['order_number']==ordered['order_number'].max()][['customer_number']]
    return res
    '''

    return orders['customer_number'].mode().to_frame()