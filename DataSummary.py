from LoadData import *

data_dir = "Preprocessing/filled.npy"

raw_data = np.load(data_dir)
label_1 = np.count_nonzero(raw_data[:,0])
label_0 = raw_data.shape[0] - label_1
ratio = 1.0 * label_1 / (label_0 + label_1)
print label_0, label_1, ratio

Y, X = np.split(raw_data, [1], axis=1)
print X.shape, Y.shape

school_dict = {}
for x in X:
    no = x[0]
    school_dict[no] = school_dict.get(no, 0) + 1
max_count = 0
max_index = 0
for s in school_dict:
    if school_dict[s] > max_count:
        max_count = school_dict[s]
        max_index = s

print max_count, 800 - (max_index * 800)

avgs = np.average(X, axis=1)

print "degree:", avgs[2]
print "TOEFL:", avgs[3] * 120, avgs[4] * 30, avgs[5] * 30, avgs[6] * 30, avgs[7] * 30
print "GRE:", avgs[8] * 80 + 260, avgs[9] * 40 + 130, avgs[10] * 40 + 130, avgs[11] * 6
print "GPA:", avgs[12] * 100, avgs[13]