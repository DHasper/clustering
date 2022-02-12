import matplotlib.pyplot as plt
import matplotlib.markers as marker
import random
from point import Point
from clustering.hierarchical import hierarchical
from clustering.k_means import k_means

# Generate some points.
points = frozenset(Point(random.randrange(300), random.randrange(300)) for _ in range(200))

# Use clustering algorithm to find clusters.
k_means_clusters = k_means(points, cluster_count=8)
hierarchical_clusters = hierarchical(points, cluster_count=8)

# Plot the different clusters.
fig, (plot1, plot2) = plt.subplots(1, 2)

plot1.set_title("k-means clustered points")
for cluster in k_means_clusters:
    plot1.scatter([point.x for point in cluster], [point.y for point in cluster])

plot2.set_title("agglomerative hierarchical clustered points")
for cluster in hierarchical_clusters:
    plot2.scatter([point.x for point in cluster], [point.y for point in cluster])

plt.show()