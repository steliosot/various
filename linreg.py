import matplotlib.pyplot as plt
import numpy as np
X = [ [6],[8],[10],[14],[18] ]
y = [ [7],[9],[13],[17.5],[18] ]

from sklearn.linear_model import LinearRegression

linreg=LinearRegression()
linreg.fit(X,y)
y_pred= linreg.predict(X)
# plt.figure()
# plt.plot(X,y,'k.')
# plt.plot(X,y_pred)
#
# plt.grid(True)
# plt.show()


print("RSE: ", np.round(np.mean((y-y_pred)**2),2))
print("Variance: ",np.var(X,ddof=1))
X= [a for b in X for a in b]
y= [a for b in y for a in b]
print("Covariance: ",np.cov(X,y)[0][1])

b=np.round(np.cov(X,y)[0][1]/np.var(X,ddof=1),4) #cov(x,y)/var(x)
a=np.round(np.average(y)-(np.cov(X,y)[0][1]/np.var(X,ddof=1))*np.average(X),4) # avg(y)-avg(b)x

print("Model: y=", a ,"+",b,"X")
print(a+b*11)
print(linreg.predict(11));
