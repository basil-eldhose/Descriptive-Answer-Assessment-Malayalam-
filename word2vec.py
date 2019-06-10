# -*- coding: utf-8 -*-
import multiprocessing
import gensim.models.word2vec as w2v


num_features =  1
min_word_count = 1
num_workers = multiprocessing.cpu_count()
context_size = 1
downsampling = 1e-3
seed = 1


def feature2vec(feature):
    feature2vec = w2v.Word2Vec(
            sg=1,
            seed=seed,
            workers=num_workers,
            size=num_features,
            min_count=min_word_count,
            window=context_size,
            sample=downsampling
            )

    feature2vec.build_vocab(feature)
    return feature2vec
