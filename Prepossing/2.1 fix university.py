import json
from PostDecoder import *

with open('json_data.txt', 'r') as file:
    for line in file:
        post_dict = json.loads(line)
        post = decode_post(post_dict[u'__Post__'])
        print post.__str__()
        exit(0)