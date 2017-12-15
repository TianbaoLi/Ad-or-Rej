import string

def normalize_school(school):
    return (800.0 - school) / 800

def normalize_year(year):
    return (year - 2012.0) / 4

def normalize_toefl(score):
    return score / 30.0

def normalize_toefl_total(score):
    return score / 120.0

def normalize_gre(score):
    return (score - 130) / 40.0

def normalize_gre_total(score):
    return (score - 260) / 80.0