# import pandas as pd
# from bs4 import BeautifulSoup
# import re
# from tqdm import tqdm
# import datetime
# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.stem import SnowballStemmer
# from nltk.corpus import stopwords
# nltk.download('punkt')
# nltk.download('stopwords')
# from gensim.models import Word2Vec
# from sklearn.feature_extraction.text import TfidfVectorizer
# import numpy as np
# data = pd.read_csv("Posts.csv")
# data.sort_values("Title", inplace = True)
# print("number of duplicated rows",len(data[data.duplicated()]))
# print("number of null rows", data[data.isnull().any(1)])
# data.drop_duplicates(keep='first')
# def striphtml(data):
#     soup = BeautifulSoup(data, 'lxml')
#     cleantext = soup.get_text()
#     soup1 = BeautifulSoup(cleantext, 'html5lib')
#     cleantext = soup1.get_text()
#     cleantext = re.sub('<.*?>', ' ', str(cleantext))  
#     cleantext = re.sub('\\n', ' ', str(cleantext))  
#     cleantext=re.sub('\sdiv\s', ' ', str(cleantext), flags=re.MULTILINE|re.DOTALL)
#     return cleantext
# start = datetime.datetime.now()
# preprocessed_data_list=[]
# preprocessed_data_list_code = []
# questions_with_code=0
# len_pre=0
# len_post=0
# questions_proccesed = 0
# questions = []
# for row in tqdm(range(len(data))):
#     is_code = 0
#     title, question = data['Title'][row], data['Body'][row]
#     if '<code>' in question:
#         questions_with_code+=1
#         is_code = 1
#     x = len(question)+len(title)
#     len_pre+=x
#     code = str(re.findall(r'<code>(.*?)</code>', question, flags=re.DOTALL))
#     preprocessed_data_list_code.append(code)
#     question = re.sub('<code>(.*?)</code>', '', question, flags=re.MULTILINE|re.DOTALL)#keeping the c>
#     question=striphtml(question.encode('utf-8'))
#     question=str(title)+" "+str(question)
#     question=re.sub(r'[^A-Za-z]+',' ',question)
#     words= word_tokenize(str(question.lower()))
#     #Removing all single letter and and stopwords from question exceptt for the letter 'c'
#     stemmer = SnowballStemmer("english")
#     question=' '.join(str(stemmer.stem(j)) for j in words if j not in stopwords.words('english') and >
#     preprocessed_data_list.append(question)
#     len_post+=len(question)
#     questions_proccesed += 1
#     questions.append(question)
# no_dup_avg_len_pre=(len_pre*1.0)/questions_proccesed
# no_dup_avg_len_post=(len_post*1.0)/questions_proccesed
# print( "\nAvg. length of questions(Title+Body) before processing: %d"%no_dup_avg_len_pre)
# print( "\nAvg. length of questions(Title+Body) after processing: %d"%no_dup_avg_len_post)
# print ("\nPercent of questions containing code: %d"%((questions_with_code*100.0)/questions_proccesed))
# print("\nTime taken to run this cell :", datetime.datetime.now() - start)
# tfidf = TfidfVectorizer()
# tfidf.fit_transform(questions)
# dictionary = dict(zip(tfidf.get_feature_names(),tfidf.idf_))

# import json
# f = open("questions.txt", "w")
# f.write(json.dumps(questions))
# f.close() 

# f = open("dictionary.txt", "w")
# f.write(json.dumps(dictionary))
# f.close() 


#  for word in sent: # for each word in a review/sentence
#     if word in tfidf_feat:
#       vec = w2v_model.wv[word]
#       print(vec)
#         # tf_idf = tf_idf_matrix[row, tfidf_feat.index(word)]
#         # to reduce the computation we are 
#         # dictionary[word] = idf value of word in whole courpus
#         # sent.count(word) = tf valeus of word in this review
#       tf_idf = dictionary[str(word)]*(sent.count(word)/len(sent))
#       sent_vec+= (vec*tf_idf)
#       weight_sum += tf_idf
#   if weight_sum !=0:
#     sent_vec /= weight_sum 
#   tfidf_sent_vectors.append(sent_vec)
#   row+=1

import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())