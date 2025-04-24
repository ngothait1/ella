from Person import Person

class Employee(Person):
    def __init__(self, id, name, age, field_of_work, salary):
        super().__init__(id, name, age)
        self._field_of_work = field_of_work
        self._salary = salary

    def getFieldOfWork(self):
        return self._field_of_work
    
    def getSalary(self):
        return self._salary
    
    def getEmplyeeEntry(self):
        return self._id, self._name, self._age, self._field_of_work, self._salary
    
    def setDictEntry(self):
        return {
            "id":self._id,
            "name":self._name, 
            "age":self._age, 
            "field_of_work":self._field_of_work, 
            "salary":self._salary
        }
    
    def getEmployeeString(self, index):
        return self.getPersonString(index) + ", The field is " + str(self._field_of_work) + ", Salary: " + str(self._salary)
    
    def printMyself(self,index):
        print(self.getEmployeeString(index))