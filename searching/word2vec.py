from gensim.models import Word2Vec
from scipy import spatial
import json
q = open("questions.txt", "r")
d = open("dictionary.txt", "r")
questions = json.loads(q.read())
dictionary = json.loads(d.read())

# print(len(dictionary))
#print(dictionary)
data = []
for q in questions:
    data.append(q.split(" "))
#print(data)
#from gensim.test.utils import common_texts
model = Word2Vec(sentences=data, vector_size=100, window=2, min_count=10, workers=2, sg=0)
model.save("word2vec.model")
#print(common_texts)
model = Word2Vec.load("word2vec.model")
vector = model.wv['java']  # get numpy vector of a word
sims = model.wv.most_similar('java', topn=20)  # get other similar words
print(sims)
#print(vector)