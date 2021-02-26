import tensorflow as tf
import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt

print('Tensorflow Version :{}'.format(tf.__version__))
data = pd.DataFrame(np.random.exponential(,(100,5)))
print(data)
x = data.iloc[:,1:-1]
y = data.iloc[:,-1]
model = tf.keras.Sequential([tf.keras.layers.Dense(10,input_shape=(3,),activation='relu'),
                             tf.keras.layers.Dense(1)])
model.summary()
model.compile(optimizer='adam',
              loss='mse')
model.fit(x,y,epochs=100)
test =data.iloc[:10,1:-1]
print(model.predict(test))
