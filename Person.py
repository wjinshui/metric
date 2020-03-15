import pandas as pd
from scipy.stats import pearsonr


file = 'grade.csv'
data = pd.read_csv(file)



r_row, p_value = pearsonr(data['(i) Difficulty'], data['(ii) Average_length'])
print (r_row)
print (p_value)


r_row, p_value = pearsonr(data['(i) Difficulty'], data['(v) Ratio_correct'])
print (r_row)
print (p_value)


























