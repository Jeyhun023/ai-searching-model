from tqdm import tqdm
from gensim.models import Word2Vec
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import json
import pandas as pd
import csv

#Open questions and dictionary files
q = open("questions.txt", "r")
questions = json.loads(q.read())

#Split and preprocess questions
data = []
for q in questions:
    data.append(q.split(" "))

#Load Word2Vec model
w2v_model = Word2Vec.load("word2vec.model")

#Create TfidfVectorizer and fit questions
tfidf = TfidfVectorizer(token_pattern = '(?u)\\b\\w+\\b')
tfidf.fit_transform(questions)

#Functions for calculating tf_idf staff
def get_tf(a):
  return sent.count(a)/len(sent)

def get_idf(a):
  return tfidf.idf_[tfidf.vocabulary_[a]]

def get_word2vec(a):
  try:
    word_vec = w2v_model.wv[a]
  except:
    word_vec = np.zeros(100)

tfidf_sent_vectors = [] # The tf_diag_idf_wordvec_tf_idf for each sentence is stored in this list

#For each sentence
for sent in tqdm(data): 
  #Calculate tf_idf diagonal
  tf = list(map(get_tf, sent))
  tf_diag = np.diagflat(tf)
  idf = list(map(get_idf, sent))
  idf_diag = np.diagflat(idf)
  tf_idf_diag = np.matmul(tf_diag, idf_diag)

  #Calculate tf_diag and idf
  tf_diag_idf = np.matmul(tf_diag, idf)
  tf_diag_idf = np.float_power(tf_diag_idf, -1)
  tf_diag_idf = np.sum(tf_diag_idf)

  #Word2vec vector
  word_vec = list(map(get_word2vec, sent))
  wordvec_tf_idf = sum(np.matmul(tf_idf_diag, word_vec))
  
  #Calculate final result 
  tf_diag_idf_wordvec_tf_idf = np.multiply(tf_diag_idf, wordvec_tf_idf)
  
  #Adding result to general array
  tfidf_sent_vectors.append(tf_diag_idf_wordvec_tf_idf)
  
print(tf_diag_idf_wordvec_tf_idf) #FINAL_OUTPUT

# data = pd.read_csv("Posts.csv")
# data.sort_values("Title", inplace = True)
# with open('Posts2.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['Id','Title', 'Body', 'Tags', 'LastEditorDisplayName', 'Score', 'ViewCount', 'CreationDate', 'LastEditDate', 'corpus','vector'])
#     for row in tqdm(range(len(data))):
#         writer.writerow([ data['Id'][row], data['Title'][row], data['Body'][row], data['Tags'][row], data['LastEditorDisplayName'][row], data['Score'][row], data['ViewCount'][row], data['CreationDate'][row], data['LastEditDate'][row], questions[row], tfidf_sent_vectors[row]  ])
   

