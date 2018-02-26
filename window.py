
seq1 = "AMGDEFAM"

dictioseq = {}
dictioseq["A"] = [1,0,0,0,0,0]
dictioseq["D"] = [0,1,0,0,0,0]
dictioseq["G"] = [0,0,1,0,0,0]
dictioseq["E"] = [0,0,0,1,0,0]
dictioseq["F"] = [0,0,0,0,1,0]
dictioseq["M"] = [0,0,0,0,0,1]


     
window_size = 3


def window(seq, window_size):
    for i in range(len(seq)- window_size):
        return(seq[i:i+window_size])

for i in range(len(seq1)-window_size):
    print(seq1[i:i+window_size])
    for i in seq1[i:i+window_size]:
        print(dictioseq[i])    
  
    
    
