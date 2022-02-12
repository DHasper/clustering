import math
from point import Point

def euclidean_distance(p1, p2):
    """Calculates the euclidian distance given 2 points.
    
    Uses the formula d(p, q) = √((q₂ - p₁)² + (q₂ - p₁)²) 
    """

    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

def compute_means(clusters):
    """Computes the mean per cluster given a list of clusters of points."""

    means = [0] * len(clusters)

    for i, cluster in enumerate(clusters):
        if len(cluster) > 0:
            mean_x = sum([point.x for point in cluster]) / len(cluster)
            mean_y = sum([point.y for point in cluster]) / len(cluster)

            means[i] = Point(mean_x, mean_y)
        else:
            means[i] = Point(0, 0)

    return means