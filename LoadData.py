from sklearn.model_selection import train_test_split
import numpy as np

def load_data(data_dir):
    raw_data = np.load(data_dir)
    label, data = np.split(raw_data, [1])

    return data, label

def split_data(data, label, ratio=0.2):
    X_train, X_test, y_train, y_test = train_test_split(data, label, test_size=ratio, random_state=42)

    return X_train, X_test, y_train, y_test