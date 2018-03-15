# Project-in-molecular-life-science
In my project I need to predict signal peptide of gram positive bacteria, which are small sequences around 15-40 residues in the N-terminal site that direct the protein to the cell membrane. I had a big dataset of more than 3.000 sequences, both positive (containing signal peptide (S)) and negative examples (not containing S, but t or .). Given that running my whole dataset is very time-consuming (more than 24h day), I decided to create a smaller dataset of around 40 sequences, trying to maintain the representation of both negativa and positive sequences. This dataset is a FASTA file in text form called new_train_test_gram+.txt which I also attached. In addition, these is the content of my other files: 

Scripts: 
- input_good.py: parsers for both the training set and the protein sequence to predict
- crossval_svm.py: crossvalidation and window size testing. 
- train_SVM_model: training an SVM input and creating the model ('signalP+_model.sav')
- optimized_predictor.py: predictor that includes the model ('signalP+_model.sav') and predicts three sequences ('predict_protein.txt')

Also attached are all the files that I used to train and predict. 
