#1.SORUMUN C SIKKI : 


import pandas as pd

data = {
    'age': ['young', 'young', 'middle-aged', 'old', 'old', 'old', 'middle-aged', 'young', 'young', 'old', 'young', 'middle-aged', 'middle-aged', 'old'],
    'income': ['high', 'high', 'high', 'medium', 'low', 'low', 'low', 'medium', 'low', 'medium', 'medium', 'medium', 'high', 'medium'],
    'student': ['no', 'no', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no'],
    'credit_rating': ['fair', 'excellent', 'fair', 'fair', 'fair', 'excellent', 'excellent', 'fair', 'fair', 'fair', 'excellent', 'excellent', 'fair', 'excellent'],
    'buys_computer': ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']
}

df = pd.DataFrame(data)

df['age'] = df['age'].replace({'young': 'genc', 'middle-aged': 'orta yasli', 'old': 'yasli'})


print(df)
