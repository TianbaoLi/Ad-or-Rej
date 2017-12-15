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
    if score == 0:
        return np.NaN
    elif score < 170 and score > 130:
        return (score - 130) / 40.0
    elif score > 200:
        return (score - 200) / 600
    else:
        return np.NaN

def normalize_gre_aw(score):
    if score != 0:
        return score / 6.0
    else:
        return np.NaN

def normalize_gre_total(score):
    if score == 0:
        return np.NaN
    elif score < 340 and score > 260:
        return (score - 260) / 80.0
    elif score > 400:
        return (score - 400) / 1200
    else:
        return np.NaN