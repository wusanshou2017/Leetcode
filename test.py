import tensorflow as tf

w1= tf.Variable(tf.random.truncated_normal([784,256],stddev=0.1))
b1 =tf.Variable (tf.zeros([256]))

w2=tf.Variable(tf.random.truncated_normal([256,128],stddev=0.1))
b2 =tf.Variable (tf.zeros([128]))

w3 =tf.Variable(tf.random.truncated_normal([128,10],stddev=0.1))
b3 =tf.Variable(tf.zeros([10]))

x= tf.Variable(tf.random.truncated_normal([128,28,28],stddev=0.1))
# [128,28,28]=> [128,28*28]
x= tf.reshape(x,[-1,28*28])

h1 =x@w1+b1
h1=tf.nn.relu(h1)
h2=h1@w2+b2 
h2 =tf.nn.relu(h2)
out =h2@w3+b3
y =tf.random.uniform([128],maxval=10,dtype=tf.int32)
y_onehot= tf.one_hot(y,depth=10)
loss = tf.square(y_onehot-out)
loss =tf.reduce_mean(loss)
print (loss)


x3=tf.random.normal([2,28,28,1])
x4 =tf.random.normal([28,28])

y2 =x3*x4
print (y2.shape)


