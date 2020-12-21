# -*- coding: utf-8 -*-
"""

@author: Ccccandy

"""


import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers, optimizers,losses
import jieba
import re

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'


batchsz = 32 # 批量大小
max_review_len = 30 # 每个句子词语量
embedding_len = 300 # 词向量长度
epochs = 2 # 训练次数
hiddenSizes=[128,64]
drop=0.5

# 分词 
# in：可for循环的数据集，如['a','b',……]
# out：[[a,],[b,],……]
def fenci(batch):    
    fc=[]      # 建立列表，存储每条数据的分词结果
    for i in batch:
        i=str(i)    # 将数据转化为字符串格式
        i=re.sub(r'//@.*?:', '',i)   # 处理转发
        i=re.sub(r'http://(\w|\.)+(/\w+)*', '',i)   #处理超链接
        cut = jieba.cut(i)
        cut_list = [ i for i in cut ]
        cut=stop(cut_list)
        fc.append(cut)  
    return fc

# 引用停词文档
def stopwordslist():
    stopwords = [line.strip() for line in open('data/stopword1.txt',encoding='UTF-8').readlines()]
    return stopwords

# 过滤停词文档
def stop(each):    
    stopword=stopwordslist()    # 获取停词文档
    new=[]              # 建立列表，存储过滤后的分词结果
    for i in each:
        if i not in stopword:
            new.append(i)
    return new

# in：分词列表
# out：分词转换为的数字列表
def w2n(each,index_dict):    
    return ([index_dict.get(i, 0) for i in each]) 

# 获取词向量层的权重
def get_data(index_dict,word_vectors,num_words):
    embedding_weights = np.zeros((num_words, 300))
    for word, index in index_dict.items():
        embedding_weights[index, :] = word_vectors[word]        
    return embedding_weights

# 加载数据 
def load():
    # 加载数据
    print('开始加载数据ing')
    train = pd.read_excel('data/virus_train.xlsx', usecols = [1,2],nrows=200,encoding='utf-8')  # 读取excel文件
    print('加载完毕')    
    a=train.values.tolist()  # 转换为列表形式    
    x=[]
    y=[]
    for i in a:
        x.append(i[0])
        if i[1]=='happy':
            y.append(0)
        elif i[1]=='sad':
            y.append(1)
        elif i[1]=='surprise':
            y.append(2)
        elif i[1]=='fear':
            y.append(3)
        elif i[1]=='angry':
           y.append(4)
        elif i[1]=='neural':
            y.append(5)
    y=tf.one_hot(y,6)
    print('x、y拆分完毕')
    return x,y

# 数据预处理    
def process(x,y,index_dict):
    data_len=len(y)
    t_data_len=data_len//5*4
    # 分词
    print('开始分词，转化为数字ing')
    fens=fenci(x)
    xx=[w2n(i,index_dict) for i in fens]
    print('分词完毕')    
    # 截断和填充句子，使得等长，此处长句子保留句子后面的部分，短句子在后面填充
    print('拆分训练集和测试集ing')
    x_train = keras.preprocessing.sequence.pad_sequences(xx[:t_data_len], maxlen=max_review_len,padding='post')
    x_test = keras.preprocessing.sequence.pad_sequences(xx[t_data_len:], maxlen=max_review_len,padding='post')
    y_train = tf.constant(y[:t_data_len])
    y_test = tf.constant(y[t_data_len:])
    print('拆分完毕')
    # 构建数据集，打散，批量，并丢掉最后一个不够 batchsz 的 batch
    print('合并x和ying')
    db_train = tf.data.Dataset.from_tensor_slices((x_train, y_train))
    db_train = db_train.shuffle(1000).batch(batchsz, drop_remainder=True)  # 不足一个batch抛弃
    db_test = tf.data.Dataset.from_tensor_slices((x_test, y_test))
    db_test = db_test.batch(batchsz, drop_remainder=True)
    print('合并完毕')
    # 统计数据集属性
    print('x_train shape:', x_train.shape)    
    return db_train,db_test

# 加载词典，获取词典数量和词典矩阵
def get_dict():    
    # 载入词典
    print('开始加载词典ing')
    index_dict=np.load('other/w2n_dic.npy').item()   
    word_vectors=np.load('other/w2v_dic.npy').item()   
    print('加载完毕')
    # 加载词向量矩阵
    print('开始加载词向量ing')
    num_words = len(word_vectors)+1
    embedding_matrix=get_data(index_dict,word_vectors,num_words)
    print('加载完毕')
    return num_words,embedding_matrix,index_dict


