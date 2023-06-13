#4.SORUM :

from sklearn.linear_model import LinearRegression

X = [[x1[i], x2[i], x3[i], x4[i]] for i in range(len(x1))]
Y1 = y1
Y2 = y2
Y3 = y3

regressor1 = LinearRegression()
regressor1.fit(X, Y1)
coefficients1 = regressor1.coef_
intercept1 = regressor1.intercept_

regressor2 = LinearRegression()
regressor2.fit(X, Y2)
coefficients2 = regressor2.coef_
intercept2 = regressor2.intercept_

regressor3 = LinearRegression()
regressor3.fit(X, Y3)
coefficients3 = regressor3.coef_
intercept3 = regressor3.intercept_

print("Katsayılar:")
print("(y1) =", round(intercept1, 2), "+", round(coefficients1[0], 2), "*(x1)", round(coefficients1[1], 2), "*(x2)", round(coefficients1[2], 2), "*(x3)", round(coefficients1[3], 2), "*(x4)")
print("(y2) =", round(intercept2, 2), "+", round(coefficients2[0], 2), "*(x1)", round(coefficients2[1], 2), "*(x2)", round(coefficients2[2], 2), "*(x3)", round(coefficients2[3], 2), "*(x4)")
print("(y3) =", round(intercept3, 2), "+", round(coefficients3[0], 2), "*(x1)", round(coefficients3[1], 2), "*(x2)", round(coefficients3[2], 2), "*(x3)", round(coefficients3[3], 2), "*(x4)")

Yeni = [5, 3.4, 1.5, 0.2] örneği (y3) sınıfına aittir.