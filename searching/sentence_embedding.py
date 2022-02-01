from tqdm import tqdm
from gensim.models import Word2Vec
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import json
import pandas as pd
import csv

q = open("questions.txt", "r")
d = open("dictionary.txt", "r")
questions = json.loads(q.read())
dictionary = json.loads(d.read())
data = []
for q in questions:
    data.append(q.split(" "))
w2v_model = Word2Vec.load("word2vec.model")
tfidf = TfidfVectorizer()
tfidf.fit_transform(questions)
tfidf_feat = tfidf.get_feature_names()
tfidf_sent_vectors = []# the tfidf-w2v for each sentence/review is stored in this list
row = 0
for sent in tqdm(data): # for each review/sentence 
  sent_vec = np.zeros(100) # as word vectors are of zero length
  weight_sum = 0 # num of words with a valid vector in the sentence/review
  for word in sent: # for each word in a review/sentence
    if word in tfidf_feat:
      try:
        vec = w2v_model.wv[word]
        #print(vec)
        tf_idf = dictionary[str(word)]*(sent.count(word)/len(sent))
        sent_vec+= (vec*tf_idf)
        weight_sum += tf_idf
      except Exception:
          a=0
#      else:
#          print("sure, it was defined.")
  if weight_sum !=0:
    sent_vec /= weight_sum 
  tfidf_sent_vectors.append(sent_vec)
  row+=1
  #print(sent_vec)
  print(len(tfidf_sent_vectors))
#  print(tfidf_sent_vectors)
# import pickle
# pickle.dump(tfidf_sent_vectors,open('/content/drive/My Drive/case study data/tfidf_sent_vectors_500','wb'))

data = pd.read_csv("Posts.csv")
data.sort_values("Title", inplace = True)
with open('Posts2.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Id','Title', 'Body', 'Tags', 'LastEditorDisplayName', 'Score', 'ViewCount', 'CreationDate', 'LastEditDate', 'corpus','vector'])
    for row in tqdm(range(len(data))):
        writer.writerow([ data['Id'][row], data['Title'][row], data['Body'][row], data['Tags'][row], data['LastEditorDisplayName'][row], data['Score'][row], data['ViewCount'][row], data['CreationDate'][row], data['LastEditDate'][row], questions[row], tfidf_sent_vectors[row]  ])
   