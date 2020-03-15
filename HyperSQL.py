from Metric import Metric
from Statistics import Statistics
import sqlite3
import numpy as np

mydb=sqlite3.connect(r"E:\Git\Projects\Java\SQLParse\src\main\resources\DB.sqlite")
cursor=mydb.cursor()
sql = "select submission_id, grade * 100, approach from exercises_grade   where submission_id in ( select DISTINCT submission_id from exercises_benchmark )"
cursor.execute(sql)
data=cursor.fetchall()
sematic = [d for d in data if d[2] == 'sematic']
syntatic = [d for d in data if d[2] == 'syntatic']
hybrid = [d for d in data if d[2] == 'two_stage_combine']
dynamic = [d for d in data if d[2] == 'dynamic']
two_semantic = [d for d in data if d[2] == 'two_stage_sematic']
two_syntatic = [d for d in data if d[2] == 'two_stage_syntactic']

sql = "select submission_id, avg(grade) from exercises_benchmark group by submission_id"
cursor.execute(sql)
data = cursor.fetchall()
actual = np.array(data)[:, 1:2].astype(np.float64)

hybrid = np.array(hybrid)[:, 1:2].astype(np.float64)
syntatic = np.array(syntatic)[:, 1:2].astype(np.float64)
sematic = np.array(sematic)[:, 1:2].astype(np.float64)
dynamic = np.array(dynamic)[:, 1:2].astype(np.float64)
#two_semantic = np.array(two_semantic)[:, 1:2].astype(np.float64)
#two_syntatic = np.array(two_syntatic)[:, 1:2].astype(np.float64)


def printMetric():
    metric = Metric()
    print("MAE")
    print(metric.mae(actual, hybrid))
    print(metric.mae(actual, syntatic))
    print(metric.mae(actual, sematic))
    print(metric.mae(actual, dynamic))
#    print(metric.mae(actual, two_semantic))
#    print(metric.mae(actual, two_syntatic))
    print("MAPE")
    print(metric.mape(actual, hybrid))
    print(metric.mape(actual, syntatic))
    print(metric.mape(actual, sematic))
    print(metric.mape(actual, dynamic))
#    print(metric.mape(actual, two_semantic))
#    print(metric.mape(actual, two_syntatic))
    print("SMAPE")
    print(metric.smape(actual, hybrid))
    print(metric.smape(actual, syntatic))
    print(metric.smape(actual, sematic))
    print(metric.smape(actual, dynamic))
#    print(metric.smape(actual, two_semantic))
#    print(metric.smape(actual, two_syntatic))
    print("RMSE")
    print(metric.rmse(actual, hybrid))
    print(metric.rmse(actual, syntatic))
    print(metric.rmse(actual, sematic))
    print(metric.rmse(actual, dynamic))
#    print(metric.rmse(actual, two_semantic))
#    print(metric.rmse(actual, two_syntatic))


def printStatic():
    static = Statistics()
    print('actual')
    print(static.getStatistic(actual))
    print('hybrid')
    print(static.getStatistic(hybrid))
    print('syntatic')
    print(static.getStatistic(syntatic))
    print('sematic')
    print(static.getStatistic(sematic))
    print('dynamic')
    print(static.getStatistic(dynamic))

def count(data):
    for i in range(10):
        print('*******' + str(i) + '*********')
        temp = data
        min = i * 10
        if min == 0:
            temp = temp[temp >= min]
        else:
            temp = temp[temp > min]
        temp = temp[temp <= (i+1) * 10]
        print(temp.size)



#printMetric()
#printStatic()

printMetric()


cursor.close()
