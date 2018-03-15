# Project-in-molecular-life-science
In my project I need to predict signal peptide of gram positive bacteria, which are small sequences around 15-40 residues in the N-terminal site that direct the protein to the cell membrane. I had a big dataset of more than 3.000 sequences, both positive (containing signal peptide (S)) and negative examples (not containing S, but t or .). Given that running my whole dataset is very time-consuming (more than 24h day), I decided to create a smaller dataset of around 40 sequences, trying to maintain the representation of both negativa and positive sequences. This dataset is a FASTA file in text form called new_train_test_gram+.txt which I also attached. Moreover, I organised my work into different folders so that they you can run the script with their own dataset. 

These are the following folders:

- SVM: contains input_good.py (parsers), crossval_svm.py (different window size testing), train_SVM_model.py (model creation), and the datasets needed to open those scripts ('new_train_test_gram+.txt' and 'testg+2lines.txt'). 
- Protein_prediction_SVM:to predict input it contains input_good.py for the parsers and the script optimized_predictor.py to obtain the prediction of a set of sequences (file used also included as 'predict_protein.txt'). Also, it includes the datasets needed for the scripts ('new_train_test_gram+.txt' and 'testg+2lines.txt').
- DecisionTree: it contains input_good.py (with all the needed datasets), as well as decision_tree.py (checks the best window size for decision tree classification), and decision_tree_model.py (saves the model). 
- RandomForest: it contains input_good.py (with all the needed datasets), as well as random_forest.py (checks the best window size for random forest classification), and random_forest_model.py (saves the model). 


These are the python scripts used:

- input_good.py: parsers for both the training set and the protein sequence to predict.
- crossval_svm.py: crossvalidation and window size testing. 
- train_SVM_model: training an SVM input and creating the model ('signalP+_model.sav') with window size of 39.
- optimized_predictor.py: predictor that includes the model ('signalP+_model.sav') and predicts three sequences ('predict_protein.txt').
- random_forest: code to test the performance of the random forest classification, for different parameters (window size, n_estimadtors and min_samples_split). 
- random_forest_model: saves the model ('signalP+_model_rfc.sav') with window size of 37.
- decision_tree_.py: code to test the performance of the decision tree classification, for different window sizes.  
- decision_tree_model.py: saves the model ('signalP+_model_dtc.sav') with window size of 33.

