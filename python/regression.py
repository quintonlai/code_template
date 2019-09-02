#Regression model evalution
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

'''
    reg_model_perf
    y_set = Actual value of y
    yhat_set = Predicted value of y
    title_txt = Title
'''

# Example
reg_model_perf(y_train, yhat_train_linear, 'Training performance (Linear regression)')
