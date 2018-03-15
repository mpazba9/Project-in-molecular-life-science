###### This should have the code for training an SVM input and save the model ####
import input_good
import numpy as np
from sklearn import svm
from sklearn.externals import joblib 

window_size = 39

def train_test(filenamee):
    x, y =input_good.parser_train(filenamee) 
    clf3 = svm.SVC(kernel='linear', C=1)
    clf3.fit(x,y)
    
    #savefile = 'signalP+_model.sav'
    savefile = 'signalP+_model2.sav'
    joblib.dump(clf3,savefile)
    
if __name__ == '__main__':
    #train_test('small_test_gram+.txt') 
    train_test('new_train_test_gram+.txt') 
    #train_test('big_test_dataset_gram+.txt') 
 

