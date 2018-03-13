## This code is a test to see if I can manage to predict properly (for predicting the topology of multiple sequences in S if it's signal peptide or . if it's not) ###

import input_good
import numpy as np
from sklearn import svm
from sklearn.externals import joblib


loaded_model = joblib.load('signalP+_model.sav')

window_size = 39

def predict_signalP(filename2):
    
    predicting_topo = input_good.parser_output(filename2)
 
    
    z = loaded_model.predict(predicting_topo) 
    
    results = z
    #print(results)
    
    signalP_decode = {0:".",4:"S"}
    
    decoded_topo_list = []
    
    for element in results:
        decoded_topo_list.append(signalP_decode[element])
    
    #print(decoded_topo_list)
    #print(len(decoded_topo_list))
    
    outputSP = 0
    start = 0

    filet = open(filename2,'r+')
    texti = filet.read().splitlines()
    for lines in range(len(texti)):
        #print(lines)
        if texti[lines].startswith (">"):
            print(texti[lines])
            print(texti[lines+1])
            outputSP = outputSP +len(texti[lines+1])
            j ="".join(decoded_topo_list[start:outputSP])
            print(j)
            start = outputSP
           
     
if __name__ == '__main__':
    predict_signalP('predict_protein.txt')
    #predict_signalP('small_test_gram+.txt',10) 
    #predict_signalP('new_train_test_gram+.txt',39) 
    #predict_signalP('big_test_dataset_gram+.txt',39) 
