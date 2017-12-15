import numpy as np
import json
from PostDecoder import *
from Normalizer import *

POST_N = 15
data = np.zeros((11056, 15))
with open('calibrated.txt', 'r') as file:
    i = 0
    for line in file:
        post_dict = json.loads(line)
        post = decode_post(post_dict[u'__Post__'])
        post_data = np.zeros(POST_N)
        post_data[0] = post.result
        post_data[1] = normalize_school(post.school)
        post_data[2] = post.degree
        post_data[3] = normalize_year(post.year)
        post_data[4] = normalize_toefl_total(post.toefl_total)
        post_data[5] = normalize_toefl(post.toefl_reading)
        post_data[6] = normalize_toefl(post.toefl_listening)
        post_data[7] = normalize_toefl(post.toefl_speaking)
        post_data[8] = normalize_toefl(post.toefl_writing)
        post_data[9] = normalize_gre_total(post.gre_total)
        post_data[10] = normalize_gre(post.gre_verbal)
        post_data[11] = normalize_gre(post.gre_quantity)
        post_data[12] = normalize_gre_aw(post.gre_writing)
        post_data[13] = post.gpa
        post_data[14] = post.gpa_ranking
        #print post_data
        data[i] = post_data
        i += 1
np.save('normalized', data)