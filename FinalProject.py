import sys
import pandas as pd
from Person import Person
from Employee import Employee
from Student import Student
from Menu import MenuOption

def exportCSV(data_base):
    converted_data = []
    for object in data_base.values():
        converted_object = object
        converted_data.append(converted_object.getDictEntry())
    df = pd.DataFrame(converted_data)
    user_filename = input("What is your output file name? ")
    df.to_csv(user_filename, index=False)
    print("[+] Exported Successfully")

def saveNewPersonByType(data_base, id, name, age):
    person = None
    status = getValidAns("Is " + name + " an Employee? (y/n) ")
    if status == "y":
        field_of_work = input("Field of Work: ")
        salary = getNumber("Salary: ")
        person = Employee(id, name, age, field_of_work, salary)
    if status == "n":
        status = getValidAns("Is " + name + " a student? (y/n) ")
        if status == "y":
            field_of_study = input("Field of Study: ")
            years_of_study = getNumber("Years of Study: ")
            score_avg = getNumber("Score Average: ")
            person = Student(id, name, age, field_of_study, years_of_study, score_avg)
        else:
            person = Person(id, name, age)
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
        
def saveNewEntry(data_base, id_list):
    id = getNumber("ID: ")
    if id in data_base:
        person = data_base[id]
        print("Error: ID already exists: " + str(person.getDictEntry()))
        return 0
    name = input("Name: ")
    age = getNumber("Age: ")
    saveNewPersonByType(data_base, id, name, age)
    id_list.append(id)
    return age
    
def searchById(data_base):
    id = getNumber("Please enter the ID you want to look for: ")
    if id not in data_base:
        print("Error: ID " + str(id) + " is not saved")
        return 0
    entry = data_base[id]
    entry.printMyself("+")

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
        i = str(index)
        value.printMyself(i)

def entryByIndex(id_list, data_base):
    if len(id_list) == 0:
        print("[-] No entries have been saved yet")
        return 0
    index = getNumber("Please enter the index of the entry you want to print: ")
    max_index = len(id_list) - 1
    if index > max_index:
        print("Error: index is out of range. The maximun index allowed is " + str(max_index))
        return 0
    person = data_base[id_list[index]]
    person.printMyself(index)

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

        try:
            user_input = int(input("Please choose an option: "))
            if user_input == MenuOption.SAVE_NEW_ENTRY.value:
                sum_ages += saveNewEntry(data_base, ids)
            elif user_input == MenuOption.SEARCH_BY_ID.value:
                searchById(data_base)
            elif user_input == MenuOption.PRINT_AGE_AVERAGE.value:
                print(ageAverage(data_base, sum_ages))
            elif user_input == MenuOption.PRINT_ALL_NAMES.value:
                printAllNames(data_base)
            elif user_input == MenuOption.PRINT_ALL_IDS.value:
                printAllIDs(data_base)
            elif user_input == MenuOption.PRINT_ALL_ENTRIES.value:
                printAllEntries(data_base)
            elif user_input == MenuOption.PRINT_ENTRY_BY_INDEX.value:
                entryByIndex(ids, data_base)
            elif user_input == MenuOption.SAVE_ALL_DATA.value:
                exportCSV(data_base)
            elif user_input == MenuOption.EXIT.value:
                quit = getValidAns("Are you sure? (y/n) ")
                if quit == "y":
                    print("Goodbye!")
                    break
                elif quit == "n":
                    print("Returning to the main menu... ")
            elif user_input <= 0 or user_input > 9:
                print("Option [" + str(user_input) + "] doesn't exist. Please choose a number between 1-9.")    
            print(input("Press enter to continue "))
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)
        except:
           print("[-] Invalid Input. Please try again.")
           print(input("Press enter to continue "))

data_base = {}
sum_ages = 0
ids = []

printMenu(data_base, sum_ages)
