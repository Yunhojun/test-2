#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd

def sort_dataset(dataset_df):
	#TODO: Implement this function
    return dataset_df.sort_values('year')

def split_dataset(dataset_df):	
	#TODO: Implement this function
    X_train = dataset_df[:1718]
    X_test = dataset_df[1718:]
    Y_train = dataset_df.salary[:1718] * 0.001
    Y_test = dataset_df.salary[1718:] * 0.001    
    return X_train, X_test, Y_train, Y_test

def extract_numerical_cols(dataset_df):
	#TODO: Implement this function
    list = ['age','G','PA','AB','R','H','2B','3B','HR','RBI','SB','CS','BB',
            'HBP','SO','GDP','fly','war']
    frame = pd.DataFrame(columns=list)
    for i in list:
        frame[i] = dataset_df[i]
    return frame

def train_predict_decision_tree(X_train, Y_train, X_test):
	#TODO: Implement this function
    from sklearn.tree import DecisionTreeRegressor
    dt_reg =  DecisionTreeRegressor()
    dt_reg.fit(X_train, Y_train)
    return dt_reg.predict(X_test)

def train_predict_random_forest(X_train, Y_train, X_test):
	#TODO: Implement this function
    from sklearn.ensemble import RandomForestRegressor
    rf_reg = RandomForestRegressor()
    rf_reg.fit(X_train, Y_train)
    return rf_reg.predict(X_test)

def train_predict_svm(X_train, Y_train, X_test):
	#TODO: Implement this function
    from sklearn.svm import SVR
    svm_reg = SVR()
    svm_reg.fit(X_train, Y_train)
    return svm_reg.predict(X_test)

def calculate_RMSE(labels, predictions):
	#TODO: Implement this function
    return np.sqrt(np.mean((labels - predictions)**2))

if __name__=='__main__':
	#DO NOT MODIFY THIS FUNCTION UNLESS PATH TO THE CSV MUST BE CHANGED.
	data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')
	
	sorted_df = sort_dataset(data_df)	
	X_train, X_test, Y_train, Y_test = split_dataset(sorted_df)
	
	X_train = extract_numerical_cols(X_train)
	X_test = extract_numerical_cols(X_test)

	dt_predictions = train_predict_decision_tree(X_train, Y_train, X_test)
	rf_predictions = train_predict_random_forest(X_train, Y_train, X_test)
	svm_predictions = train_predict_svm(X_train, Y_train, X_test)
	
	print ("Decision Tree Test RMSE: ", calculate_RMSE(Y_test, dt_predictions))	
	print ("Random Forest Test RMSE: ", calculate_RMSE(Y_test, rf_predictions))	
	print ("SVM Test RMSE: ", calculate_RMSE(Y_test, svm_predictions))