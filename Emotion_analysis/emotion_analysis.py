import sklearn
from nltk.classify.scikitlearn import  SklearnClassifier
from sklearn.svm import SVC, LinearSVC,  NuSVC
from sklearn.naive_bayes import  MultinomialNB, BernoulliNB
from sklearn.linear_model import  LogisticRegression
from sklearn.metrics import  accuracy_score
import nltk
from nltk.collocations import  BigramCollocationFinder
from nltk.metrics import  BigramAssocMeasures
import jieba
from random import shuffle

def text():
    f1 = open('E:/工作文件/情感分析案例1/good.txt', 'r', encoding='utf-8')
    f2 = open('E:/工作文件/情感分析案例1/bad.txt', 'r', encoding='utf-8')
    line1 = f1.readline()
    line2 = f2.readline()
    str = ''
    while line1:
        str += line1
        line1 = f1.readline()
    while line2:
        str += line2
        line2 = f2.readline()
    f1.close()
    f2.close()
    return str


def bag_of_words(words):
    return dict([(word, True) for word in words])


def bigram(words, score_fn=BigramAssocMeasures.chi_sq, n=1000):
    bigram_finder = BigramCollocationFinder.from_words(words)  # 把文本变成双词搭配的形式
    bigrams = bigram_finder.nbest(score_fn, n)  # 使用卡方统计的方法，选择排名前1000的双词
    newBigrams = [u + v for (u, v) in bigrams]
    return bag_of_words(newBigrams)


def bigram_words(words, score_fn=BigramAssocMeasures.chi_sq, n=1000):
    bigram_finder = BigramCollocationFinder.from_words(words)
    bigrams = bigram_finder.nbest(score_fn, n)
    newBigrams = [u + v for (u, v) in bigrams]
    a = bag_of_words(words)
    b = bag_of_words(newBigrams)
    a.update(b)  # 把字典b合并到字典a中
    return a


print(bigram_words(text(), score_fn=BigramAssocMeasures.chi_sq, n=1000))


def read_file(filename):
     stop = [line.strip() for line in  open('E:/工作文件/情感分析案例1/stop.txt','r',encoding='utf-8').readlines()]  #停用词
     f = open(filename,'r',encoding='utf-8')
     line = f.readline()
     str = []
     while line:
         s = line.split('\t')
         fenci = jieba.cut(s[0],cut_all=False)  #False默认值：精准模式
         str.append(list(set(fenci)-set(stop)))
         line = f.readline()
     return str


def jieba_feature(number):
    posWords = []
    negWords = []
    for items in read_file('E:/工作文件/情感分析案例1/good.txt'):  # 把集合的集合变成集合
        for item in items:
            posWords.append(item)
    for items in read_file('E:/工作文件/情感分析案例1/bad.txt'):
        for item in items:
            negWords.append(item)

    word_fd = FreqDist()  # 可统计所有词的词频
    cond_word_fd = ConditionalFreqDist()  # 可统计积极文本中的词频和消极文本中的词频

    for word in posWords:
        word_fd[word] += 1
        cond_word_fd['pos'][word] += 1

    for word in negWords:
        word_fd[word] += 1
        cond_word_fd['neg'][word] += 1

    pos_word_count = cond_word_fd['pos'].N()  # 积极词的数量
    neg_word_count = cond_word_fd['neg'].N()  # 消极词的数量
    total_word_count = pos_word_count + neg_word_count

    word_scores = {}  # 包括了每个词和这个词的信息量

    for word, freq in word_fd.items():
        pos_score = BigramAssocMeasures.chi_sq(cond_word_fd['pos'][word], (freq, pos_word_count),
                                               total_word_count)  # 计算积极词的卡方统计量，这里也可以计算互信息等其它统计量
        neg_score = BigramAssocMeasures.chi_sq(cond_word_fd['neg'][word], (freq, neg_word_count), total_word_count)
        word_scores[word] = pos_score + neg_score  # 一个词的信息量等于积极卡方统计量加上消极卡方统计量

    best_vals = sorted(word_scores.items(), key=lambda item: item[1], reverse=True)[
                :number]  # 把词按信息量倒序排序。number是特征的维度，是可以不断调整直至最优的
    best_words = set([w for w, s in best_vals])
    return dict([(word, True) for word in best_words])


def build_features():
    # feature = bag_of_words(text())#第一种：单个词
    # feature = bigram(text(),score_fn=BigramAssocMeasures.chi_sq,n=500)#第二种：双词
    # feature =  bigram_words(text(),score_fn=BigramAssocMeasures.chi_sq,n=500)#第三种：单个词和双个词
    feature = jieba_feature(300)  # 第四种：结巴分词

    posFeatures = []
    for items in read_file('E:/工作文件/情感分析案例1/good.txt'):
        a = {}
        for item in items:
            if item in feature.keys():
                a[item] = 'True'
        posWords = [a, 'pos']  # 为积极文本赋予"pos"
        posFeatures.append(posWords)
    negFeatures = []
    for items in read_file('E:/工作文件/情感分析案例1/bad.txt'):
        a = {}
        for item in items:
            if item in feature.keys():
                a[item] = 'True'
        negWords = [a, 'neg']  # 为消极文本赋予"neg"
        negFeatures.append(negWords)
    return posFeatures, negFeatures

posFeatures,negFeatures =  build_features()

shuffle(posFeatures)
shuffle(negFeatures) #把文本的排列随机化
train =  posFeatures[300:]+negFeatures[300:]#训练集(70%)
test = posFeatures[:300]+negFeatures[:300]#验证集(30%)
data,tag = zip(*test)#分离测试集合的数据和标签，便于验证和测试


def score(classifier):
    classifier = SklearnClassifier(classifier)
    classifier.train(train)  # 训练分类器
    pred = classifier.classify_many(data)  # 给出预测的标签
    n = 0
    s = len(pred)
    for i in range(0, s):
        if pred[i] == tag[i]:
            n = n + 1
    return n / s  # 分类器准确度

print('BernoulliNB`s accuracy is %f'  %score(BernoulliNB()))
print('MultinomiaNB`s accuracy is %f'  %score(MultinomialNB()))
print('LogisticRegression`s accuracy is  %f' %score(LogisticRegression()))
print('SVC`s accuracy is %f'  %score(SVC()))
print('LinearSVC`s accuracy is %f'  %score(LinearSVC()))
print('NuSVC`s accuracy is %f'  %score(NuSVC()))