import tensorflow as tf
from LoadData import *
import argparse
from pandas import DataFrame

parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', default=100, type=int, help='batch size')
parser.add_argument('--train_steps', default=100000, type=int,
                    help='number of training steps')

def train_input_fn(features, labels, batch_size):
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)
    return dataset

def eval_input_fn(features, labels, batch_size):
    features=dict(features)
    if labels is None:
        inputs = features
    else:
        inputs = (features, labels)
    dataset = tf.data.Dataset.from_tensor_slices(inputs)
    assert batch_size is not None, "batch_size must not be None"
    dataset = dataset.batch(batch_size)
    return dataset

def main(argv):
    args = parser.parse_args(argv[1:])

    X, Y = load_data("Preprocessing/filled.npy")
    Y = Y.ravel()
    X_train, X_test, Y_train, Y_test = split_data(X, Y)
    Y_train = Y_train.T
    X_train = DataFrame(X_train, columns=['school', 'degree', 'year', 'toefl_total', 'toefl_reading', 'toefl_listening', 'toefl_speaking', 'toefl_writing', 'gre_total', 'gre_verbal', 'gre_quantity', 'gre_writing', 'gpa', 'gpa_ranking'])
    Y_train = DataFrame(Y_train)
    X_test = DataFrame(X_test, columns=['school', 'degree', 'year', 'toefl_total', 'toefl_reading', 'toefl_listening', 'toefl_speaking', 'toefl_writing', 'gre_total', 'gre_verbal', 'gre_quantity', 'gre_writing', 'gpa', 'gpa_ranking'])
    Y_test = DataFrame(Y_test)

    my_feature_columns = []
    for key in X_train.keys():
        my_feature_columns.append(tf.feature_column.numeric_column(key=key))

    classifier = tf.estimator.DNNClassifier(
        feature_columns=my_feature_columns,
        hidden_units=[200, 200, 200, 200],
        n_classes=2)

    classifier.train(
        input_fn=lambda:train_input_fn(X_train, Y_train, args.batch_size),
        steps=args.train_steps)

    eval_result = classifier.evaluate(
        input_fn=lambda:eval_input_fn(X_test, Y_test, args.batch_size))
    print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)
