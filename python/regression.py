from sklearn.linear_model import Ridge
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import sklearn.metrics as metrics
from math import sqrt

# Regression model evalution
def reg_model_perf(y_set, yhat_set, title_txt):

    ess = metrics.explained_variance_score(y_set, yhat_set)
    mse = metrics.mean_squared_error(y_set, yhat_set) 
    mae = metrics.mean_absolute_error(y_set, yhat_set) 
    med_absolute_error = metrics.median_absolute_error(y_set, yhat_set)
    r_sq = metrics.r2_score(y_set, yhat_set)
    
    print(title_txt)
    print('R-Square: ', r_sq,)
    print('Explained SS: ', ess)
    print('MSE: ', mse)
    print('RMSE: ', np.sqrt(mse))
    print('Mean Absolute Error: ', mae)
    print('Median Absoluate Error:', med_absolute_error, '\n')

# Regression coefficient output
def reg_coeff_out(X, reg_model):
    coeff = pd.DataFrame(reg_model.coef_, X.columns, columns=['Coefficient'])  
    print('(Intercept)', reg_model.intercept_)
    print(coeff)
    
'''
    reg_model_perf
        y_set = Actual value of y
        yhat_set = Predicted value of y
        title_txt = Title
        
    reg_coeff_out
        X = Dataframe of Xs
        model = Output model
'''

# Example
reg_model_perf(y_train, yhat_train_linear, 'Training performance (Linear regression)')
reg_coeff_out(X_temp, linear_fit)


reg_coeff_out(X_temp, linear_fit)
