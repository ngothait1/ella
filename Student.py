from Person import Person

class Student(Person):
    def __init__(self, id, name, age, field_of_study, year_of_study, score_avg):
        super().__init__(id, name, age)
        self._field_of_study = field_of_study
        self._year_of_study = year_of_study
        self._score_avg = score_avg

    def getFieldOfStudy(self):
        return self._field_of_study
    
    def getYearOfStudy(self):
        return self._year_of_study
    
    def getScoreAvg(self):
        return self._score_avg
    
    def setDictEntry(self):
        return {
            "id":self._id,
            "name":self._name, 
            "age":self._age, 
            "field_of_study":self._field_of_study, 
            "sayear_of_studylary":self._year_of_study,
            "score_avg":self._score_avg
    }
    
    def getStudentString(self, index):
        return self.getPersonString(index) + ", The field of study is " + str(self._field_of_study) + ", the year of study is " + str(self._year_of_study) + ", the avg is " + str(self._score_avg)
    
    def printMyself(self, index):
        print(self.getStudentString(index))