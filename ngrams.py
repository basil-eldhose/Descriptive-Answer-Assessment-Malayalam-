from nltk import ngrams
file = open("/home/gofreelab/answer1","r")
sentence =file.readlines()
str1 = ''.join(sentence)


def n_grams(str,n):
        twograms = ngrams(str.split(),n)
        used=set()
        unique = [x for x in twograms if x not in used and (used.add(x) or True)]
        return unique

bigrams=n_grams(str1,2)
print(bigrams)
    
trigrams=n_grams(str1,3)
print(trigrams)
     
quadgrams=n_grams(str1,4)
print(quadgrams)