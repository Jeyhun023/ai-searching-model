import mysql.connector
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec

cnx = mysql.connector.connect(
  host="searching.cngwmhdxghmd.us-east-2.rds.amazonaws.com",
  user="root",
  password="888ceyhun",
  database="abyss"
)
cursor = cnx.cursor()
add_record = ("INSERT INTO dictionary (word, word2vec, tfidf) VALUES (%s, %s, %s)")


q = open("questions.txt", "r")
d = open("dictionary.txt", "r")
questions = json.loads(q.read())
dictionary = json.loads(d.read())

tfidf = TfidfVectorizer()
tfidf.fit_transform(questions)

w2v_model = Word2Vec.load("word2vec.model")

for word in dictionary:
    try:
        vec = json.dumps(w2v_model.wv[word].tolist())
    except:
        vec = 0
    record = (word, vec, dictionary[word])
    cursor.execute(add_record, record)
    cnx.commit()

cursor.close()
cnx.close()
