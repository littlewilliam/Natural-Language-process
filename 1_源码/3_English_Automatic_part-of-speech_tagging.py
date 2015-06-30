# coding=utf-8
__author__ = 'tianchuang'

import nltk

# 英语的词类自动标注
# sent为原始语句，摘自NPR新闻网
sent = "NPR's Morning Edition host Steve Inskeep interviews President Obama at the White House on Monday." \
       "President Obama says it would be a \"fundamental misjudgment\" to condition a nuclear deal with Iran " \
       "on the country's recognition of Israel."
tokens = nltk.word_tokenize(sent)
pos_tags = nltk.pos_tag(tokens)

print "英语的词类自动标注结果为："
print pos_tags
