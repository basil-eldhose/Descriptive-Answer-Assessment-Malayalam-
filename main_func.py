import glob   
from cosine import compare
from pathlib import Path
import os
import csv
import operator
from preprocess import cleantext,stemm,sandhi_split,stop_word
from Vectorisation import vectorise

def main():    
    
#    Reading Standard answer key and converts into vector form
    
    standardans = open("./txtData/standardans","r") #specify correct path
    std=cleantext(standardans)
       
    std=sandhi_split(std)
    std=stemm(std)
    std=stop_word(std)
    vec2=vectorise(std)
#-----------------------------------------------------------    
    
#    FILE_PATH=input("Enter file path: ")
#    print("file path is: ",FILE_PATH)
#    text_file= open(FILE_PATH ,"r")
         
    path = './txtData/*.txt'   
    files=glob.glob(path)
    os.remove("point.csv")

    for file in files:     
        text_file=open(file, 'r')
        name=Path(file).resolve().stem

        
        x=cleantext(text_file)
        print("\n\n",name,"\n",x)
        st=sandhi_split(x)
        stm=stemm(st)
        cleaned_text=stop_word(stm)
        vectorised=vectorise(cleaned_text)
    
        marks={} 
        marks=compare(vectorised,vec2,name)
#   
#    
#   stores  marks of students into csv file.
        with open('point.csv', 'a') as f:
            for key in marks.keys():
                f.write("%s,%s\n"%(key,marks[key]))
                
        data = csv.reader(open('point.csv'),delimiter=',')
        sortedlist = sorted(data, key=operator.itemgetter(1),reverse=True)
        
        
    #sorted mark list is stored in external file.
        with open("ranked.csv", "w") as f:
          fileWriter = csv.writer(f, delimiter=',')
          for row in sortedlist:
              fileWriter.writerow(row)
    
    


if __name__ == '__main__':
 main()