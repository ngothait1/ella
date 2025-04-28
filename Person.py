class Person:
    def __init__(self, id, name, age):
        self._id = id
        self._name = name
        self._age = age 

    def getName(self):
        return self._name    

    def getID(self):
        return self._id

    def getAge(self):
        return self._age   

    def getPersonString(self, index):
        return "[" + str(index) + "] [ID:" + str(self._id) + "] " + str(self._name) + ", " + str(self._age) + " years old"

    def getDictEntry(self):
        return {
            "id" : self._id,
            "name" : self._name,
            "age" : self._age
        }
    
    def printMyself(self, index):
        print(self.getPersonString(index))


#Test
if __name__ == "__main__":
    test_id = 109
    test_name = "Mel"
    test_age = 27
    person = Person(test_id, test_name, test_age)

    if person.getID() != test_id:
        print("Error: ID should be " + str(test_id) + " but i got " + str(person.getID()))
    if person.getName() != test_name:
        print("Error: Name should be " + str(test_name) + " but i got " + str(person.getName()))
    if person.getAge() != test_age:
        print("Error: Age should be " + str(test_age) + " but i got " + str(person.getAge()))
    
