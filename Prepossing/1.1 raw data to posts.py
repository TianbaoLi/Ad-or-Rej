import csv
from Post import *
from PostEncoder import *
import json

json_file = open('json_data.txt', 'w')

info = []
with open('CommaFixed.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, quotechar='|')
    for row in reader:
        if len(row) == 0:
            continue
        else:
            info.append(row)

for i in info:
    #print i
    #if info.index(i) > 10000:
    #    print info.index(i)
    json_str = None
    if len(i) == 0:
        continue
    elif len(i) == 16:
        school = i[0].strip()
        degree = i[1].strip()
        major = i[2].strip()
        result = i[3].strip()
        year = int(i[4].strip())
        semester = i[5].strip()
        date = i[6].strip()
        toefl = []
        if len(i[7]) != 0:
            try:
                toefl.append(float(i[7].strip().split(' ')[1].replace('+', '')))
            except IndexError:
                print IndexError, 'toefl total', [7], info.index(i)
        RLSW = i[8].split('/')
        try:
            for s in RLSW:
                if len(s.split(':')[1].strip()) == 0 or s.split(':')[1].strip() == '\"':
                    toefl.append(0)
                else:
                    toefl.append(float(s.split(':')[1].strip().strip('\"')))
        except ValueError:
            print ValueError, RLSW, 'toefl', info.index(i)
        gre = []
        if len(i[9]) != 0:
            gre.append(float(i[9].strip().split(' ')[1].replace('+', '')))
        VQW = i[10].split('/')
        try:
            for s in VQW:
                if len(s.split(':')[1].strip()) == 0 or s.split(':')[1].strip() == '\"':
                    gre.append(0)
                else:
                    gre.append(float(s.split(':')[1].strip().strip('\"')))
        except ValueError:
            print ValueError, VQW, 'gre', info.index(i)
        undergraduate = i[11].strip()
        under_major = i[12].strip()
        gpa = i[13].strip()
        gpa_range = i[13].strip()
        gpa_ranking = i[13].strip()
        others = i[14].strip()
        url = i[15].strip()
        post = Post(school, degree, major, result, year, semester, date, toefl, gre, undergraduate, under_major, gpa, gpa_range, gpa_ranking, others, url)
        json_str = json.dumps(post, indent=4, cls=PostEncoder)
        #print post
        #exit(0)
    elif len(i) == 15:
        school = i[0].strip()
        degree = i[1].strip()
        major = i[2].strip()
        result = i[3].strip()
        year = int(i[4].strip())
        semester = i[5].strip()
        date = i[6].strip()
        if i[8].startswith('\"Overall'):
            toefl = []
            if len(i[7]) != 0:
                if i[7].startswith('\"Overall'):
                    toefl = [float(i[7].strip().split(' ')[1].replace('+', ''))]
                else:
                    RLSW = i[7].split('/')
                    try:
                        for s in RLSW:
                            if len(s.split(':')[1].strip()) == 0 or s.split(':')[1].strip() == '\"':
                                toefl.append(0)
                            else:
                                toefl.append(float(s.split(':')[1].strip().strip('\"')))
                    except ValueError:
                        print ValueError, RLSW, 'toefl', info.index(i)
            gre = []
            if len(i[8]) != 0:
                gre.append(float(i[8].strip().split(' ')[1].replace('+', '')))
            VQW = i[9].split('/')
            try:
                for s in VQW:
                    if len(s.split(':')[1].strip()) == 0 or s.split(':')[1].strip() == '\"':
                        gre.append(0)
                    else:
                        gre.append(float(s.split(':')[1].strip().strip('\"')))
            except ValueError:
                print ValueError, VQW, 'gre', info.index(i)
        else:
            toefl = []
            gre = []
            if len(i[7]) != 0:
                toefl.append(float(i[7].strip().split(' ')[1]))
            RLSW = i[8].split('/')
            if len(RLSW) != 1:
                try:
                    for s in RLSW:
                        if len(s.split(':')[1].strip()) == 0 or s.split(':')[1].strip() == '\"':
                            toefl.append(0)
                        else:
                            toefl.append(float(s.split(':')[1].strip().strip('\"')))
                except ValueError:
                    print ValueError, RLSW, 'toefl', info.index(i)
            gre = []
            if len(i[8]) != 0:
                if i[8].startswith('\"Overall'):
                    gre = [float(i[8].strip().split(' ')[1].replace('+', ''))]
                else:
                    VQW = i[8].split('/')
                    if len(VQW) != 1:
                        try:
                            for s in VQW:
                                if len(s.split(':')[1].strip()) == 0 or s.split(':')[1].strip() == '\"':
                                    gre.append(0)
                                else:
                                    gre.append(float(s.split(':')[1].strip().strip('\"')))
                        except ValueError:
                            print ValueError, VQW, 'gre', info.index(i)

        undergraduate = i[10].strip()
        under_major = i[11].strip()
        gpa = i[12].strip()
        gpa_range = i[12].strip()
        gpa_ranking = i[12].strip()
        others = i[13].strip()
        url = i[14].strip()
        post = Post(school, degree, major, result, year, semester, date, toefl, gre, undergraduate, under_major, gpa, gpa_range, gpa_ranking, others, url)
        json_str = json.dumps(post, indent=4, cls=PostEncoder)
        #print 15
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
        toefl = []
        if len(i[7]) != 0:
            if i[7].startswith('\"Overall'):
                toefl = [float(i[7].strip().split(' ')[1].replace('+', ''))]
            else:
                RLSW = i[7].split('/')
                try:
                    for s in RLSW:
                        if len(s.split(':')[1].strip()) == 0 or s.split(':')[1].strip() == '\"':
                            toefl.append(0)
                        else:
                            toefl.append(float(s.split(':')[1].strip().strip('\"')))
                except ValueError:
                    print ValueError, RLSW, 'toefl', info.index(i)
        gre = []
        if len(i[8]) != 0:
            if i[8].startswith('\"Overall'):
                gre = [float(i[8].strip().split(' ')[1].replace('+', ''))]
            else:
                VQW = i[8].split('/')
                try:
                    for s in VQW:
                        if len(s.split(':')[1].strip()) == 0 or s.split(':')[1].strip() == '\"':
                            gre.append(0)
                        else:
                            gre.append(float(s.split(':')[1].strip().strip('\"')))
                except ValueError:
                    print ValueError, VQW, 'gre', info.index(i)
        undergraduate = i[9].strip()
        under_major = i[10].strip()
        gpa = i[11].strip()
        gpa_range = i[11].strip()
        gpa_ranking = i[11].strip()
        others = i[12].strip()
        url = i[13].strip()
        post = Post(school, degree, major, result, year, semester, date, toefl, gre, undergraduate, under_major, gpa, gpa_range, gpa_ranking, others, url)
        json_str = json.dumps(post, indent=4, cls=PostEncoder)
        #print 14
        #print post
        #exit(0)
    else:
        print "ERROR"
        print info.index(i)
        print len(i)
        print i
        #for x in i:
        #    print x
        exit(0)
    json_file.write(json_str + '\n')

json_file.close()