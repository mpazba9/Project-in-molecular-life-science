dictioseq = {}
dictioseq["X"] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dictioseq["A"] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dictioseq["D"] = [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dictioseq["G"] = [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dictioseq["E"] = [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dictioseq["F"] = [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dictioseq["M"] = [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dictioseq["T"] = [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
dictioseq["K"] = [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
dictioseq["R"] = [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
dictioseq["H"] = [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
dictioseq["S"] = [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
dictioseq["C"] = [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
dictioseq["L"] = [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
dictioseq["N"] = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
dictioseq["I"] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
dictioseq["Q"] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
dictioseq["V"] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
dictioseq["W"] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
dictioseq["Y"] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
dictioseq["P"] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]

dictiotopo = {"C": 0, "S":1, "M":2}

window_size = 3


file = open("testg+.txt",'r+')
text = file.read().splitlines()
d = {}
count=1
for line in text:
    line = line.rstrip('\n\r')
    if line.startswith(">"):
        key = line.strip(">")
        d[key] = [text [count], text [count+1]]
        count=count+3
seq = []
#seq is a string
ID = []
topology = [] 


for ID in d.keys():
    seq = d.get(ID)[0]   
    topology = d.get(ID)[1]
    modiseq = ["X"] + list(seq) + [2*"X"]
    aa_sequence = ''.join(modiseq)
    moditop = ''.join(list(topology))
    #print(ID,seq,topology,modiseq)
    print(aa_sequence)
    #print(moditop)
    
    binaryseq = []
    mergedbinseq = []
    binarytopo = []
    mergedbintopo = []
    
    for i in range(len(aa_sequence)-window_size):
      #print(aa_sequence[i:i+window_size])
      #print(moditop[i])
      for t in moditop[i]:
        #print(dictiotopo[t])
        binarytopo.append(dictiotopo[t]) 
      for i in aa_sequence[i:i+window_size]:
        binaryseq.extend(dictioseq[i])
    mergedbinseq.extend(binaryseq)  
    mergedbintopo.extend(binarytopo)
    print(mergedbinseq)
    print(mergedbintopo) 

"""import numpy as numpy
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()

X_train = 
X_test = 
y_train = 
y_test = 

test size es 0.4 porque es el 40%
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.4, random_state=0)

El kernel lo tengo que ir probando i mirando cuanto da el score
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
clf.score(X_test, y_test)                           



from sklearn.model_selection import cross_val_predict
predicted = cross_val_predict(clf, iris.data, iris.target, cv=10)


"""    
