import csv
from Post import *

info = []
with open('go_america_to_study_data.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, quotechar='|')
    for row in reader:
        if len(row) == 0:
            continue
        else:
            info.append(row)

for i in info:
    if len(i) == 0:
        pass
    elif len(i) == 16:
        school = i[0].strip()
        degree = i[1].strip()
        major = i[2].strip()
        result = i[3].strip()
        year = int(i[4].strip())
        semester = i[5].strip()
        date = i[6].strip()
        toefl = []
        toefl.append(float(i[7].strip().split(' ')[1]))
        RLSW = i[8].split('/')
        for s in RLSW:
            toefl.append(float(s.split(':')[1].strip().strip('\"')))
        gre = []
        gre.append(float(i[9].strip().split(' ')[1]))
        VQW = i[10].split('/')
        for s in VQW:
            gre.append(float(s.split(':')[1].strip().strip('\"')))
        undergraduate = i[11].strip()
        under_major = i[12].strip()
        gpa = i[13].strip()
        gpa_range = i[13].strip()
        gpa_ranking = i[13].strip()
        others = i[14].strip()
        url = i[15].strip()
        post = Post(school, degree, major, result, year, semester, date, toefl, gre, undergraduate, under_major, gpa, gpa_range, gpa_ranking, others, url)
        #print 16
        #print post
        #exit(0)
    elif len(i) == 14:
        school = i[0].strip()
        degree = i[1].strip()
        major = i[2].strip()
        result = i[3].strip()
        year = int(i[4].strip())
        semester = i[5].strip()
        date = i[6].strip()
        toefl = i[7].strip()
        gre = i[8].strip()
        undergraduate = i[9].strip()
        under_major = i[10].strip()
        gpa = i[11].strip()
        gpa_range = i[11].strip()
        gpa_ranking = i[11].strip()
        others = i[12].strip()
        url = i[13].strip()
        post = Post(school, degree, major, result, year, semester, date, toefl, gre, undergraduate, under_major, gpa, gpa_range, gpa_ranking, others, url)
        print 14
        print post
        exit(0)
    else:
        print len(i)
        for x in i:
            print x
        exit(0)