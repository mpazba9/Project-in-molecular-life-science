####------storing DT model-------####

import input_good
import numpy as np
from sklearn import svm
from sklearn.externals import joblib 
from sklearn.model_selection import cross_val_score 
from sklearn.tree import DecisionTreeClassifier 
from sklearn import tree


window_size = 33

def DecisiontreeC(filenam):
    m,n = input_good.parser_train(filenam, window_size) 
    clf_dt = tree.DecisionTreeClassifier(class_weight = "balanced")       
    clf_dt.fit(m,n)
    
    savefile = 'signalP+_model_dtc.sav'
    joblib.dump(clf_dt,savefile, compress = 9)
    
if __name__ == '__main__':
    DecisiontreeC('new_train_test_gram+.txt') 
