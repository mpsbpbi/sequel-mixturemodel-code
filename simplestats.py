import h5py
import bisect
import datetime
import numpy as np

def simplestats( dat ):
  # dat has shape (2, 829440) as in ff['TraceData']['Traces'][myhn-1]
  n = np.apply_along_axis(len,1,dat) # array([829440, 829440])
  s = np.apply_along_axis(sum,1,dat) # 29585235 31033614
  ss = np.sum(dat**2,axis=1) # 1644152845 2052561778
  sxy = np.sum(dat[0,:]*dat[1,:]) # 1443588628
  mean = np.true_divide(s,n) # array([ 35.66892723,  37.41514034])
  var = np.true_divide( ss - np.true_divide(s*s,n), n) # array([  709.97209052,  1074.74290493])
  cov = np.true_divide( sxy - np.true_divide(s[0]*s[1],n[0]),n[0]) # 405.87976057565436
  #return( { "mean":mean, "var":var, "cov":cov, "n":n[0], "s":s, "ss":ss, "sxy":sxy} )
  return( ( mean[0],mean[1], var[0],var[1], cov, n[0], s[0],s[1], ss[0],ss[1], sxy) )

def simplestatsstable( dat ):
  # dat has shape (2, 829440) as in ff['TraceData']['Traces'][myhn-1]
  # take 100 points to estimate means
  #k0 = np.true_divide(sum(dat[0,1000:1100]),len(dat[0,1000:1100]))
  #k1 = np.true_divide(sum(dat[1,1000:1100]),len(dat[1,1000:1100]))
  k0 = dat[0,0]
  k1 = dat[1,0]
  n = len(dat[0,:])
  s0 = np.sum(dat[0,:])
  s1 = np.sum(dat[1,:])
  ss0 = np.sum((dat[0,:]-k0)**2)
  ss1 = np.sum((dat[1,:]-k1)**2)
  sxy = np.sum((dat[0,:]-k0)*(dat[1,:]-k1))
  mean0 = np.true_divide(s0,n)
  mean1 = np.true_divide(s1,n)
  var0 = np.true_divide( ss0 - np.true_divide((s0-k0*n)**2,n), n)
  var1 = np.true_divide( ss1 - np.true_divide((s1-k1*n)**2,n), n)
  cov  = np.true_divide( sxy - np.true_divide((s0-k0*n)*(s1-k1*n),n) ,n) 
  #return( { "mean":mean, "var":var, "cov":cov, "n":n[0], "s":s, "ss":ss, "sxy":sxy} )
  return( ( mean0,mean1, var0,var1, cov, n, s0,s1, ss0,ss1, sxy, k0,k1) )

################################
ff = h5py.File("/mnt/LIMS/vol73/3100134/0001/m54006_151021_185942.trc.h5", "r")

tr = ff['TraceData']['Traces']
hn = ff['TraceData']['HoleNumber']

myhn = bisect.bisect(hn, 48955765)

store = []
start = datetime.datetime.now()
for ii in range(myhn-1,myhn-1+100):
  store.append(simplestatsstable( tr[ii] ) )
end = datetime.datetime.now()

dt = end-start
print dt

print "mean0\tmean1\tvar0\tvar1\tcov\tn\ts0\ts1\tss0\tss1\tsxy\tk0\tk1"
for dd in store:
  print "\t".join([str(xx) for xx in dd])
