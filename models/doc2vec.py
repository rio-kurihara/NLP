from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument


class Doc2VecModelCreater():
    def __init__(self, list_doc_split, list_ids):
        self.sentences = [item for item in list_doc_split]
        self.list_ids = list_ids
        assert len(self.sentences) == len(self.list_ids)

    def create_doc2vec_model(self, alpha=0.015, min_count=5, window=5,
                             size=100, itr=20, workers=4):
        train_corpus = [TaggedDocument(doc, [i])
                for doc, i in zip(self.sentences, self.list_ids)]

        model = Doc2Vec(alpha=alpha, min_count=min_count, seed=3455, window=window,
                        size=size, iter=itr, workers=workers)

        model.build_vocab(train_corpus)

        model.train(train_corpus, total_examples=model.corpus_count, epochs=10)
        return model
