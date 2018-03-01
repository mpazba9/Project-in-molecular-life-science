#Sequence dictionaries
seq1 = "AMGDEFAM"

dictioseq = {}
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


#Topology dictionaries
topology = "SSSSMMMM"

dictiotopo = {}
dictiotopo["S"] = [1]
dictiotopo["M"] = [2]
dictiotopo["C"] = [0]
     


###Parse to extract features###
flank = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


def parse_fasta(filename):
    filehandle = open(filename,'r')
    text = filehandle.read().splitlines()
    d = {}
    count=1
    for line in text:
        line = line.rstrip('\n\r')
        if line.startswith(">"):
            key = line.strip(">")
            d[key] = [text [count], text [count+1]]
            count=count+3
    seq = []
    ID = []
    topology = []    
    for ID in d.keys():
        seq = d.get(ID)[0]   
        topology = d.get(ID)[1]
        modiseq = flank + [seq] + flank 
        #print(ID,seq,topology,modiseq)
    return(d)
#add file.close()
#print(parse_fasta("testg+.txt"))

parse_fasta("testg+.txt")
 
 

 
#Window size
window_size = 3


##Function for window size###
def window(modiseq, window_size):
    flanking = window_size//2
    for i in range(len(modiseq)- 2* flanking):
        print(modiseq)

"""mergedbinseq = []
        for i in range(len(modiseq)-window_size):
            print(modiseq[i:i+window_size])
            print(topology[i])
            binaryseq = []
            for i in modiseq[i:i+window_size]:
                binaryseq.append(dictioseq[i])
            mergedbinseq.extend(binaryseq)    
            print(binaryseq) 
            
        for i in range(len(topology)-window_size):    
            binarytopo = []
            for i in topology:
                binarytopo.append(dictiotopo[i])    
            
        print(mergedbinseq)
        print(binarytopo)"""

#mergedbinseq prints me the binary code of my seq1, with sliding window of three     
  


#from sklearn.model_selection import cross_val_predict
#predicted = cross_val_predict(clf, iris.data, iris.target, cv=10)
