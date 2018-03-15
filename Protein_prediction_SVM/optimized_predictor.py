###-------This code predicts the topology of multiple sequences as an S if it's signal peptide or . if it's not, in form of ID, sequence and topology----------###

import input_good
import numpy as np
from sklearn import svm
from sklearn.externals import joblib


loaded_model = joblib.load('signalP+_model2.sav')
window_size = 39

def predict_signalP(filename2):
    
    predicting_topo = input_good.parser_output(filename2)
    z = loaded_model.predict(predicting_topo) 
    results = z
    
    signalP_decode = {0:".",4:"S"}
    decoded_topo_list = []
    for element in results:
        decoded_topo_list.append(signalP_decode[element])
    
    endSP = 0
    start = 0
    
    filet = open(filename2,'r+')
    texti = filet.read().splitlines()
    for lines in range(len(texti)):
        #print(lines)
        if texti[lines].startswith (">"):
            endSP = endSP +len(texti[lines+1])
            j ="".join(decoded_topo_list[start:endSP])
            print(texti[lines])
            print(texti[lines+1])
            print(j)
            start = endSP
           
     
    
if __name__ == '__main__':
    predict_signalP('predict_protein.txt')

