import tensorflow as tf

w = tf.Variable([0.], tf.float32)
b = tf.Variable([0.], tf.float32)

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
p = w * x + b

loss = tf.reduce_sum(tf.square(y - p))
optimizer = tf.train.GradientDescentOptimizer(0.1)
train = optimizer.minimize(loss)

x_train = [0, 1, 2]
y_train = [-3, -2, -1]

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

for i in range(100):
    sess.run(train, {x: x_train, y: y_train})
print(sess.run([w, b, loss], {x: x_train, y: y_train}))
