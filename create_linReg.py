import pandas as pd
import matplotlib.pyplot as plt
import math
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

# read our dataset from csv
df = pd.read_csv('csv_dataset_follNorm_Nov22.csv', index_col=False)

# isolate the column labels of our explanatory variables
ev_col_labels = df.columns.values
ev_col_labels = ev_col_labels[2:10]

# isolate our explanatory and class variables
data = df.as_matrix(columns=ev_col_labels)
cv = df.change_std

# print, for troubleshooting
print(data)
print(cv)

# fit a linear regression model
regr = linear_model.LinearRegression()
regr.fit(data, df.change_std)

# use our model to predict on our overall dataset
predicted_results = regr.predict(data)

print("\nResults:")
# The coefficients (m, b) of y = m1x1 + m2x2 + ... + b
print('Coefficients (m): \n', ev_col_labels, '\n', regr.coef_)
print('Intercept (b): \n', regr.intercept_)

# The mean square error MSE or the mean residual sum of square of errors
MSE = mean_squared_error(cv, predicted_results)
RMSE = math.sqrt(MSE)
# Explained variance score: 1 is perfect prediction
R2 = r2_score(cv, predicted_results)

print("Mean residual sum of squares =", MSE)
print("RMSE =", RMSE)
print("R2 =", R2)
