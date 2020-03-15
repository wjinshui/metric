import numpy as np

class Statistics:
    def getStatistic(self, data):
        mean = np.mean(data)
        max = np.max(data)
        min = np.min(data)
        median = np.median(data)
        std = np.std(data, ddof= 1)
        return mean, median,  min, max, std


