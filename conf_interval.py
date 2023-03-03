import stats_utils
from scipy.stats import t
from readcsv import load_data


def confidence_interval(confidence, df):
    c = t.interval(confidence, df)
    print(c)
    return c


stickleback = load_data('Sticklebacks.csv')
bluegill = load_data('Bluegill.csv')
mosquito = load_data('Mosquitofish.csv')

for data in [stickleback, bluegill, mosquito]:
    confidence_interval(.95, 9)
