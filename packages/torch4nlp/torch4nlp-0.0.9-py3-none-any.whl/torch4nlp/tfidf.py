# 2022-11-23
import math
import torch


class TFIDF:
    def __init__(self, corpus, stop_words=None):
        """
        corpus(List[List[str]]): list of segmented sentences
        stop_words(iterable): stop words
        """
        
        self.word2idf = self._get_word2idf(corpus, stop_words)
        self.corpus_vec = torch.FloatTensor([self._get_tfidf_vec(x) for x in corpus])
    
    def _get_word2idf(self, corpus, stop_words):
        if stop_words is None:
            stop_words = set()
        else:
            stop_words = set(stop_words)

        num_doc = len(corpus)

        word2num_doc_covered = {}  # word -> number of doc that cover the word
        for doc in corpus:
            uniq_words_in_cur_doc = set(doc)
            for word in uniq_words_in_cur_doc:
                word2num_doc_covered[word] = word2num_doc_covered.get(word, 0) + 1

        word2idf = {}
        for word, freq in word2num_doc_covered.items():
            assert freq > 0, f'{word} not existed in any doc'
            if word not in stop_words:
                word2idf[word] = math.log(num_doc / freq)
        
        return word2idf
    
    def _get_tfidf_vec(self, word_list):
        if not word_list:
            return [0]*len(self.word2idf)

        word2tf = {}
        for word in word_list:
            word2tf[word] = word2tf.get(word, 0) + 1
        for k in word2tf:
            word2tf[k] = word2tf[k] / len(word_list)
        
        result_vec = []
        for word, idf in self.word2idf.items():
            if word in word2tf:
                result_vec.append(word2tf[word] * idf)
            else:
                result_vec.append(0)
        
        return result_vec

    def get_top_doc(self, segment_sentence, distance_method='cosine_sim', topk=1):
        """get the top doc by similarity
        """

        cur_vec = self.get_tfidf_vec(segment_sentence)
        cur_vec = torch.FloatTensor([cur_vec])
        if distance_method == 'cosine_sim':
            scores = torch.nn.functional.cosine_similarity(cur_vec, self.corpus_vec)
        
        sorted_scores, indices = torch.sort(scores, descending=True)
        return indices[:topk], sorted_scores[:topk]