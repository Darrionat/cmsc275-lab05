import math

import stats_utils
from scipy.stats import t
from readcsv import load_data


def confidence_interval(confidence, mu, stdev):
    dx = confidence * stdev / math.sqrt(len(data))
    ci = (mu - dx, mu + dx)
    print(ci)
    return ci


def data_confidence_interval(confidence, data):
    mu = stats_utils.mean(data)
    # Population = False, so do sample stdev
    stdev = stats_utils.std_dev(data, False)
    dx = confidence * stdev / math.sqrt(len(data))
    return confidence_interval(confidence, mu, stdev)


stickleback = load_data('Sticklebacks.csv')
bluegill = load_data('Bluegill.csv')
mosquito = load_data('Mosquitofish.csv')

for data in [stickleback, bluegill, mosquito]:
    data_confidence_interval(.95, data)

print(confidence_interval(.95, 4.2, 1.4))
