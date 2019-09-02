from sklearn.model_selection import train_test_split

# Separate x and y matrices
X_temp = data.drop(['Y_NAME'], axis = 1)
y_temp = data['Y_NAME']

# Turn into values
X = X_temp.values
y = y_temp.values

# Split into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

print(X_train.shape)
print(X_test.shape)

# Check missing values
def chk_null_df(df_name):
    print('Percentage of missing value in the dataframe')
    print(df_name.isnull().sum()/df_name.shape[0]*100, '\n')
