#2.SORUMUN B SIKKI : 

import pandas as pd

data = {
    'X': [1, 2, 2, 3, 4, 5, 6, 8, 10, 11],
    'Y': [3, 5, 3, 9, 7, 2, 8, 6, 6, 1],
    'Z': ['negatif', 'pozitif', 'pozitif', 'negatif', 'negatif', 'pozitif', 'pozitif', 'pozitif', 'pozitif', 'pozitif']
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nx ve y Koordinatları:")
for index, row in df.iterrows():
    print(f"x: {row['X']}, y: {row['Y']}")