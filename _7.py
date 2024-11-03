import numpy as np
import matplotlib.pyplot as plt 
from scipy.cluster.hierarchy import dendrogram ,linkage,fcluster

data = np.array([12,22,25,27,42,43]).reshape(-1,1)


linked =linkage(data,method='ward')
max_distance =10
cluster = fcluster(linked,max_distance,criterion='distance')

for i,cluster_label in enumerate(cluster):
    print(f"Data point {data[i][0]}belongs to cluster {cluster_label}")
    
plt.figure(figsize=(8,4))
dendrogram(linked,
orientation='top',
labels=[18,22,25,27,42,43],
distance_sort='descending',
show_leaf_counts=True)

plt.title('Dendrogram of simple Data')
plt.show()
    