####---------Code for the crossvalidation-------------####

import input_good
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn import svm
from sklearn import metrics

#window_size = 39

def crossvalidation (filename): 
    for window_size in range(3,41,2):
        x, y =input_good.parser_train(filename, window_size) 
        clf1 = svm.SVC(kernel='linear', C=1, class_weight = "balanced")
        #scores = cross_val_score(clf1, x, y, cv=5,verbose=True, scoring='f1_macro')
        scores = cross_val_score(clf1, x, y, cv=5,verbose=True)
        average_scores = np.average(scores)
        #print(average_scores,window_size)


if __name__ == '__main__':
    #crossvalidation('small_test_gram+.txt')
    crossvalidation('new_train_test_gram+.txt')
    #crossvalidation('big_test_dataset_gram+.txt')
    

