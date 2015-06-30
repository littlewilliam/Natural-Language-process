# coding=utf-8
__author__ = 'tianchuang'

import jieba.posseg as pseg

# 汉语的词类自动标注
# sent为原始语句，摘自网易新闻
sent = '各方瞩目的国共两党领导人“习朱会”上午10点30分在北京人民大会堂举行，进行一个小时会谈后。' \
       '朱立伦举行记者会说明“习朱会”进行过程。'

words = pseg.cut(sent)

L = []
for w in words:
    word = w.word
    flag = w.flag
    L.append((w.word, w.flag))

# list unicode转中文显示
L_str = str(L).replace('u\'', '\'')
L_str = L_str.decode("unicode-escape")

print "汉语的词类自动标注结果为："
print L_str


