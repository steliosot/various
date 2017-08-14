# Polynomial regression

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

X_train = [ [6],[8],[10],[14],[18] ]
y_train = [ [7],[9],[13],[17.5],[18] ]

X_test = [ [6] , [8], [11], [16] ]
y_test = [ [8], [12], [15], [18] ]

linreg=LinearRegression()
linreg.fit(X_train, y_train)
print("R**2 =", linreg.score(X_test,y_test))

quadratic_feat=PolynomialFeatures(degree=2)
X_train_quad = quadratic_feat.fit_transform(X_train)
X_test_quad = quadratic_feat.transform(X_test)

quadreg = LinearRegression()
quadreg.fit(X_train_quad,y_train)
print("R**2 =", quadreg.score(X_test_quad,y_test))
