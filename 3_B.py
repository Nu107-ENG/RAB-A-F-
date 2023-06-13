#3.SORUMUN B SIKKI :

import pandas as pd

data = [15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65]
c1 = 16
c2 = 22

def calculate_distance(x, c):
    return abs(x - c)

def assign_cluster(x):
    distance1 = calculate_distance(x, c1)
    distance2 = calculate_distance(x, c2)
    return 1 if distance1 < distance2 else 2

def update_centroid(cluster):
    return sum(cluster) / len(cluster)

dataframe = pd.DataFrame(data, columns=['Data'])
dataframe['c1'] = c1
dataframe['c2'] = c2
dataframe['Distance1'] = dataframe['Data'].apply(lambda x: calculate_distance(x, c1))
dataframe['Distance2'] = dataframe['Data'].apply(lambda x: calculate_distance(x, c2))
dataframe['Nearest Cluster'] = dataframe[['Distance1', 'Distance2']].idxmin(axis=1)
dataframe['New Centroid'] = dataframe['Nearest Cluster'].apply(lambda x: update_centroid(dataframe[dataframe['Nearest Cluster'] == x]['Data'].tolist()))

print("Iteration 1:")
print(dataframe)