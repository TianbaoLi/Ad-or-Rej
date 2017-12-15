import numpy as np
from sklearn.preprocessing import Imputer

data = np.load("normalized.npy")
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit(data)
raw_data = imp.transform(data)

np.save('filled', data)