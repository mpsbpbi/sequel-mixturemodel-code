"""simple kmeans https://gist.github.com/bistaumanga/6023692"""
import numpy as np

def kmeans(xx, centroids, maxIters = 20, minclust=30, maxDiff = 2):

  # Cluster Assignment step
  ca = np.array([np.argmin([np.dot(x_i-y_k, x_i-y_k) for y_k in centroids]) for x_i in xx])
  # all clusters have at least minclust?
  (unique, counts) = np.unique(ca, return_counts=True)
  for cc in counts:
    if cc < minclust:
      return("error: too few", np.array(centroids), ca)
  # Move centroids step
  centroids = np.array([xx[ca == k].mean(axis = 0) for k in range(centroids.shape[0])])

  iter=1
  while (iter<maxIters):
      # Cluster Assignment step
      canew = np.array([np.argmin([np.dot(x_i-y_k, x_i-y_k) for y_k in centroids]) for x_i in xx])
      # all clusters have at least minclust?
      (unique, counts) = np.unique(canew, return_counts=True)
      for cc in counts:
        if cc < minclust:
          return("error: too few", np.array(centroids), canew)
      numdiff = sum(ca != canew)
      if numdiff < maxDiff:
        return("converged", np.array(centroids), canew)
      ca = canew
      # Move centroids step
      centroids = np.array([xx[ca == k].mean(axis = 0) for k in range(centroids.shape[0])])
      iter += 1

  return("error: not converged", np.array(centroids), ca)

def kmeanscov(xx, ca):
  return([np.cov(xx[ca == k],rowvar=0) for k in range(np.max(ca)+1)])
