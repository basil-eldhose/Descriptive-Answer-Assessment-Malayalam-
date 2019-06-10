from sklearn.metrics.pairwise import cosine_similarity
def compare2(v1,v2,name):
 n1=len(v1)
 n2=len(v2)
 n= abs(n1-n2)
 i=0
 if(n1<n2):
     while(i<n):
         v1.append(0)
         i=i+1
 else:
     while(i<n):
         v2.append(0)
         i=i+1
 vector1=[]
 vector1.append(v1)
 vector2=[]
 vector2.append(v2)

 a=(cosine_similarity(vector1,vector2))
 m=a[0][0]
 print("\nSimiliarity: ",m)
 marks={}
 marks[name]=m
 return marks

