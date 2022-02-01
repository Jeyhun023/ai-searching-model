from nltk.tokenize import word_tokenize
import re
import numpy as np
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from gensim.models import Word2Vec
from sklearn.feature_extraction.text import TfidfVectorizer

question = input("Enter your query: ")
question=re.sub(r'[^A-Za-z]+',' ',question)
words= word_tokenize(str(question.lower()))

stemmer = SnowballStemmer("english")
question=' '.join(str(stemmer.stem(j)) for j in words if j not in stopwords.words('english') and (len(j)!=1 or j=='c'))

tfidf = TfidfVectorizer()
tfidf.fit_transform([question])
dictionary = dict(zip(tfidf.get_feature_names(),tfidf.idf_))

data = []
data.append(question.split(" "))

w2v_model = Word2Vec.load("word2vec.model")
tfidf_feat = tfidf.get_feature_names()
tfidf_sent_vectors = []# the tfidf-w2v for each sentence/review is stored in this list
row = 0 

for sent in data: # for each review/sentence 
  sent_vec = np.zeros(100) # as word vectors are of zero length
  weight_sum = 0 # num of words with a valid vector in the sentence/review
  for word in sent: # for each word in a review/sentence
    if word in tfidf_feat:
      try:
        vec = w2v_model.wv[word]
        tf_idf = dictionary[str(word)]*(sent.count(word)/len(sent))
        sent_vec+= (vec*tf_idf)
        weight_sum += tf_idf
      except Exception:
          a=0
  if weight_sum !=0:
    sent_vec /= weight_sum 
  tfidf_sent_vectors.append(sent_vec)
  row+=1

print(tfidf_sent_vectors[0])

     
