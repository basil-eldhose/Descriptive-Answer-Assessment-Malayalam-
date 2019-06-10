from sandhisplitter import Sandhisplitter
from libindic.stemmer import Stemmer

def cleantext(file):
    
 punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
 
 sentence=file.readlines()

 str1 = ''.join(sentence)
 no_punct = ""
 for char in str1:
   if char not in punctuations:
       no_punct = no_punct + char

 userstring = no_punct.split(" ")
 return userstring


def stemm(token_words):
    print("\nStemmed Text..")
    v = open('temp_file.txt', 'w')
    exceptions=['ഇതെല്ലാം']
    index_nos=[]
    
    v.writelines(["%s\n" % item  for item in token_words])
    v.close()
    u = open("temp_file.txt", "r")
    sentence=u.readlines()
    str1 = ''.join(sentence)
    noise="[]',\n"
    for char in str1:
        if char in noise:
            str1=str1.replace(char," ")
    
    data = str1.split() #split string into a list
    tokenlist=[]
    for word in data:
        tokenlist.append(word)
    for x in tokenlist:
     if x in exceptions:           
        index_nos.append(tokenlist.index(x))
    
    stemmer = Stemmer()
    result = stemmer.stem(language='malayalam', text=str1)
    stemmed=[]
    for word, output in result.items():
        print(output['stem'])
        stemmed.append(output['stem'])
    for i in index_nos:
        stemmed[i+1]=tokenlist[i]
        
    return stemmed  
      

def sandhi_split(token_words):
 print("\n Splitted using Sandhi!!\n--------------------------")   
 temp=[]
 s = Sandhisplitter()
 for word in token_words:
    ss=s.split(word)
    out=ss[0]
    temp.append(out)
    print(out)
 return temp
       

def stop_word(stemmed): 
 list =["അതിൽ","ഇതിൽ","ഇത്","ആണ്","അത്","എന്ന","ഈ","ആ","\n"]
 another_list = []
 print("\nStopwords removed...")
 for x in stemmed:
    if x not in list:           
        another_list.append(x) 
 print("\n",another_list)
 return another_list




    





