import json
import string
from PostDecoder import *
from fuzzywuzzy import fuzz
from Calibrator import *

university_list = {}

index = 1
with open('timesData.csv', 'r') as file:
    for line in file:
        items = line.split(',')
        name = items[1].strip().decode('utf-8')
        rank = items[0].strip()
        if rank.find('-') == -1:
            rank = int(rank)
        else:
            rank = index
        university_list[name] = rank
        index += 1

ff = open('temp.txt', 'w')
with open('json_data.txt', 'r') as file:
    for line in file:
        post_dict = json.loads(line)
        post = decode_post(post_dict[u'__Post__'])

        #post.school = calibrate_school(university_list, post.school)
        #post.degree = calibrate_degree(post.degree)
        #post.result = calibrate_result(post.result)
        #post.year = calibrate_year(post.year)
        #post.toefl_total, post.toefl, post.toefl_reading, post.toefl_listening, post.toefl_speaking, post.toefl_writing = calibrate_toefl(post.toefl)
        #post.gre_total, post.gre, post.gre_verbal, post.gre_quantity, post.gre_writing = calibrate_gre(post.gre)
        calibrate_gpa(post.gpa)
        ff.write(str(post.gre_total) + str(post.gre) + str(post.gre_verbal) + str(post.gre_quantity) + str(post.gre_writing) + '\n')
ff.close()