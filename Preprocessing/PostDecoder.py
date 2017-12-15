from Post import *

def decode_post(o):
    post = Post(school=o["school"], degree=o["degree"], major=o["major"], result=o["result"], year=o["year"], semester=o["semester"], date=o["date"], toefl_total=o["toefl_total"], toefl_reading=o["toefl_reading"], toefl_listening=o["toefl_listening"], toefl_speaking=o["toefl_speaking"], toefl_writing=o["toefl_writing"], toefl=o["toefl"], gre_total=o["gre_total"], gre_verbal=o["gre_verbal"], gre_quantity=o["gre_quantity"], gre_writing=o["gre_writing"], gre=o["gre"], undergraduate=o["undergraduate"], under_major=o["under_major"], gpa=o["gpa"], gpa_ranking=o["gpa_ranking"], others=o["others"], url=o["url"])
    return post
