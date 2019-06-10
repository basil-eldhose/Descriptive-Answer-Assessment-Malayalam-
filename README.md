sandhi splitter:
	
	Update words in train file (./sandhi-splitter/data directory)
	create model file: sandhisplitter_train -k 3 -s 0 -i TRAINFILE -o MODELFILE (open terminal on /sandhi-splitter/data directory)
	copy model files to  ./anaconda3/lib/python3.7/site-packages/sandhisplitter/models/model.json

Stemming:

	Change to the directory `cd indicstemmer`
 	run command python setup.py install 
	*(delete ./anaconda3/lib/python3.7/site-packages/libindic  before installing updated stemmer)
	
