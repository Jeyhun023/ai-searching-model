import mysql.connector
import numpy as np
from tqdm import tqdm
import concurrent.futures
import json

cnx = mysql.connector.connect(
  host="searching.cngwmhdxghmd.us-east-2.rds.amazonaws.com",
  user="root",
  password="888ceyhun",
  database="abyss"
)
cursor = cnx.cursor()

query = ("SELECT id, word, w2vec, idf  FROM dictionary")
cursor.execute(query)

dictionary = {}
for (id, word, w2vec, idf) in cursor:
    dictionary[word] = {
        'w2vec': w2vec,
        'idf': idf
    }

query = ("SELECT id, post_id, corpus1, corpus2, tags, vector  FROM corpus")
cursor.execute(query)

corpus_array = []
for (id, post_id, corpus1, corpus2, tags, vector) in cursor:
    corpus_array.append(corpus1.split(" ")) 

def get_idf(word):
    return float(dictionary[word]['idf'])

def get_word2vec(word):
    w2vec = json.loads(dictionary[word]['w2vec'])
    return np.array(w2vec)



# For each sentence
def vectorize(sent):
    def get_tf(word):
        return sent.count(word) / len(sent)

    tf = list(map(get_tf, sent))
    # print(tf)
    tf_diag = np.diagflat(tf)
    # print(tf_diag)
    idf = list(map(get_idf, sent))
    idf_diag = np.diagflat(idf)
    tf_idf_diag = np.matmul(tf_diag, idf_diag)
    # print(tf_idf_diag)

    # Calculate tf_diag and idf
    tf_diag_idf = np.matmul(tf_diag, idf_diag)
    tf_diag_idf = np.diag(tf_diag_idf)
    tf_diag_idf = np.float_power(tf_diag_idf, -1)
    tf_diag_idf = np.diagflat(tf_diag_idf)
    tf_diag_idf = np.sum(tf_diag_idf)

    # Word2vec vector
    word_vec = list(map(get_word2vec, sent))
    wordvec_tf_idf = sum(np.matmul(tf_idf_diag, word_vec))

    # Calculate final result
    tf_diag_idf_wordvec_tf_idf = np.multiply(tf_diag_idf, wordvec_tf_idf)

    return tf_diag_idf_wordvec_tf_idf

with concurrent.futures.ThreadPoolExecutor() as executor:
    finals = list(tqdm(executor.map(vectorize, corpus_array)))
    # results
    for index, final in enumerate(finals):
        final = json.dumps(final.tolist())
        update_record = ("UPDATE corpus SET vector = %s WHERE id = %s")
        cursor.execute(update_record, (final, index + 1))
        cnx.commit() 
