import input_good
import numpy as np
from sklearn import svm
from sklearn.externals import joblib
from sklearn.metrics import matthews_corrcoef
from sklearn.model_selection import cross_val_predict


savedmodel= joblib.load('signalP+_model2.sav')
window_size = 39


def MCC(model, X, Y):
    performance = cross_val_predict(savedmodel, X, Y)
    MCC_accuracy = matthews_corrcoef(Y, performance)
    #return (MCC_accuracy))

if __name__ == "__main__":
    #print(MCC_accuracy())

