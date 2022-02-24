from bs4 import BeautifulSoup
import re
from tqdm import tqdm
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
from sklearn.feature_extraction.text import TfidfVectorizer
import mysql.connector

print("import finished")

cnx = mysql.connector.connect(
  host="searching.cngwmhdxghmd.us-east-2.rds.amazonaws.com",
  user="root",
  password="888ceyhun",
  database="abyss"
)
cursor = cnx.cursor()

print("connected database")

def striphtml(data):
    soup = BeautifulSoup(data, 'lxml')
    cleantext = soup.get_text()
    soup1 = BeautifulSoup(cleantext, 'html5lib')
    cleantext = soup1.get_text()
    cleantext = re.sub('<.*?>', ' ', str(cleantext))  
    cleantext = re.sub('\\n', ' ', str(cleantext))  
    cleantext=re.sub('\sdiv\s', ' ', str(cleantext), flags=re.MULTILINE|re.DOTALL)
    return cleantext
  
def reprocess1(data):
    title, body = data['title'], data['content']
    #Keeping the code content
    question = re.sub('<code>(.*?)</code>', '', body, flags=re.MULTILINE|re.DOTALL)
    question = striphtml(question.encode('utf-8'))
    question=str(title)+" "+str(question)
    question=re.sub(r'[^A-Za-z]+',' ',question)
    words= word_tokenize(str(question.lower()))
    #Removing all single letter and and stopwords from question except for the letter 'c'
    stemmer = SnowballStemmer("english")
    question=' '.join(str(stemmer.stem(j)) for j in words if j not in stopwords.words('english') and (len(j)!=1 or j=='c'))
    return question
  
def reprocess2(data):
    title, body, answers = data['title'], data['content'], data['answers']
    #Keeping the code content
    question = re.sub('<code>(.*?)</code>', '', body, flags=re.MULTILINE|re.DOTALL)
    question = striphtml(question.encode('utf-8'))
    question=str(title)+" "+str(question)+" "+str(answers)
    question=re.sub(r'[^A-Za-z]+',' ',question)
    words= word_tokenize(str(question.lower()))
    #Removing all single letter and and stopwords from question except for the letter 'c'
    stemmer = SnowballStemmer("english")
    question=' '.join(str(stemmer.stem(j)) for j in words if j not in stopwords.words('english') and (len(j)!=1 or j=='c'))
    return question

for a in range(0, 50000, 1000):
  query = ("SELECT id, title, content, tags, answers  FROM posts WHERE id BETWEEN {} AND {}".format(a, a + 999))
  cursor.execute(query)

  print("start preprocess")

  corpus1 = []
  corpus2 = []
  questions = []
  for (id, title, content, tags, answers) in tqdm(cursor):
    data = {
      "id" : id,
      "title" : title,
      "content" : content,
      "tags" : tags,
      "answers" : answers
    }
    questions.append(data)
    corpus1.append(reprocess1(data))
    corpus2.append(reprocess2(data))

  x=0
  data = []
  for question in questions:
    data.append((question['id'], corpus1[x], corpus2[x], question['tags']))
    x = x + 1
    
  add_record = ("INSERT INTO corpus "
    "(post_id, corpus1, corpus2, tags) "
    "VALUES (%s, %s, %s, %s)") 
  cursor.executemany(add_record, data)
  cnx.commit() 
  
cursor.close()
cnx.close()