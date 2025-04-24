import pandas as pd
from Person import Person
from Employee import Employee
from Student import Student

def exportCSV(objects_dict):
    data_list = []
    for object in objects_dict.values():
            new = object
            data_list.append(new)
    df = pd.DataFrame(data_list)
    user_filename = input("What is your output file name? ")
    df.to_csv(user_filename, index=False)

def status(objects_dict, data_base, id, name, age, employed_list, students_list):
    status = getValidAns("Is " + name + " an Employee? (y/n) ")
    if status == "y":
        field_of_work = input("Field of Work: ")
        salary = getNumber("Salary: ")
        employee = Employee(id, name, age, field_of_work, salary)
        employed_list.append(employee.getEmplyeeEntry())
        objects_dict[id] = employee.setDictEntry()
        data_base[id] = employee
        print("[+] Employee entry saved successfully!")
    if status == "n":
        status = getValidAns("Is " + name + " a student? (y/n) ")
        if status == "y":
            field_of_study = input("Field of Study: ")
            years_of_study = getNumber("Years of Study: ")
            score_avg = getNumber("Score Average: ")
            student = Student(id, name, age, field_of_study, years_of_study, score_avg)
            objects_dict[id] = student.setDictEntry()
            data_base[id] = student
            students_list.append(student)
            print("[+] Student entry saved successfully!")
        else:
            person = Person(id, name, age)
            objects_dict[id] = person.setDictEntry()
            data_base[id] = person
            print("[+] Entry saved successfully!")

def getValidAns(description):
    while True:
        user_input = input(description)
        if user_input == "n":
            return "n"
        if user_input == "y":
            return "y"
        else:
            print("Please enter a valid answer")

def getNumber(key):
    while True:
        user_input = input(key)
        if user_input.isdigit():
            return int(user_input)
        print("Error: " + " must be a number. " + str(user_input) + " is not a number")   

def dictToObject(objects_dict, id):
    if "salary" in objects_dict:
        return Employee(id, objects_dict["name"], objects_dict["age"], objects_dict["field_of_work"], objects_dict["salary"])
    if "score_avg" in objects_dict:
        return Student(id, objects_dict["name"], objects_dict["age"], objects_dict["field_of_study"], objects_dict["sayear_of_studylary"], objects_dict["score_avg"])
    else:
        return Person(id, objects_dict["name"], objects_dict["age"])
        
def saveNewEntry(objects_dict, data_base, id_list):
    id = getNumber("ID: ")
    if id in data_base:
        print("Error: ID already exists: " + str(objects_dict.get(id)))
        return 0
    name = input("Name: ")
    age = getNumber("Age: ")
    data_base[id] = Person(id, name, age)
    status(objects_dict, data_base, id, name, age, employed, students)
    id_list.append(id)
    return age
    
def searchById(data_base):
    id = getNumber("Please enter the ID you want to look for: ")
    if id not in data_base:
        print("Error: ID " + str(id) + " is not saved")
        return 0
    entry = data_base[id]
    entry.printMyself("[ID " + str(id) + "] ")

def ageAverage(data_base, age_sum):
    if len(data_base.keys()) == 0:
        return "Error: No entrys found"
    return age_sum / len(data_base.keys())

def printAllNames(data_base):
    for index, (key, value) in enumerate(data_base.items()):
        print(str(index) + ". " + value.getName())

def printAllIDs(data_base):
    for index, id in enumerate(data_base):
        print(str(index) + ". " + str(id))

def printAllEntries(data_base):
    for index, (key, value) in enumerate(data_base.items()):
        i = "[" + str(index) + "] "
        value.printMyself(i)

def entryByIndex(objects_dict, id_list):
    if len(id_list) == 0:
        print("[-] No entries have been saved yet")
        return 0
    index = getNumber("Please enter the index of the entry you want to print: ")
    max_index = len(id_list) - 1
    if index > max_index:
        print("Error: index is out of range. The maximun index allowed is " + str(max_index))
        return 0
    entry = objects_dict.get(id_list[index])
    person = dictToObject(entry, id_list[index])
    person.printMyself("[ID " + str(id_list[index]) + "] ") 

def printMenu(data_base, sum_ages):
    while True:
        print(
        "\n---- Main Menu ----"     
        "\n1. Save a new  entry "
        "\n2. Search by ID "
        "\n3. Print ages average "
        "\n4. Print all names "
        "\n5. Print all IDs"
        "\n6. Print all entries"
        "\n7. Print entry by index"
        "\n8. Save all data"
        "\n9. Exit")

        user_input = input("Please choose an option: ")
        if user_input == "1":
            sum_ages += saveNewEntry(objects, data_base, ids)
        elif user_input == "2":
            searchById(data_base)
        elif user_input == "3":
            print(ageAverage(data_base, sum_ages))
        elif user_input == "4":
            printAllNames(data_base)
        elif user_input == "5":
            printAllIDs(data_base)
        elif user_input == "6":
            printAllEntries(data_base)
        elif user_input == "7":
            entryByIndex(objects, ids)
        elif user_input == "8":
            exportCSV(objects)
        elif user_input == "9":
            quit = getValidAns("Are you sure? (y/n) ")
            if quit == "y":
                print("Goodbye!")
                break
            elif quit == "n":
                print("Returning to the main menu... ")          
        else:
            if not user_input.isdigit():
                print("Invalid input. Please choose a number between 1 and 8")
            else:
                print("Option" + " [" + user_input + "] " + "does not exist. Please try again")
        input("Press enter to continue")

data_base = {}
students = []
employed = []
objects = {}
sum_ages = 0
ids = []

printMenu(data_base, sum_ages)
