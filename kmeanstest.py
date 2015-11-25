import numpy as np
import kmeans

datin = open("trace-48955765.txt").read().splitlines()
dat = []
for ii in range(1024):
    dat.append([float(xx) for xx in datin[ii].split("\t")])

xx = np.array(dat)

centroids = np.array(
    [[109.50725,  65.26570],
     [ 75.37279,  49.44523],
     [ 48.07525, 122.90891],
     [ 38.31944,  73.09921],
     [ 24.86317,  22.05613]],
    np.float32 )

res = kmeans.kmeans(xx,centroids)
print res

rescov = kmeans.kmeanscov(xx, res[2])
for rr in rescov:
    print rr.flatten() #escov
