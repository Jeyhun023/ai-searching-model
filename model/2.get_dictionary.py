import mysql.connector
from gensim.models import Word2Vec
from sklearn.feature_extraction.text import TfidfVectorizer
from tqdm import tqdm
import json
import numpy as np

cnx = mysql.connector.connect(
  host="searching.cngwmhdxghmd.us-east-2.rds.amazonaws.com",
  user="root",
  password="888ceyhun",
  database="abyss"
)
cursor = cnx.cursor()

query = ("SELECT id, post_id, corpus1, corpus2, vector  FROM corpus")
cursor.execute(query)

splited_corpuses = []
corpuses = []
for (id, post_id, corpus1, corpus2, vector) in cursor:
    splited_corpuses.append(corpus2.split(" "))
    corpuses.append(corpus2)

tfidf = TfidfVectorizer(token_pattern='(?u)\\b\\w+\\b')
tfidf.fit_transform(corpuses)
dictionary = dict(zip(tfidf.get_feature_names_out(),tfidf.idf_))

print(len(dictionary))

model = Word2Vec(sentences=splited_corpuses, vector_size=100, window=2, min_count=2, workers=2, sg=0) 
model.save("word2vec.model")
model = Word2Vec.load("word2vec.model")

add_record = ("INSERT INTO dictionary (word, w2vec, idf) VALUES (%s, %s, %s)") 

for word in tqdm(dictionary):
    try:
        w2vec = json.dumps(model.wv[word].tolist())
    except:
        w2vec = json.dumps(np.zeros(100).tolist())
        
    data = (word, w2vec, dictionary[word])
    
    try:
        cursor.execute(add_record, data)
        cnx.commit() 
    except:
        print("Error")
    
cursor.close()
cnx.close()