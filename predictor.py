## This code is for predicting the topology of multiple sequences in S if it's signal peptide or . if it's not ###

import input_good
import numpy as np
from sklearn import svm

window_size = 39

def predict_signalP(filename, filename2):
    x,y = input_good.parser_train(filename)
    predicting_topo = input_good.parser_output(filename2)
    #print(predicting_topo)
    #print(len(predicting_topo))
    clf2 = svm.SVC(kernel='linear', C=1)
    clf2.fit(x,y)
    result = clf2.predict(predicting_topo) 
    results = result
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
    predict_signalP('small_test_gram+.txt', 'predict_protein.txt')
    #predict_signalP('small_test_gram+.txt',10) 
    #predict_signalP('new_train_test_gram+.txt',39) 
    #predict_signalP('big_test_dataset_gram+.txt',39) 
