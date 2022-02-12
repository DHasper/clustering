from math_functions import euclidean_distance, compute_means
from itertools import combinations

def hierarchical(points, cluster_count=2):
    """Agglomerative hierarchical clustering algorithm that clusters point in cluster_count clusters"""

    # Generate maximum amount of clusters.
    clusters = [[point] for point in points]

    # Iterate until we have cluster_count amount of clusters.
    while len(clusters) != cluster_count:
        lowest_distance, clusters_to_combine = float("inf"), [0, 0]
        cluster_combinations = list(combinations(clusters, 2))

        # Find 2 clusters with shortest distance
        for cluster1, cluster2 in cluster_combinations:
            distance = compute_cluster_distance(cluster1, cluster2)

            if distance < lowest_distance:
                lowest_distance = distance
                clusters_to_combine[0] = clusters.index(cluster1)
                clusters_to_combine[1] = clusters.index(cluster2)

        # Combine the 2 clusters into one.
        for point in clusters.pop(clusters_to_combine[1]):
            clusters[clusters_to_combine[0]].append(point)

    return clusters

def compute_cluster_distance(c1, c2):

    # Calculate mean of the clusters
    means = compute_means([c1, c2])

    return euclidean_distance(means[0], means[1])