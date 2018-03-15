####Decision tree classification algorithm####

import input_good
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier 
from sklearn import tree




def DecisiontreeC(filen):
    for window_size in range(23,45,2):
        m,n = input_good.parser_train(filen, window_size) 
        clf_dt = tree.DecisionTreeClassifier(class_weight = "balanced")       
        clf_dt.fit(m,n)   
        scores = cross_val_score(clf_dt, m, n, cv=5,verbose=True)             
        average_scores = np.average(scores)            
        #print(average_scores, window_size)       

if __name__ == '__main__':
    DecisiontreeC('new_train_test_gram+.txt')

