##trying random forest classification, different parameters ###

import input_good
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier as rf
from sklearn.tree import DecisionTreeClassifier as dt




def RandomForestC (filenamerfc):
    for window_size in range(35,43,2):
        for n_estimators_new in (100,200,300,400,500):
            for min_samples_split_new in range (2,5):
                o,u = input_good.parser_train(filenamerfc, window_size) 
                clf_rfc = rf(n_estimators = n_estimators_new, min_samples_split = min_samples_split_new, n_jobs = 1)
                clf_rfc.fit(o,u)
                scores = cross_val_score(clf_rfc, o, u, cv=5,verbose=True)
                #--f1 score --# scores = cross_val_score(clf_rfc, o, u, cv=5,verbose=True, scoring='f1_macro')
                average_scores = np.average(scores)
                #print(average_scores,window_size, n_estimators_new, min_samples_split_new)




###--------------------------balanced and good one----------------------------####

def RandomForestC_balanced (filenamerfc):
    for window_size in range(35,43,2):
        for n_estimators_new in (100,200,300,400,500):
            for min_samples_split_new in range (2,5):
                o,u = input_good.parser_train(filenamerfc, window_size) 
                clf_rfc = rf(n_estimators = n_estimators_new, min_samples_split = min_samples_split_new, n_jobs = 1, class_weight = "balanced")
                clf_rfc.fit(o,u)
                scores = cross_val_score(clf_rfc, o, u, cv=5,verbose=True)
                #--f1 score --# scores = cross_val_score(clf_rfc, o, u, cv=5,verbose=True, scoring='f1_macro')
                average_scores = np.average(scores)
                print(average_scores,window_size, n_estimators_new, min_samples_split_new)



if __name__ == '__main__':
    #RandomForestC('new_train_test_gram+.txt')
    RandomForestC_balanced('new_train_test_gram+.txt')

