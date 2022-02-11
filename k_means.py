import random
import math
from point import Point

def k_means(points, cluster_count=2):
    """k_means clustering algorithm that clusters points to K clusters."""

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
        centroids = compute_centroids(clusters)

        # Calculate new clusters.
        new_clusters = compute_clusters(points, centroids)

        # Stop iterating if no changes.
        if clusters != new_clusters:
            clusters = new_clusters
        else:
            finished = True

    return clusters, centroids

def compute_clusters(points, centroids):
    """Computes clusters by grouping points to the centroid with the shortest euclidian distance."""

    clusters = [[] for _ in range(len(centroids))]

    for point in points:
        closest_centroid, closest_distance = 0, float("inf")

        for i, centroid in enumerate(centroids):
            distance = euclidian_distance(point, centroid)

            if distance < closest_distance:
                closest_distance = distance
                closest_centroid = i

        clusters[closest_centroid].append(point)

    return clusters

def compute_centroids(clusters):
    """Computes the mean point given a list of clusters of points."""

    means = [0] * len(clusters)

    for i, cluster in enumerate(clusters):
        mean_x = sum([point.x for point in cluster]) / len(cluster)
        mean_y = sum([point.y for point in cluster]) / len(cluster)

        means[i] = Point(mean_x, mean_y)

    return means

def euclidian_distance(p1, p2):
    """Calculates the euclidian distance given 2 points
    
    Uses the formula d(p, q) = √((q₂ - p₁)² + (q₂ - p₁)²) 
    """

    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)