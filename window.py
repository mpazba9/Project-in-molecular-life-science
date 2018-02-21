
seq1 = "AMGDEF"

dictioseq = {}
dictioseq["A"] = [1,0,0,0,0,0]
dictioseq["D"] = [0,1,0,0,0,0]
dictioseq["G"] = [0,0,1,0,0,0]
dictioseq["E"] = [0,0,0,1,0,0]
dictioseq["F"] = [0,0,0,0,1,0]
dictioseq["M"] = [0,0,0,0,0,1]


for i in range(0,len(seq1)): 
    b = [seq1[i:i+3] for i in range(len(seq1)-2)]
    #print(seq1[i])
    
print(b) 
print(dictioseq)

for aa in b: 
    

   
     

#Both codes work    
"""def window(seq, window_size=5):
    for i in range(len(seq) - window_size + 1):
        yield seq[i:i+window_size]
for seq in window(seq1, 3):
    print(seq)
    #print(dictioseq)

merged = dictioseq.values(seq)
print(merged)"""

