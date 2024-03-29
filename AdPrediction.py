import tensorflow as tf
import sklearn
import numpy as np
import numpy.ma as ma
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn import svm
from sklearn import neighbors
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

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

def mnb(train, train_labels, test, test_labels):
    # training the multinomial naive bayes model
    splits = 5
    kf = KFold(splits, shuffle = True, random_state = 0)
    As = [1e-10, 1e-8, 1e-6, 1e-4, 1e-2, 0.1, 0.5, 1.0, 2, 5, 10]
    scores = []
    for a in As:
        model = MultinomialNB(alpha = a)
        score = cross_val_score(model, train, train_labels, cv = kf)
        scores.append(np.mean(score))

    opt_A_index = int(np.argmax(scores))
    opt_A = As[opt_A_index]
    print('Optimal Alpha for multinomial naive bayes = {}'.format(opt_A))
    model = MultinomialNB(alpha = opt_A)
    model.fit(train, train_labels)
    train_pred = model.predict(train)
    print('MultinomialNB train accuracy = {}'.format((train_pred == train_labels).mean()))
    test_pred = model.predict(test)
    print('MultinomialNB test accuracy = {}'.format((test_pred == test_labels).mean()))

    return model

def logistic(train, train_labels, test, test_labels):
    # training the logistic regression model
    splits = 5
    kf = KFold(splits, shuffle = True, random_state = 0)
    Cs = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000, 100000]
    scores = []
    for c in Cs:
        model = LogisticRegression(C = c)
        score = cross_val_score(model, train, train_labels, cv = kf)
        scores.append(np.mean(score))

    opt_C_index = int(np.argmax(scores))
    opt_C = Cs[opt_C_index]

    print('Optimal C for logistic regression = {}'.format(opt_C))
    model = LogisticRegression(C = opt_C)
    model.fit(train, train_labels)
    train_pred = model.predict(train)
    print('Logistic regression train accuracy = {}'.format((train_pred == train_labels).mean()))
    test_pred = model.predict(test)
    print('Logistic regression test accuracy = {}'.format((test_pred == test_labels).mean()))

    return model

def SGD(train, train_labels, test, test_labels):
    # training the stochastic gradient descent model
    splits = 5
    kf = KFold(splits, shuffle = True, random_state = 0)
    As = [1e-10, 1e-8, 1e-6, 1e-4, 1e-2, 0.1, 0.5, 1.0, 2]
    scores = []
    for a in As:
        model = SGDClassifier(alpha = a, max_iter = 100, tol = 1e-3, learning_rate = 'optimal')
        score = cross_val_score(model, train, train_labels, cv = kf)
        scores.append(np.mean(score))

    opt_A_index = int(np.argmax(scores))
    opt_A = As[opt_A_index]
    print('Optimal Alpha for stochastic gradient descent = {}'.format(opt_A))
    model = MultinomialNB(alpha=opt_A)
    model.fit(train, train_labels)
    train_pred = model.predict(train)
    print('SGD train accuracy = {}'.format((train_pred == train_labels).mean()))
    test_pred = model.predict(test)
    print('SGD test accuracy = {}'.format((test_pred == test_labels).mean()))

    return model

def SVM(train, train_labels, test, test_labels):
    # training the support vector machine model
    splits = 5
    kf = KFold(splits, shuffle = True, random_state = 0)
    Cs = [1, 10, 100, 1000, 10000, 100000, 1000000]
    scores = []
    for c in Cs:
        model = svm.LinearSVC(penalty = "l1", dual = False, tol = 1e-3, C = c)
        score = cross_val_score(model, train, train_labels, cv = kf)
        scores.append(np.mean(score))

    opt_C_index = int(np.argmax(scores))
    opt_C = Cs[opt_C_index]

    print('Optimal C for support vector machine = {}'.format(opt_C))
    model = LogisticRegression(C=opt_C)
    model.fit(train, train_labels)
    train_pred = model.predict(train)
    print('SVM train accuracy = {}'.format((train_pred == train_labels).mean()))
    test_pred = model.predict(test)
    print('SVM test accuracy = {}'.format((test_pred == test_labels).mean()))

    return model

def KNN(train, train_labels, test, test_labels):
    # training the K nearest neighbors model
    splits = 5
    kf = KFold(splits, shuffle = True, random_state = 0)
    Ks = range(1, 11)
    scores = []
    for k in Ks:
        model = neighbors.KNeighborsClassifier(n_neighbors = k)
        score = cross_val_score(model, train, train_labels, cv = kf)
        scores.append(np.mean(score))

    opt_K_index = int(np.argmax(scores))
    opt_K = Ks[opt_K_index]

    print('Optimal K for K nearest neighbors = {}'.format(opt_K))
    model = neighbors.KNeighborsClassifier(n_neighbors = opt_K)
    model.fit(train, train_labels)
    train_pred = model.predict(train)
    print('KNN train accuracy = {}'.format((train_pred == train_labels).mean()))
    test_pred = model.predict(test)
    print('KNN test accuracy = {}'.format((test_pred == test_labels).mean()))

    return model

