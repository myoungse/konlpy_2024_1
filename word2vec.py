from gensim.models import Word2Vec, keyedvectors

corpus_fname = "C:/Users/ekbin/w2v file/korquad_mecab.txt"
model_fname = "C:/Users/ekbin/w2v file/word2vec.txt"

corpus = [sent.strip().split(" ") for sent in open(corpus_fname, 'r', encoding="utf-8").readlines()]
model = Word2Vec(corpus, workers=4, sg=1)
model.wv.save_word2vec_format(model_fname)

loaded_model = keyedvectors.load_word2vec_format("C:/Users/ekbin/w2v file/word2vec.txt")
model_result = loaded_model.most_similar("힐머니")
print(model_result)
