# This code has the parser that contains the sequence in binary and topology in integer, for further use ###
import collections

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

d = collections.OrderedDict()

#window_size = 3
#flank = window_size//2

def parser_train(filename, window_size):
    file = open(filename,'r+')
    text = file.read().splitlines()
    d = {}
    d = collections.OrderedDict()
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

    binaryseq = []
    mergedbinseq = []
    binarytopo = []    
    
    
    for ID in d.keys():
        
        seq = d.get(ID)[0]   
        topology = d.get(ID)[1]
        flank = window_size//2
        modiseq = ["X"]*flank + list(seq[:80]) + ["X"]*flank
        aa_sequence = ''.join(modiseq)
        moditop = ''.join(list(topology[:80])) 
        
       
        for i in range(0,len(aa_sequence)-2*flank):
            for t in moditop[i]:
                if "S" == moditop[i]:
                    binarytopo.append(4)
                else: 
                    binarytopo.append(0) 
            binaryseq = []
            for i in aa_sequence[i:i+window_size]:
              binaryseq.extend(dictioseq[i])
            mergedbinseq.append(binaryseq)         
        #print(ID, seq, len(seq))
    #print(binarytopo, len(binarytopo))
    #print(len(binarytopo),len(mergedbinseq))
    return(mergedbinseq,binarytopo)


#### This parser has the code to read the file that I will further predict. It's different from the parser_train because this file will only have line for ID and line for sequence ####

d = collections.OrderedDict()
def parser_output(filename):
    file = open(filename,'r+')
    text = file.read().splitlines()
    d =  {}
    d = collections.OrderedDict()
    count=1
    for line in text:
        line = line.rstrip('\n\r')
        if line.startswith(">"):
            key = line.strip(">")
            value = [text[count]]
            d[key] = value
            count=count+2           
    ID = []
    seq = []
    
    binaryseq = []
    mergedbinseq = []
    
    for ID in d.keys():
        seq = d.get(ID)[0]
        modiseq = ["X"]*flank + list(seq[:80]) + ["X"]*flank
        aa_sequence = ''.join(modiseq)        
        

        for x in range(0,len(aa_sequence)-2*flank):
            binaryseq = []
            for x in aa_sequence[x:x+window_size]:
              binaryseq.extend(dictioseq[x])
            mergedbinseq.append(binaryseq) 

        #print(ID, seq,len(seq)) 
    #print(mergedbinseq)      
    #print(ID, modiseq, len(modiseq),len(mergedbinseq))
    return(mergedbinseq)

if __name__ == '__main__':
    parser_train('new_train_test_gram+.txt',3)
    parser_output('testg+2lines.txt')



