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
        post.school = calibrate_school(university_list, post.school)
        #ff.write(str(post.school) + '\n')
ff.close()