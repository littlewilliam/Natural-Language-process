# coding=utf-8
__author__ = 'tianchuang'

import jieba

# 汉语自动分词
# sent为原始语句，摘自网易新闻
sent = '各方瞩目的国共两党领导人“习朱会”上午10点30分在北京人民大会堂举行，进行一个小时会谈后。' \
       '朱立伦举行记者会说明“习朱会”进行过程。'

# 精确模式
tokens = jieba.cut(sent, cut_all=False)
print '精确模式:'
print("| ".join(tokens))

# 全模式
tokens = jieba.cut(sent, cut_all=True)
print '全模式:'
print("| ".join(tokens))
