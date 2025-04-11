import numpy as np
import matplotlib.pyplot as plt

def load_my_dataset():
    x = np.load('data/ex7_X.npy')
    return x

dataset = load_my_dataset();
print(dataset.shape)

plt.scatter(dataset[:, 0], dataset[:, 1], marker='o', c='blue')

initail_centroids = np.array([[2,3], [4,7], [5,6]])
plt.scatter(initail_centroids[:, 0 ], initail_centroids[:, 1], marker='o', c='red')
plt.xlabel('X_1')
plt.ylabel('X_2')
plt.show()


def find_closest_centroid(data, initial_centroids_of_clusters):
    k = initial_centroids_of_clusters.shape[0]  # number of clusters

    idx = np.zeros(data.shape[0], dtype=int)

    distances_to_cluster_centroids = []

    for i in range(data.shape[0]):
        distances_to_cluster_centroids = []

        for j in range(initial_centroids_of_clusters.shape[0]):
            norm_i_j = np.linalg.norm(data[i] - initial_centroids_of_clusters[j])
            distances_to_cluster_centroids.append(norm_i_j)

        idx[i] = np.argmin(distances_to_cluster_centroids)

    # the_smallest_distance = np.min(distances_to_cluster_centroids)
    # idx[i] = the_smallest_distance

    return idx

clus_1 = 0;
clus_2 = 0;
clus_3 = 0;

nn =find_closest_centroid(dataset, initail_centroids)
print(nn)

for i in range(300):
    if nn[i]==0:
        clus_1= clus_1+1
    elif nn[i]==1:
        clus_2 = clus_2+1
    else:
        clus_3 = clus_3+1