import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
import statsmodels.api as sm

def generateTemps():
    mean_temp = 5
    st_dev = 1.5
    num_data = 24

    oa_t = np.random.normal(mean_temp,st_dev,num_data)
    daily_fluctuation = 10 * np.sin(np.arange(num_data) * (-2.25 *np.pi / num_data))
    oa_t += daily_fluctuation

    x = np.arange(len(oa_t))
    y = oa_t

    x= x[:,np.newaxis]
    y= y[:,np.newaxis]

    polynomial_features= PolynomialFeatures(degree=5)
    xp = polynomial_features.fit_transform(x)
    model = sm.OLS(y, xp).fit()
    oa_t_pred = model.predict(xp)

    return oa_t, oa_t_pred