# Evaluating the model
import numpy as np
from sklearn.linear_model import LinearRegression

X = [ [6],[8],[10],[14],[18] ]
y = [ [7],[9],[13],[17.5],[18] ]

X_test = [ [8] , [9], [11], [16] , [12] ]
y_test = [ [11], [8.5], [15], [18], [11] ]

linreg=LinearRegression()
linreg.fit(X,y)

# Calculate RSE
y_avg = np.mean(y_test)
y_pred = linreg.predict(X_test)

print(y_avg)
TSS = sum((y_test-y_avg)**2)
RSS = sum((y_test-y_pred)**2)

print("TSS: ", TSS)
print("RSS: ", RSS)

print("R**2 = ", linreg.score(X_test, y_test))
print("R**2 = ", 1-RSS/TSS)
