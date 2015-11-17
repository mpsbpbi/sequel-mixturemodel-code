import h5py

ff = h5py.File("/mnt/LIMS/vol73/3100134/0001/m54006_151021_185942.trc.h5", "r")

print ff.keys()
# [u'ScanData', u'TraceData']

print ff['TraceData'].keys()
# [u'ActiveChipLooks', u'Codec', u'HPFrameSet', u'HoleChipLook', u'HoleNumber', u'HolePhase', u'HoleStatus', u'HoleType', u'HoleXY', u'HoleXYPlot', u'IFVarianceScale', u'OFBackgroundMean', u'OFBackgroundVariance', u'RVFrameSet', u'ReadVariance', u'Spectra', u'Traces', u'VFrameSet', u'Variance']

dd = ff['TraceData']['Spectra']

print dd.shape
# (4, 207360, 2)

print dd.dtype
# dtype('float32')
