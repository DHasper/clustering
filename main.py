import matplotlib.pyplot as plt
import matplotlib.markers as marker
from point import Point
from k_means import k_means
import random

# Generate some points.
points = frozenset(Point(random.randrange(100), random.randrange(100)) for _ in range(100))

# Use clustering algorithm to find clusters.
clusters, centroids = k_means(points, cluster_count=4)

# Plot the different clusters.
for cluster in clusters:
    plt.scatter([point.x for point in cluster], [point.y for point in cluster])

# Plot the means of the clusters.
plt.scatter([centroid.x for centroid in centroids], [centroid.y for centroid in centroids], color='red', linewidths=5, marker="D")

plt.show()