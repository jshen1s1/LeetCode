import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    '''
    triangle['triangle'] = 'No'
    for idx, row in triangle.iterrows():
        x, y, z = row['x'], row['y'], row['z']
        if ((x+y) > z) and ((x+z) > y) and ((y+z) > x):
            triangle['triangle'][idx] = 'Yes'

    return triangle
    '''
    triangle['triangle'] = triangle.apply(lambda t: 'Yes' if ((t.x+t.y) > t.z) 
                                                        and ((t.x+t.z) > t.y) 
                                                        and ((t.y+t.z) > t.x)  else 'No', axis=1)
    return triangle