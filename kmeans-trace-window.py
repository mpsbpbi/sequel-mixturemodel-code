import kmeans
import h5py
import bisect
import datetime
import numpy as np
import sys

ff = h5py.File("/mnt/LIMS/vol73/3100134/0001/m54006_151021_185942.trc.h5", "r")

tr = ff['TraceData']['Traces']
hn = ff['TraceData']['HoleNumber']
myhn = bisect.bisect(hn, int(sys.argv[1])-1)
window = 1024

numwin = len(tr[myhn][0])/window
results = []

starttime = datetime.datetime.now()

for ii in range(numwin):

  start = (ii*window)
  end = start + window
  xx = np.transpose(tr[myhn][:,start:end])

  # simplest k-means
  centroids = np.array(
      [[109.50725,  65.26570],
       [ 75.37279,  49.44523],
       [ 48.07525, 122.90891],
       [ 38.31944,  73.09921],
       [ 24.86317,  22.05613]],
      np.float32 )

  res = kmeans.kmeans(xx,centroids)

  if not "error" in res[0]:
    rescov = kmeans.kmeanscov(xx, res[2])
    for kk in range(res[1].shape[0]):
          results.append( np.concatenate( [ np.array([myhn,ii,kk]), res[1][kk], rescov[kk].flatten() ] ))

for dd in results:
  print "\t".join([str(xx) for xx in dd])

endtime = datetime.datetime.now()
print endtime-starttime

