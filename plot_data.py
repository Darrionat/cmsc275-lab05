import readcsv
import pylab
import stats_utils


def makeHist(data, bins, title, xLabel, yLabel):
    pylab.hist(data, bins)
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    mean = sum(data) / len(data)
    std = stats_utils.std_dev(data)  # Use the function you created for standard deviation
    pylab.annotate('Mean = ' + str(round(mean, 2)) + \
                   '\nSD = ' + str(round(std, 2)), fontsize=20,
                   xy=(0.65, 0.75), xycoords='axes fraction')


weights = readcsv.load_data('Mosquitofish.csv')
stats_utils.statistical_summary(weights, True)
makeHist(weights, 20, "Mosquitofish", "Length", "Frequency")
pylab.savefig('Mosquitofish.pdf')
pylab.show()
