import math
from collections import Counter

def get_cosine(vec1, vec2):
     set(vec1.keys())
     
     set(vec2.keys())
     intersection = (vec1.keys()) & (vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])
     
     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator
def compare(v1,v2,name):
 vector1 = Counter(v1)
 vector2 = Counter(v2)
 cosine = get_cosine(vector1, vector2)
 print ('\nCosine Similiarity:', cosine)
 marks={}
 marks[name]=cosine
 return marks
    
