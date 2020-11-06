import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import os


print("analysis is loaded successfully")

default_path_dir = os.getcwd() + '/data_merged'

def get_file_list(path_dir = default_path_dir):
    return os.listdir(path_dir)

def train(Class_Info, Mileage_Result):
    if (Class_Info['정원'][0] >= Class_Info['참여인원'][0]):
#         print("meaningless")
        return (1, 1)
    
    Mileage_Result = Mileage_Result.to_numpy()
    x, y = np.split(Mileage_Result, [-1,], axis = 1)
#     x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)
    
#     y_train = y_train.reshape(-1, 1)
#     y_test = y_test.reshape(-1, 1)
    y = y.reshape(-1, 1)
    
    if (len(np.unique(y)) == 1):
        return (1, 1)
    
    
    svm_clf = Pipeline([
        ('scaler', StandardScaler()),
        ('liear_svc', SVC(kernel='poly', degree=1, coef0=0.1, C=5, probability = True))])
#     svm_clf.fit(x_train, y_train)
    svm_clf.fit(x, y)
    
    
#     y_test_pred = svm_clf.predict(x_test)
    
    
    custom_test = []
    for mileage in range(1, 37):
        for grade in range(2, 5):
            for major in range(0, 2):
                    custom_test.append(np.array([mileage + 0. , major + 0., grade + 0.]))
    
    custom_test = np.array(custom_test)
    custom_result = svm_clf.predict(custom_test)
    prob = svm_clf.predict_proba(custom_test)
    
    min_mileage_nonmajor = 100
    min_mileage_major = 100
    
    for i, test in enumerate(custom_test):
        mileage, major, grade = test[0], test[1], test[2]
        result = custom_result[i]
        if result and prob[i][1] >= 0.7:
            if major:
                min_mileage_major = min(min_mileage_major, mileage)
            else:
                min_mileage_nonmajor = min(min_mileage_nonmajor, mileage)
    
    return min_mileage_nonmajor, min_mileage_major