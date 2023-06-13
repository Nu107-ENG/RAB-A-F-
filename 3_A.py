#3.SORUMUN A SIKKI : 

import pandas as pd
import math

data = {
    'X': [1, 2, 2, 3, 4, 5, 6, 8, 10, 11],
    'Y': [3, 5, 3, 9, 7, 2, 8, 6, 6, 1],
    'Z': ['negatif', 'pozitif', 'pozitif', 'negatif', 'negatif', 'pozitif', 'pozitif', 'pozitif', 'pozitif', 'pozitif']
}

df = pd.DataFrame(data)

new_x = 7
new_y = 3

df['Distance'] = df.apply(lambda row: math.sqrt((row['X'] - new_x) ** 2 + (row['Y'] - new_y) ** 2), axis=1)

df['Proximity'] = df['Distance'].rank()

print("DataFrame:")
print(df)