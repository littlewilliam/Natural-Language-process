# coding=utf-8
__author__ = 'tianchuang'

import collections
import nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews

# 英文文本分类（电影评论的正负面情感分析）

# 定义特征函数
def word_feats(words):
    return dict([(word, True) for word in words])

# 积极与消极的特征
neg_ids = movie_reviews.fileids('neg')
pos_ids = movie_reviews.fileids('pos')
neg_feats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in neg_ids]
pos_feats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in pos_ids]


# 样本数量节选
neg_cutoff = len(neg_feats) * 4 / 5
pos_cutoff = len(pos_feats) * 4 / 5
train_feats = neg_feats[:neg_cutoff] + pos_feats[:pos_cutoff]
test_feats = neg_feats[neg_cutoff:] + pos_feats[pos_cutoff:]
print '训练样本有：%d , 测试样本有：%d' % (len(train_feats), len(test_feats))


# 训练与测试
def train_and_test(train_feats, test_feats):
    classifier = NaiveBayesClassifier.train(train_feats)
    ref_sets = collections.defaultdict(set)
    test_sets = collections.defaultdict(set)

    for i, (feats, label) in enumerate(test_feats):
        ref_sets[label].add(i)
        observed = classifier.classify(feats)
        test_sets[observed].add(i)

    print '积极的 准确率:', nltk.metrics.precision(ref_sets['pos'], test_sets['pos'])
    print '积极的 召回率:', nltk.metrics.recall(ref_sets['pos'], test_sets['pos'])
    print '积极的 F-measure:', nltk.metrics.f_measure(ref_sets['pos'], test_sets['pos'])
    print '消极的 准确率:', nltk.metrics.precision(ref_sets['neg'], test_sets['neg'])
    print '消极的 召回率:', nltk.metrics.recall(ref_sets['neg'], test_sets['neg'])
    print '消极的 F-measure:', nltk.metrics.f_measure(ref_sets['neg'], test_sets['neg'])

    # 显示最有用的特征
    classifier.show_most_informative_features()


train_and_test(train_feats, test_feats)
