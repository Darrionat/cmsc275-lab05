# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 12:48:28 2019

@author: Kerri-Ann Norton
"""
import math

import stats_utils

# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 13:38:31 2019

@author: Kerri Norton
Hypothesis Testing (t-tests)
"""
import numpy
import pylab
from readcsv import load_data
import random
import scipy
from scipy.stats import ttest_1samp


#
# tStat = -2.13165598142  # t-statistic for PED-X example
# tDist = []
# numBins = 1000
# for i in range(10000000):
#     tDist.append(numpy.random.standard_t(190))
#
# pylab.hist(tDist, bins=numBins,
#            weights=pylab.array(len(tDist) * [1.0]) / len(tDist))
# pylab.axvline(tStat, color='w')
# pylab.axvline(-tStat, color='w')
# pylab.title('T-distribution with 190 Degrees of Freedom')
# pylab.xlabel('T-statistic')
# pylab.ylabel('Probability')
# pylab.show()

def effect_size(mean, pop_mean, sample_stdev):
    return abs((mean - pop_mean) / sample_stdev)


stickleback = load_data('Sticklebacks.csv')
bluegill = load_data('Bluegill.csv')
mosquito = load_data('Mosquitofish.csv')

mosquitoMean = stats_utils.mean(mosquito)
print('mosquitoMean', mosquitoMean, '\n')

for data in [stickleback, bluegill, mosquito]:
    sample_mean = stats_utils.mean(data)
    samples = random.sample(data, 20)
    # Comparing to mosquitoMean
    tStat, twoTailProb = ttest_1samp(samples, mosquitoMean)
    print('mean', sample_mean)
    print('t-statistic: ', tStat)
    print('p-value: ', twoTailProb)
    if tStat > 2.0930:
        print('*Critical*')
        print('Effectsize', effect_size(sample_mean, mosquitoMean, stats_utils.std_dev(data, False)))
    print('')
# Result is: t-statistic: -0.918, p-value:0.378
