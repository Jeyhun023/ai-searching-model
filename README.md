1. Sentence Transformers: Multilingual Sentence, Paragraph, and Image Embeddings using BERT & Co.

This framework provides an easy method to compute dense vector representations for sentences, paragraphs, and images. The models are based on transformer networks like BERT / RoBERTa / XLM-RoBERTa etc. and achieve state-of-the-art performance in various task. Text is embedding in vector space such that similar text is close and can efficiently be found using cosine similarity.

2. Installation

I recommend Python 3.6 or higher, PyTorch 1.6.0 or higher and transformers v4.6.0 or higher. The code does not work with Python 2.7.

Install the sentence-transformers with pip:

pip install -U sentence-transformers

Install from sources

Alternatively, you can also clone the latest version from the repository and install it directly from the source code:

pip install -e .

If you want to use a GPU / CUDA, you must install PyTorch with the matching CUDA Version. Follow PyTorch - Get Started for further details how to install PyTorch.

3. Pre-Trained Models

This repo provide a large list of Pretrained Models for more than 100 languages. Some models are general purpose models, while others produce embeddings for specific use cases. Pre-trained models can be loaded by just passing the model name: SentenceTransformer('model_name').

4. Usage
```
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = ['This framework generates embeddings for each input sentence',
    'Sentences are passed as a list of string.', 
    'The quick brown fox jumps over the lazy dog.']
sentence_embeddings = model.encode(sentences)

for sentence, embedding in zip(sentences, sentence_embeddings):
    print("Sentence:", sentence)
    print("Embedding:", embedding)
    print("")
    ```
