import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    my_numbers.drop_duplicates(keep=False, inplace=True)
    return my_numbers.max().to_frame(name='num')