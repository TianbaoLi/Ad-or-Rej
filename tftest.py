import numpy as np
import tensorflow as tf
from LoadData import *

'''
m = 1
w = [tf.feature_column.numeric_column("x", shape = [m])]
x_train = np.array([0, 1, 2])
y_train = np.array([-3, -2, -1])
x_test = np.array([5])
y_test = np.array([2])
n_train = x_train.shape[0]
n_test = x_test.shape[0]
estimator = tf.estimator.LinearRegressor(feature_columns = w)

train_fn = tf.estimator.inputs.numpy_input_fn({"x": x_train}, y_train, batch_size=n_train, num_epochs=1000, shuffle=True)
test_fn = tf.estimator.inputs.numpy_input_fn({"x": x_test}, y_test, batch_size=n_test, num_epochs=1000, shuffle=True)
estimator.train(input_fn=train_fn, steps=1000)

train_score = estimator.evaluate(input_fn=train_fn)
print(train_score)
test_score = estimator.evaluate(input_fn=test_fn)
print(test_score)
'''

def main():
    data, label = load_data("Preprocessing/normalized.npy")


if __name__ == "__main__":
    main()
