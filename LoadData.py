from sklearn.model_selection import train_test_split
import numpy as np

def load_data(data_dir):
    raw_data = np.load(data_dir)
    label_1 = np.count_nonzero(raw_data[:,0])
    label_0 = raw_data.shape[0] - label_1
    ratio = 1.0 * label_0 / label_1
    i = 0
    while True:
        if i >= raw_data.shape[0]:
            break
        if np.random.random_sample() > ratio and raw_data[i][0] == 1:
            raw_data = np.delete(raw_data, i, 0)
            i -= 1
        i += 1
    label, data = np.split(raw_data, [1], axis=1)

    return data, label

def split_data(data, label, ratio=0.2):
    X_train, X_test, Y_train, Y_test = train_test_split(data, label, test_size=ratio, random_state=42)

    return X_train, X_test, Y_train, Y_test