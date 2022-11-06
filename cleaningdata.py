import csv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
import string
nltk.download('punkt')
nltk.download('stopwords')
stop_words=set(stopwords.words('english'))

def clean_text(text):
    tokenize_words=word_tokenize(text)
    without_stop_words=[]
    for word in tokenize_words:
        if word.lower() not in stop_words:
            without_stop_words.append(word)
     
    new_string="" 
    for x in without_stop_words:
        if ( x not in string.punctuation):
            new_string+=x+" "

    return new_string

def read_write_data():
    
    """
1. index -> Product 
3. index -> Issue
7. index -> Company
8. index -> State
9. index -> Zip Code
17.index -> Complaint ID   
    """
    with open('C:\\Users\\melih\\Desktop\\Github\\Similarity-Test-Between-Complaints-With-Multithreading\\all_data\\rows.csv',encoding='utf-8') as file, open('C:\\Users\\melih\\Desktop\\Github\\Similarity-Test-Between-Complaints-With-Multithreading\\all_data\\clean_data.csv', 'w', newline='') as new_file:
    
        reader=csv.reader(file)
        writer=csv.writer(new_file)
        count = 0
        
        for row in reader:
                    
            if(count==0):
                categories=[]
                categories.append(row[1])
                categories.append(row[3])
                categories.append(row[7])
                categories.append(row[8])
                categories.append(row[9])
                categories.append(row[17])
                writer.writerow(categories)
                count+=1
                continue
            
            if(row[1]!='' and row[3]!='' and row[7]!='' and row[8]!='' and row[9]!='' and row[17]!=''):
                liste = list()
                
                liste.append(clean_text(row[1]))
                liste.append(clean_text(row[3]))
                liste.append(clean_text(row[7]))
                liste.append(row[8])
                liste.append(row[9])
                liste.append(row[17])
                writer.writerow(liste)
            
            count+=1    


read_write_data()
