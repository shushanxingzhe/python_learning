import numpy as np
import tensorflow.compat.v1 as tf

tf.compat.v1.disable_eager_execution()
np.random.seed(1)

x_train = np.linspace(-2, 2, 200)
y_train = 3.0 * x_train + 7.0 + np.random.random(*x_train.shape) * 0.4
x_train = x_train.reshape([-1, 1])
y_train = y_train.reshape([-1, 1])

X = tf.placeholder(dtype=tf.float32, shape=[None, 1], name='x')
Y = tf.placeholder(dtype=tf.float32, shape=[None, 1], name='y')
W = tf.Variable(0.0, name='W')
b = tf.Variable(0.0, name='b')

pred = W * X + b
loss = tf.reduce_mean((pred - Y) ** 2)
# optimize = tf.train.GradientDescentOptimizer(0.01)
optimize = tf.train.RMSPropOptimizer(0.01)
optimize_op = optimize.minimize(loss)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for i in range(1, 1000):
        l, _ = sess.run([loss, optimize_op], feed_dict={X: x_train, Y: y_train})
        if i % 50 == 0:
            print(l)
    w_val, b_val = sess.run([W, b])
    print("W:", w_val, '  b:', b_val)
    print(sess.run(pred, feed_dict={X: [[3]]}))
