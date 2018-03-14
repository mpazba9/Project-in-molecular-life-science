## Storing RFC model###
import input_good
import numpy as np
from sklearn import svm
from sklearn.externals import joblib 
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier as rf

window_size = 37

def model_RFC(filenameet):
    o,u = input_good.parser_train(filenameet, window_size) 
    clf_rfc = rf(n_estimators = 300, min_samples_split = 4, n_jobs = 1, class_weight = "balanced")
    clf_rfc.fit(o,u)
    
    savefile = 'signalP+_model_rfc.sav'
    joblib.dump(clf_rfc,savefile, compress = 9)
    
if __name__ == '__main__':
    model_RFC('new_train_test_gram+.txt') 
    


