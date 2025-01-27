num_outliers_to_remove= 50
cleaned_x_train = X_train
cleaned_y_train = y_train
num_outliers_removed = 0

for i in range(num_outliers_to_remove):

    lin = LinearRegression().fit(cleaned_x_train, cleaned_y_train)
    
    y_pred = lin.predict(cleaned_x_train)
    squared_errors = (y_pred - cleaned_y_train) ** 2

    idx = np.argmax(squared_errors)
    
    cleaned_x_train = np.delete(cleaned_x_train, idx, axis=0)
    cleaned_y_train = np.delete(cleaned_y_train, idx, axis=0)
    
    num_outliers_removed += 1