def decision_tree(train, train_labels, test, test_labels):
    # training the decision tree model
    splits = 5
    kf = KFold(splits, shuffle = True, random_state = 0)
    Ds = range(1, 1201, 300)
    scores = []
    for d in Ds:
        model = DecisionTreeClassifier(max_depth = d)
        score = cross_val_score(model, train, train_labels, cv = kf)
        scores.append(np.mean(score))

    opt_D_index = int(np.argmax(scores))
    opt_D = Ds[opt_D_index]

    print('Optimal K for decision tree = {}'.format(opt_D))
    model = DecisionTreeClassifier(max_depth = opt_D)
    model.fit(train, train_labels)
    train_pred = model.predict(train)
    print('Decision tree train accuracy = {}'.format((train_pred == train_labels).mean()))
    test_pred = model.predict(test)
    print('Decision tree test accuracy = {}'.format((test_pred == test_labels).mean()))

    return model

def random_forest(train, train_labels, test, test_labels):
    # training the random forest model
    splits = 5
    kf = KFold(splits, shuffle = True, random_state = 0)
    Ns = range(1, 201, 20)
    scores = []
    for n in Ns:
        model = DecisionTreeClassifier(max_depth = n)
        score = cross_val_score(model, train, train_labels, cv = kf)
        scores.append(np.mean(score))

    opt_N_index = int(np.argmax(scores))
    opt_N = Ns[opt_N_index]

    print('Optimal N for random forest = {}'.format(opt_N))
    model = DecisionTreeClassifier(max_depth = opt_N)
    model.fit(train, train_labels)
    train_pred = model.predict(train)
    print('Random forest train accuracy = {}'.format((train_pred == train_labels).mean()))
    test_pred = model.predict(test)
    print('Random forest test accuracy = {}'.format((test_pred == test_labels).mean()))

def combined_KNN_DCT(KNN_model, decision_tree_model, train, train_labels, test, test_labels):
    X_val, X_test, Y_val, Y_test = train_test_split(test, test_labels, test_size=0.5, random_state=42)
    train_pred_KNN = KNN_model.predict(X_val)
    train_pred_dct = decision_tree_model.predict(X_val)
    As = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    Bs = As
    max_score = 0
    max_a = 0
    max_b = 0
    for a in As:
        for b in Bs:
            train_pred = a * train_pred_KNN + (1 - a) * train_pred_dct
            train_pred = (train_pred > b).astype(int)
            score = (train_pred == Y_val).mean()
            if score > max_score:
                max_score = score
                max_a = a
                max_b = b
    test_pred_KNN = KNN_model.predict(test)
    test_pred_dct = decision_tree_model.predict(test)
    test_pred = max_a * test_pred_KNN + (1 - max_a) * test_pred_dct
    test_pred = (test_pred > max_b).astype(int)

    print('Combined test accuracy = {}'.format((test_pred == test_labels).mean()))

def NN(train, train_labels, test, test_labels):
    # training the neural network model
    splits = 5
    kf = KFold(splits, shuffle = True, random_state = 0)
    As = [1e-12, 1e-10, 1e-8, 1e-6, 1e-4, 0.01, 0.1, 1, 10]
    scores = []
    for a in As:
        model = MLPClassifier(alpha = a, early_stopping = True)
        score = cross_val_score(model, train, train_labels, cv = kf)
        scores.append(np.mean(score))

    opt_A_index = int(np.argmax(scores))
    opt_A = As[opt_A_index]
    print('Optimal Alpha for neural network = {}'.format(opt_A))
    model = MLPClassifier(alpha = opt_A, max_iter = 100, tol = 1e-3, early_stopping = True)
    model.fit(train, train_labels)
    train_pred = model.predict(train)
    print('Neural network train accuracy = {}'.format((train_pred == train_labels).mean()))
    test_pred = model.predict(test)
    print('Neural network test accuracy = {}'.format((test_pred == test_labels).mean()))

def main():
    X, Y = load_data("Preprocessing/filled.npy")
    Y = Y.ravel()
    X_train, X_test, Y_train, Y_test = split_data(X, Y)

    print('### MultinomialNB ###')
    mnb_model = mnb(ma.masked_outside(X_train, 0, 1), ma.masked_outside(Y_train, 0, 1), ma.masked_outside(X_test, 0, 1), ma.masked_outside(Y_test, 0, 1))
    print('### Logistic regression ###')
    logistic_model = logistic(X_train, Y_train, X_test, Y_test)
    print('### Stochastic gradient descent ###')
    SGD_model = SGD(X_train, Y_train, X_test, Y_test)
    print('### Support vector machine ###')
    SVM_model = SVM(X_train, Y_train, X_test, Y_test)
    print('### K nearest neighbors ###')
    KNN_model = KNN(X_train, Y_train, X_test, Y_test)
    print('### Decision tree ###')
    decision_tree_model = decision_tree(X_train, Y_train, X_test, Y_test)
    print('### Random forest ###')
    random_forest_model = random_forest(X_train, Y_train, X_test, Y_test)
    print('### Neural network ###')
    NN_model = NN(X_train, Y_train, X_test, Y_test)
    print('### Combines K nearest neighbors & Decision Tree###')
    combined_KNN_DCT(KNN_model, decision_tree_model, X_train, Y_train, X_test, Y_test)

if __name__ == "__main__":
    main()
