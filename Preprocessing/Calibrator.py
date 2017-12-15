import string
from fuzzywuzzy import fuzz
import time

def calibrate_school(university_list, school):
    exclude = set(string.punctuation)
    school = ''.join(ch for ch in school if ch not in exclude)
    school.replace('  ', '')
    if school.encode('utf-8') in university_list.keys():
        return university_list[school]
    else:
        scores = {}
        for uni in university_list:
            scores[uni] = fuzz.partial_ratio(school, uni)
        choice = max(scores, key=scores.get)
        return university_list[choice]

def calibrate_degree(degree):
    if degree.find('M') != -1 or degree.find('m') != -1:
        return 1
    elif degree.find('D') != -1 or degree.find('d') != -1:
        return 2
    else:
        print degree
        exit(0)

def calibrate_result(result):
    if result.find('A') != -1 or result.find('a') != -1 or result.find('O') != -1 or result.find('o') != -1:
        return 1
    elif result.find('R') != -1 or result.find('r') != -1:
        return 0
    else:
        print result
        exit(0)

def calibrate_year(year):
    try:
        return int(year)
    except ValueError:
        print year
        exit(0)

def calibrate_toefl(toefl):
    toefl_total = 0.0
    if  toefl == None:
        toefl = [0, 0, 0, 0]
    elif len(toefl) == 5:
        toefl_total = toefl[0]
        toefl = toefl[1 : 5]
    elif len(toefl) == 4:
        toefl_total = sum(toefl)
    elif len(toefl) == 0:
        toefl = [0, 0, 0, 0]
    elif len(toefl) == 1:
        toefl_total = toefl[0]
        toefl = [0, 0, 0, 0]
    else:
        print toefl
        exit(0)
    toefl_reading = toefl[0]
    toefl_listening = toefl[1]
    toefl_speaking = toefl[2]
    toefl_writing = toefl[3]
    return toefl_total, toefl, toefl_reading, toefl_listening, toefl_speaking, toefl_writing

def calibrate_gre(gre):
    gre_total = 0.0
    if gre == None:
        gre = [0, 0, 0]
    elif len(gre) == 4:
        gre_total = gre[0]
        gre = gre[1 : 4]
    elif len(gre) == 3:
        gre_total = sum(gre)
    elif len(gre) == 0:
        gre = [0, 0, 0]
    elif len(gre) == 1:
        gre_total = gre[0]
        gre = [0, 0, 0]
    else:
        print gre
        exit(0)
    gre_verbal = gre[0]
    gre_quantity = gre[1]
    gre_writing = gre[2]
    return gre_total, gre, gre_verbal, gre_quantity, gre_writing

def calibrate_gpa(gpa):
    gpa = gpa.strip("\"")
    gpa = gpa.strip()
    gpa_ranking = 0.0
    if gpa == None or len(gpa) == 0:
        gpa = 0.0
        return gpa, gpa_ranking

    splitted = gpa.split(' ')
    if len(splitted) == 1:
        if gpa.find('/') != -1:
            score, total = gpa.split('/')
            gpa = float(score) / float(total)
        else:
            f_gpa = float(gpa)
            if f_gpa <=3.9:
                gpa = f_gpa / 4.0
            elif f_gpa <=5:
                gpa = f_gpa / 4.3
            else:
                gpa = f_gpa / 100.0
        #print gpa, gpa_ranking
    elif len(splitted) == 2:
        scores = splitted[0]
        if scores.find('/') != -1:
            score, total = scores.split('/')
            gpa = float(score) / float(total)
        else:
            f_gpa = float(scores)
            if f_gpa <=3.9:
                gpa = f_gpa / 4.0
            elif f_gpa <=5:
                gpa = f_gpa / 4.3
            else:
                gpa = f_gpa / 100.0
        rank, rank_total = splitted[1].split('/')
        gpa_ranking = float(rank) / float(rank_total)
        #print gpa, gpa_ranking
    else:
        print gpa
        print len(splitted)
        exit(0)
    return gpa, gpa_ranking