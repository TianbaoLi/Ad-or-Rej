class Post():
    '''
    Store info for each post in the data
    '''

    def __init__(self, school, degree, major, result, year, semester, date, toefl, gre, undergraduate, under_major, gpa, gpa_range, gpa_ranking, others, url):
        self.school = school
        self.degree = degree
        self.major = major
        self.result = result
        self.year = year
        self.semester = semester
        self.date = date
        self.toefl = toefl
        self.gre = gre
        self.undergraduate = undergraduate
        self.under_major = under_major
        self.gpa = gpa
        self.gpa_range = gpa_range
        self.gpa_ranking = gpa_ranking
        self.others = others
        self.url = url
