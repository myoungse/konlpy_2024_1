# word2vec 과제 코드

gensim 모델에서 word2vec과 keyedvectors를 불러줌.

    from gensim.models import Word2Vec, keyedvectors

코퍼스와 모델의 파일 경로를 적어줌.

    corpus_fname = "C:/Users/ekbin/w2v file/korquad_mecab.txt"
    model_fname = "C:/Users/ekbin/w2v file/word2vec.txt"

파일을 읽도록 하고 'r', strip을 이용해서 공백을 없애준 후 split 문자열을 나눠주게 함.

    corpus = [sent.strip().split(" ") for sent in open(corpus_fname, 'r', encoding="utf-8").readlines()]

workers는 gpu의 개수, sg는 skip-gram의 모델을 나타낸다고 함.

    model = Word2Vec(corpus, workers=4, sg=1)
    model.wv.save_word2vec_format(model_fname)

keyedvectors.load_word2vec_format는 word2vec의 메서드라고 함. 이 메서드의 역할은 저장된 word2vec의 model 파일을 loaded해준다.

    loaded_model = keyedvectors.load_word2vec_format("C:/Users/ekbin/w2v file/word2vec.txt")

"할머니"와 비슷한 단어를 model_result로 내게 한다.
    
    model_result = loaded_model.most_similar("할머니")
    
결과를 print 시킨다.

    print(model_result)


---
이상하게 단어를 오타없이 제대로 입력하면 결과가 잘 나오는데 왜 오타를 입력했을 때 안 나오는지 아직 잘 모르겠다.
오류가 여러 개 뜨는데 word2vec에 입력한 코드가 아니라 내부의 다른 코드에서
