import numpy as np

def normalize_school(school):
    return (800.0 - school) / 800

def normalize_year(year):
    return (year - 2012.0) / 4

def normalize_toefl(score):
    if score != 0:
        return score / 30.0
    else:
        return np.NaN

def normalize_toefl_total(score):
    if score != 0:
        return score / 120.0
    else:
        return np.NaN

def normalize_gre(score):
    if score != 0:
        return (score - 130) / 40.0
    else:
        return np.NaN

def normalize_gre_total(score):
    if score != 0:
        return (score - 260) / 80.0
    else:
        return np.NaN