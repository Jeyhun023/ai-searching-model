import pandas as pd
from bs4 import BeautifulSoup
import re
from tqdm import tqdm
import datetime
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import json
import asyncio

data = pd.read_csv("Posts.csv")
data.sort_values("Title", inplace = True)
print("number of duplicated rows",len(data[data.duplicated()]))
print("number of null rows", data[data.isnull().any(1)])
data.drop_duplicates(keep='first')

def striphtml(data):
    soup = BeautifulSoup(data, 'lxml')
    cleantext = soup.get_text()
    soup1 = BeautifulSoup(cleantext, 'html5lib')
    cleantext = soup1.get_text()
    cleantext = re.sub('<.*?>', ' ', str(cleantext))  
    cleantext = re.sub('\\n', ' ', str(cleantext))  
    cleantext=re.sub('\sdiv\s', ' ', str(cleantext), flags=re.MULTILINE|re.DOTALL)
    return cleantext
  
  
def reprocess(data, begin, finish):
    # start = datetime.datetime.now()
    preprocessed_data_list=[]
    preprocessed_data_list_code = []
    # questions_with_code=0
    len_pre=0
    len_post=0
    questions_proccesed = 0
    questions = []
    for row in tqdm(range(begin, finish)):
        # is_code = 0
        title, body = data['Title'][row], data['Body'][row]
        # if '<code>' in body:
        #     questions_with_code+=1
            # is_code = 1
        x = len(body)+len(title)
        len_pre+=x
        code = str(re.findall(r'<code>(.*?)</code>', body, flags=re.DOTALL))
        preprocessed_data_list_code.append(code)
        question = re.sub('<code>(.*?)</code>', '', body, flags=re.MULTILINE|re.DOTALL)#keeping the code content
        question=striphtml(question.encode('utf-8'))
        question=str(title)+" "+str(question)
        question=re.sub(r'[^A-Za-z]+',' ',question)
        words= word_tokenize(str(question.lower()))
    #Removing all single letter and and stopwords from question exceptt for the letter 'c'
        stemmer = SnowballStemmer("english")
        question=' '.join(str(stemmer.stem(j)) for j in words if j not in stopwords.words('english') and (len(j)!=1 or j=='c'))
        preprocessed_data_list.append(question)
        len_post+=len(question)
        questions_proccesed += 1
        questions.append(question)
  
    tfidf = TfidfVectorizer()
    tfidf.fit_transform(questions)
    dictionary = dict(zip(tfidf.get_feature_names(),tfidf.idf_))
    return dictionary, questions



dictionary, questions = reprocess(data, 1, 37515)

f = open("questions.txt", "w")
f.write(json.dumps(questions))
f.close()
f = open("dictionary.txt", "w")
f.write(json.dumps(dictionary))
f.close()