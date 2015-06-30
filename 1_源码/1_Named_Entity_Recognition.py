# coding=utf-8
__author__ = 'tianchuang'

import nltk


# 英文命名实体识别
# sent为原始语句，摘自NPR新闻网
sent = "NPR's Morning Edition host Steve Inskeep interviews President Obama at the White House on Monday." \
       "President Obama says it would be a \"fundamental misjudgment\" to condition a nuclear deal with Iran " \
       "on the country's recognition of Israel."
tokens = nltk.word_tokenize(sent)
pos_tags = nltk.pos_tag(tokens)
sent_final = pos_tags


def English_NER(sentence):
    # 命名实体只被标注为NE
    print '命名实体只被标注为NE:'
    print nltk.ne_chunk(sentence, binary=True)

    # 命名实体会添加类型标签，例如PERSON，ORGANIZATION，GPE等
    print '命名实体会添加类型标签，例如PERSON，ORGANIZATION，GPE等:'
    print nltk.ne_chunk(sentence)


English_NER(sent_final)
