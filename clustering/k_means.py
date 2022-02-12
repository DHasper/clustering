import random
from math_functions import euclidean_distance, compute_means
from point import Point

def k_means(points, cluster_count=2):
    """k-means clustering algorithm that clusters points in cluster_count clusters."""

    min_x = min([point.x for point in points])
    max_x = max([point.x for point in points])
    min_y = min([point.y for point in points])
    max_y = max([point.y for point in points])

    # Generate K random centroids.
    centroids = [Point(random.randrange(min_x, max_x), random.randrange(min_y, max_y)) for _ in range(cluster_count)]

    # Compute initial clusters.
    clusters = compute_clusters(points, centroids)

    finished = False
    while not finished:
        # Compute new centroids to the mean of the cluster.
        centroids = compute_means(clusters)

        # Calculate new clusters.
        new_clusters = compute_clusters(points, centroids)

        # Stop iterating if no changes.
        if clusters != new_clusters:
            clusters = new_clusters
        else:
            finished = True

    return clusters

def compute_clusters(points, centroids):
    """Computes clusters by grouping points to the centroid with the shortest euclidian distance."""

    clusters = [[] for _ in range(len(centroids))]

    for point in points:
        closest_centroid, closest_distance = 0, float("inf")

        for i, centroid in enumerate(centroids):
            distance = euclidean_distance(point, centroid)

            if distance < closest_distance:
                closest_distance = distance
                closest_centroid = i

        clusters[closest_centroid].append(point)

    return clusters
