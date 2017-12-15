import numpy as np
from sklearn.preprocessing import Imputer

raw_data = np.load("normalized.npy")
data = raw_data
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit(raw_data)
data = imp.transform(data)
np.save('filled', data)
