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
        self.toefl_total = None
        self.toefl = toefl #Total Reading Listening Speaking Writing
        self.gre_total = None
        self.gre = gre #Total Verbal Quantity Writing
        self.undergraduate = undergraduate
        self.under_major = under_major
        self.gpa = gpa
        self.gpa_range = gpa_range
        self.gpa_ranking = gpa_ranking
        self.others = others
        self.url = url

    def __str__(self):
        return "school:{0}\ndegree:{1}\nmajor:{2}\nresult:{3}\nyear:{4}\nsemester:{5}\ndate:{6}\ntoefl:{7}\ngre:{8}\nundergraduate:{9}\nunder_major:{10}\ngpa:{11}\ngpa_range:{12}\ngpa_ranking:{13}\nothers:{14}\nurl:{15}\n".format(self.school, self.degree, self.major, self.result, self.year, self.semester, self.date, self.toefl, self.gre, self.undergraduate, self.under_major, self.gpa, self.gpa_range, self.gpa_ranking, self.others, self.url)