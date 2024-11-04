import os
import sys
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs 

LEVELS = 3
CLUSTERS_PER_LEVEL = 2 

ROOT_DIR = f"./clustering/results/clustering-L{LEVELS}-C{CLUSTERS_PER_LEVEL}"
os.makedirs(ROOT_DIR, exist_ok=True)

def load_data():
    data, _ = make_blobs(n_samples=100, centers=5, n_features=2, random_state=42)
    return data

def hcluster(trace_id, cluster_id, data, num_clusters, current_level, max_level):
    level_id = f"{trace_id}-{cluster_id:04d}"
    level_root_dir = os.path.join(ROOT_DIR, f"L{current_level}")
    os.makedirs(level_root_dir, exist_ok=True)
    
    cluster_root_dir = os.path.join(level_root_dir, level_id)
    os.makedirs(cluster_root_dir, exist_ok=True)

    print(f"### STARTING hcluster L={current_level}, C={num_clusters}, ML={max_level} ###")
    
    kmeans = KMeans(n_clusters=num_clusters, random_state=0)
    kmeans.fit(data)
    labels = kmeans.labels_

    if current_level < max_level:
        for cluster_num in range(num_clusters):
            cluster_data = data[labels == cluster_num]
            if len(cluster_data) > 0:
                hcluster(level_id, cluster_num, cluster_data, num_clusters, current_level + 1, max_level)
    else:
        np.save(os.path.join(cluster_root_dir, "cluster_data.npy"), data)

data = load_data()
hcluster("root", 0, data, CLUSTERS_PER_LEVEL, 1, LEVELS)

