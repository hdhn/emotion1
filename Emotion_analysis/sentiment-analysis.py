
# coding: utf-8

# In[ ]:



#! /usr/bin/env python2.7
#coding=utf-8

import pickle
import textprocessing as tp
import numpy as np
#载入情感词典
posdict = pickle.load(open('D:/code/sentiment_test/sentiment_dictionary/posdict.pkl', 'r'))
negdict = pickle.load(open('D:/code/sentiment_test/sentiment_dictionary/negdict.pkl', 'r'))
mostdict = pickle.load(open('D:/code/sentiment_test/sentiment_dictionary/mostdict.pkl', 'r'))
verydict = pickle.load(open('D:/code/sentiment_test/sentiment_dictionary/verydict.pkl', 'r'))
moredict = pickle.load(open('D:/code/sentiment_test/sentiment_dictionary/moredict.pkl', 'r'))
ishdict = pickle.load(open('D:/code/sentiment_test/sentiment_dictionary/ishdict.pkl', 'r'))
insufficientdict = pickle.load(open('D:/code/sentiment_test/sentiment_dictionary/insufficentdict.pkl', 'r'))
inversedict = pickle.load(open('D:/code/sentiment_test/sentiment_dictionary/inversedict.pkl', 'r'))
#载入评论数据。

review = pickle.load(open('D:/code/review_set/review_pkl/Motorala.pkl', 'r'))
# 定义判断基数偶数的函数。在判断否定词时使用。
def judgeodd(num):
    if (num/2)*2 == num:
        return 'even'
    else:
        return 'odd'
        
#情感分值计算主程序。

def sentiment_score_list(dataset):
    cuted_data = []
    for cell in dataset:
        cuted_data.append(tp.cut_sentence(cell))

count1 = []
count2 = []
for sents in cuted_data: #循环遍历每一个评论
    for sent in sents: #循环遍历评论中的每一个分句
        segtmp = tp.segmentation(sent, 'list') #把句子进行分词，以列表的形式返回
        i = 0 #记录扫描到的词的位置
        a = 0 #记录情感词的位置
        poscount = 0 #积极词的第一次分值
        poscount2 = 0 #积极词反转后的分值
        poscount3 = 0 #积极词的最后分值（包括叹号的分值）
        negcount = 0#消极词的第一次分值
        negcount2 = 0
        negcount3 = 0#消极词的最后分值（包括叹号的分值）
for word in segtmp:
    if word in posdict: #判断词语是否是情感词
        poscount + = 1
        c = 0
for w in segtmp[a:i]: #扫描情感词前的程度词
    if w in mostdict:
        poscount * = 4.0
    elif w in verydict:
        poscount * = 3.0
    elif w in moredict:
        poscount * = 2.0
    elif w in ishdict:
        poscount / = 2.0
    elif w in insufficientdict:
        poscount / = 4.0
    elif w in inversedict:
            c + = 1
if judgeodd(c) == 'odd': #扫描情感词前的否定词数
    poscount * = -1.0
    poscount2 + = poscount
    poscount = 0
    poscount3 = poscount + poscount2 + poscount3
    poscount2 = 0
else:
    poscount3 = poscount + poscount2 + poscount3
    poscount = 0
a = i + 1 #情感词的位置变化
elif word in negdict: #消极情感的分析，与上面一致
    negcount + = 1
    d = 0
for w in segtmp[a:i]:
    if w in mostdict:
        negcount * = 4.0
    elif w in verydict:
        negcount * = 3.0
    elif w in moredict:
        negcount * = 2.0
    elif w in ishdict:
        negcount / = 2.0
    elif w in insufficientdict:
        negcount / = 4.0
    elif w in inversedict:
        d + = 1
if judgeodd(d) == 'odd':
    negcount * = -1.0
    negcount2 + = negcount
    negcount = 0
    negcount3 = negcount + negcount2 + negcount3
    negcount2 = 0
else:
    negcount3 = negcount + negcount2 + negcount3
    negcount = 0
a = i + 1
elif word == '！'.decode('utf8') or word == '!'.decode('utf8'): ##判断句子是否有感叹号
    for w2 in segtmp[::-1]: #扫描感叹号前的情感词，发现后权值+2，然后退出循环
        if w2 in posdict or negdict:
            poscount3 + = 2
            negcount3 + = 2
            break
            i += 1 #扫描词位置前移

 

#以下是防止出现负数的情况
pos_count = 0
neg_count = 0
if poscount3 < 0 and negcount3 > 0:
    neg_count += negcount3 - poscount3
    pos_count = 0
elif negcount3 < 0 and poscount3 > 0:
    pos_count = poscount3 - negcount3
    neg_count = 0
elif poscount3 < 0 and negcount3 < 0:
    neg_count = - poscount3
    pos_count = - negcount3
else:
    pos_count = poscount3
    neg_count = negcount3

count1.append([pos_count, neg_count])
count2.append(count1)
count1 = []

return count2
#计算出所需的积极情感值，消极情感值，积极情感均值，消极情感均值，积极情感方差，消极情感方差。

def sentiment_score(senti_score_list):
    score = []
for review in senti_score_list:
    score_array = np.array(review)
    Pos = np.sum(score_array[:,0])
    Neg = np.sum(score_array[:,1])
    AvgPos = np.mean(score_array[:,0])
    AvgNeg = np.mean(score_array[:,1])
    StdPos = np.std(score_array[:,0])
    StdNeg = np.std(score_array[:,1])
    score.append([Pos, Neg, AvgPos, AvgNeg, StdPos, StdNeg])
    return score
print(score)
