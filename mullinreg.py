X = [ [6,2], [8,1], [10,0], [14,2], [18,0]]
y = [ [7],[9],[13],[17.5],[18] ]

X_test = [ [8,2] , [9,0], [11,2], [16,2] , [12,0] ]
y_test = [ [11], [8.5], [15], [18], [11] ]

linreg = LinearRegression()
linreg.fit(X,y)
print("Coefficients: ",linreg.intercept_, " ", linreg.coef_)
print("R**2 =", linreg.score(X_test,y_test))
