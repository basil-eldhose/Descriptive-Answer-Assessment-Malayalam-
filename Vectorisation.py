# -*- coding: utf-8 -*-
import pandas as pd
from nltk.tokenize import word_tokenize
#using gensim.models.word2vec package

from word2vec import feature2vec

def vectorise(stemmed_list):
    feature=[]
    for text in stemmed_list:
        feature.append(word_tokenize(text))
    
    feature2vector=feature2vec(feature)
    words=[]

    words=list(feature2vector.wv.vocab)
#    print(words)
    vectors=[]

    vectors=list(feature2vector[words])
    my_list = map(lambda x: x[0], vectors)
    ser = list(my_list)
    print("\nVectors assigned to unique words ..\n\n",ser)
    return ser
    #data=[]   
    #
    #data=split(ser,100)
    #print(data)
    df=pd.DataFrame(ser).T


    df.to_csv('/home/gofreelab/DAA/data22.csv',index=False,header=None )
    
    #csv2set=csvtoset('data22.csv')
