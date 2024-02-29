## Size Constrained Clustering Solver

Implementation of Deterministic Annealing Size Constrained Clustering. 
Size constrained clustering can be treated as an optimization problem. Details could be found in a set of reference paper.

This is a fork of https://github.com/jingw2/size_constrained_clustering that solves installation issues. And mantains only the Determinstic Annealing clustering.

### Installation
Requirement Python >= 3.6, Numpy >= 1.13
* install from PyPI
```shell
pip install light-size-constrained-clustering
```

### Methods
* Deterministic Annealling Algorithm: Input target cluster distribution, return correspondent clusters

### Usage:

Deterministic Annealing
```python
# setup
from light_size_constrained_clustering import da
import numpy as np

n_samples = 40 # number cells in spot
n_clusters = 4 # distinct number of cell types
distribution= [0.4,0.3,0.2,0.1] # distribution of each cell type (form deconv)
seed = 17

print(np.sum(distribution))
np.random.seed(seed)

X = np.random.rand(n_samples, 2)
# distribution is the distribution of cluster sizes
model = da.DeterministicAnnealing(n_clusters, distribution= distribution, random_state=seed)

model.fit(X)
centers = model.cluster_centers_
labels = model.labels_
print("Labels:")
print(labels)
print("Elements in cluster 0: ", np.count_nonzero(labels == 0))
print("Elements in cluster 1: ", np.count_nonzero(labels == 1))
print("Elements in cluster 2: ", np.count_nonzero(labels == 2))
print("Elements in cluster 3: ", np.count_nonzero(labels == 3))
```

In case of provided distributions not being respected due to lack of convergence, distribution can
be nforced by using the parameter `enforce_cluster_distribution`

```model.fit(X, enforce_cluster_distribution=True)```


Cluster size: 16, 12, 8 and 4 in the figure above, corresponding to distribution [0.4, 0.3, 0.2, 0.1]


## Copyright
Copyright (c) 2023 Jing Wang & Albert Pla. Released under the MIT License. 

Third-party copyright in this distribution is noted where applicable.

### Reference
* [Clustering with Capacity and Size Constraints: A Deterministic
Approach](http://web.eecs.umich.edu/~mayankb/docs/ClusterCap.pdf)
* [Deterministic Annealing, Clustering and Optimization](https://thesis.library.caltech.edu/2858/1/Rose_k_1991.pdf)
* [Deterministic Annealing, Constrained Clustering, and Opthiieation](https://authors.library.caltech.edu/78353/1/00170767.pdf)
* [Shrinkage Clustering](https://www.researchgate.net/publication/322668506_Shrinkage_Clustering_A_fast_and_size-constrained_clustering_algorithm_for_biomedical_applications)
* [Clustering with size constraints](https://www.researchgate.net/publication/268292668_Clustering_with_Size_Constraints)
* [Data Clustering with Cluster Size Constraints Using a Modified k-means Algorithm](https://core.ac.uk/download/pdf/61217069.pdf)
* [KMeans Constrained Clustering Inspired by Minimum Cost Flow Problem](https://github.com/joshlk/k-means-constrained)
* [Same Size Kmeans Heuristics Methods](https://elki-project.github.io/tutorial/same-size_k_means)
* [Google's Operations Research tools's
`SimpleMinCostFlow`](https://developers.google.com/optimization/flow/mincostflow)
* [Cluster KMeans Constrained](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-2000-65.pdf)
