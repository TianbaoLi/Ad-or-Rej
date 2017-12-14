from Post import *

def decode_post(o):
    post = Post(school=o["school"], degree=o["degree"], major=o["major"], result=o["result"], year=o["year"], semester=o["semester"], date=o["date"], toefl_total=o["toefl_total"], toefl=o["toefl"], gre_total=o["gre_total"], gre=o["gre"], undergraduate=o["undergraduate"], under_major=o["under_major"], gpa=o["gpa"], gpa_range=o["gpa_range"], gpa_ranking=o["gpa_ranking"], others=o["others"], url=o["url"])
    return post
