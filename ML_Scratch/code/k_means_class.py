import numpy as np
np.random.seed(42)

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1- x2)**2))

class kmeans():
    def __init__(self, k=3, max_iters=100, plot_steps=False):
        self.k = k
        self.max_iters = max_iters
        self.plot_steps = plot_steps
    
        # list of sample indices for each cluster
        self.clusters = [[] for _ in range(self.k)]

        # mean feature vector for each cluster
        self.centroids = []

    def predict(self, X):
        self.X = X
        self.n_samples, self.n_features = X.shape

        # initialize centroids
        random_sample_idxs = np.random.choice(self.n_samples, self.k, replace=False)
        self.centroids = [self.X[idx] for idx in random_sample_idxs]

        # optimization
        for _ in range(self.max_iters):
            # update clusters
            self.clusters = self._create_clusters(self.centroids)
            # update the centroids
            centroids_old = self.centroids
            self.centroids = self._get_centroids(self.clusters)
            # check if converged
            if self_is_converged(centroids_old, self.centroids):
                break
        
        # return cluster labels
        return self._get_cluster_labels(self.cluster)

        def _get_cluster_labels(self, cluster):
            labels = np.empty(self.n_samples)
            for cluster_idx, cluster in enumerate(clusters):
                for sample_idx in cluster:
                    labels[sample_idx] = cluster_idx
            return labels

        def _create_clusters(self, centroids):
            clusters = [[] for _ in range(self.k)]
            for idx, sample in enumerate(self.X):
                centroid_idx = self._closest_centroid(sample, centroids)
                clusters[centroid_idx].append(idx)
            return clusters

        def _closest_centroid(self, sample, centroids):
            distances = [euclidean_distance(sample, point) for point in centroids]
            closest_idx = np.argmin(distances)
            return closest_idx
        
        def _get_centroids(self, clusters):
            centroids = np.zeros(self.k, self.n_features)
            for cluster_idx, cluster in enumerate(clusters):
                cluster_mean = np.mean(self.X[cluster], axis=0)
                centroids[cluster_idx] = cluster_mean
            return centroids

        def _is_converged(self, centroids_old, centroids):
            distances = [euclidean_distance(centroids_old[i], centroids[i]) for i in range(self.k)]
            return sum(distances) == 0