class RnnAttentionLayer(layers.Layer):
    def __init__(self, attention_size, drop_rate):
         super().__init__()
         self.attention_size = attention_size
         self.dropout = layers.Dropout(drop_rate)

    def build(self, input_shape):
        self.attention_w = self.add_weight(name = "atten_w", shape = (input_shape[-1], self.attention_size), initializer = tf.random_uniform_initializer(), dtype = "float32", trainable = True)
        self.attention_u = self.add_weight(name = "atten_u", shape = (self.attention_size,), initializer = tf.random_uniform_initializer(), dtype = "float32", trainable = True)
        self.attention_b = self.add_weight(name = "atten_b", shape = (self.attention_size,), initializer = tf.constant_initializer(0.1), dtype = "float32", trainable = True)    
        super().build(input_shape)

    def call(self, inputs, training):
        x = tf.tanh(tf.add(tf.tensordot(inputs, self.attention_w, axes = 1), self.attention_b))
        x = tf.tensordot(x, self.attention_u, axes = 1)
        x = tf.nn.softmax(x)
        weight_out = tf.multiply(tf.expand_dims(x, -1), inputs)
        final_out = tf.reduce_sum(weight_out, axis = 1) 
        drop_out = self.dropout(final_out, training = training)
        return drop_out

class RnnLayer(layers.Layer):
    def __init__(self, rnn_size, drop_rate):
        super().__init__()
        fwd_lstm = layers.LSTM(rnn_size, return_sequences = True, go_backwards= False, dropout = drop_rate, name = "fwd_lstm")
        bwd_lstm = layers.LSTM(rnn_size, return_sequences = True, go_backwards = True, dropout = drop_rate, name = "bwd_lstm")
        self.bilstm = layers.Bidirectional(merge_mode = "concat", layer = fwd_lstm, backward_layer = bwd_lstm, name = "bilstm")

    def call(self, inputs, training):
        outputs = self.bilstm(inputs, training = training)
        return outputs



# 构建模型
class BiLSTMAttention(tf.keras.Model):
    """
    Text CNN 用于文本分类
    """
    def __init__(self):
        super(BiLSTMAttention, self).__init__()
        
        self.embedding = layers.Embedding(num_words, embedding_len,input_length=max_review_len,trainable=True)#不参与梯度更新
        self.embedding.build(input_shape=(None, max_review_len))
        self.embedding.set_weights([embedding_matrix])       
        self.rnn_layer1 = RnnLayer(hiddenSizes[1], drop)
        self.attention_layer = RnnAttentionLayer(hiddenSizes[-1], drop)      
        self.f=layers.Flatten() # 打平层，方便全连接层处理
        self.out1=layers.Dense(64, activation='relu')
        self.out2=layers.Dense(16, activation='relu') 
        self.outlayer=layers.Dense(6, activation='softmax') 
  
    def call(self, inputs, training=None):
        x = inputs 
        #print(x.shape)
        x = self.embedding(x)
        #print(x.shape)        
        x = self.rnn_layer1(x,training = training)
        #print(x.shape)
        x = self.attention_layer(x,training = training)
        #print(x.shape)
        x = self.f(x)
        #print(x.shape)
        x = self.out1(x)
        #print(x.shape)
        x = self.out2(x)
        #print(x.shape)
        x = self.outlayer(x)
        #print(x.shape)
        prob = tf.sigmoid(x)
        return prob

    
if __name__ == '__main__':

    
    # 加载数据 
    x,y=load()
    num_words,embedding_matrix,index_dict=get_dict()  
    db_train,db_test=process(x,y,index_dict) 
    
    # 创建模型
    model = BiLSTMAttention() 

    # 装配    
    model.compile(optimizer = optimizers.Adam(0.001),
                  loss = losses.CategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'],
                  experimental_run_tf_function=False)
    # 训练和验证
    model.fit(db_train, epochs=epochs, validation_data=db_test)
    # 测试
    a=model.evaluate(db_test)
    print("Final test loss and accuracy :", a)
    
    # 保存前需要模型的compile，不然会保存失败
    tf.saved_model.save(model, 'model/att')
    
    correct, total = 0,0
    
    for x,y in db_test: # 遍历所有测试集样本

        out = model(x)
        out = tf.argmax(out,1)
        out=tf.cast(out,tf.int32)
        y = tf.argmax(y, 1)
        y=tf.cast(y,tf.int32)
        # 统计预测正确数量
        correct += float(tf.reduce_sum(tf.cast(tf.equal(out, y),tf.float32)))
        # 统计预测样本总数
        total += x.shape[0] # 计算准确率
    print('test acc:', correct/total)


























