import numpy as np
from sklearn import metrics
import math
class Metric:

    def mape(self, y_true, y_pred):
        return np.mean(np.abs((y_pred - y_true) / y_true)) * 100

    def smape(self, y_true, y_pred):
        return 2.0 * np.mean(np.abs(y_pred - y_true) / (np.abs(y_pred) + np.abs(y_true))) * 100

    def mse(self, y_true, y_pred):
        return metrics.mean_squared_error(y_true, y_pred)

    def rmse(self, y_true, y_pred):
        return np.sqrt(metrics.mean_squared_error(y_true, y_pred))

    def mae(self, y_true, y_pred):
        return metrics.mean_absolute_error(y_true, y_pred)

    def smape_fast(self, y_true, y_pred):
        return 100/len(y_true) * np.sum(2 * np.abs(y_pred - y_true) / (np.abs(y_true) + np.abs(y_pred)))

    def smape2(self, y_true, y_pred):
        denominator = (np.abs(y_true) + np.abs(y_pred))
        diff = np.abs(y_true - y_pred) / denominator
        diff[denominator == 0] = 0.0
        return 200 * np.mean(diff)
def main():
    y_true = np.array([1.0, 5.0, 4.0, 3.0, 2.0, 5.0, -3.0])
    y_pred = np.array([1.0, 4.5, 3.5, 5.0, 8.0, 4.5, 1.0])

    metric = Metric()
    print(metric.mse(y_true, y_pred))    # 8.107142857142858
    print(metric.rmse(y_true, y_pred))   # 2.847304489713536
    print(metric.mae(y_true, y_pred))    # 1.9285714285714286
    print(metric.mape(y_true, y_pred))   # 76.07142857142858
    print(metric.smape(y_true, y_pred))  # 57.76942355889724
    print(metric.smape_fast(y_true, y_pred))
    print(metric.smape2(y_true, y_pred))


if __name__ == '__main__':
    main()