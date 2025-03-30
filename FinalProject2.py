def saveNewEntry():
    id = input("ID: ")
    if id in dataBase:
        print("Error: ID already exists: " + str(dataBase.get(id)))
    elif not id.isdigit():
        print("Error: ID must be a number. " + str(id) + " is not a number")
    else:
        name = input("Name: ")
        age = input("Age: ")
        if not age.isdigit():
            while not age.isdigit():
                age = input("Invald input: Age must be a number, try again: ")
        dataBase[id] = {'name':name, 'age':age}
        print("[+] Entry saved successfully")
    
def searchById():
    id = input("Please enter the ID you want to look for: ")
    if id in dataBase:
        return "ID: " + str(id) + '\n' + "Name: " + dataBase[id]['name'] + '\n' + "Age: " + str(dataBase[id]['age'])
    elif not id.isdigit():
        return "Error: ID must be a number. " + str(id) + " is not a number"
    else:
        return "Error: ID " + str(id) + " is not saved"

def ageAverage():
    total_ages = 0
    divider = 0
    for i in dataBase.keys():
        total_ages += int(dataBase[i]['age'])
        divider += 1
    return total_ages / divider

def printAllNames():
    for index, (key, value) in enumerate(dataBase.items()):
        print(str(index) + ". " + value['name'])

def printAllIDs():
    for index, id in enumerate(dataBase):
        print(str(index) + ". " + str(id))

def printAllEntries():
    for index, (key, value) in enumerate(dataBase.items()):
        print(str(index) + ". " + str(key) + '\n' + "    Name: " + str(value['name']) + '\n' + "    age: " + str(value['age']))

def entryByIndex():
    max_index = 0
    index = input("Please enter the index of the entry you want to print: ")
    if not index.isdigit():
        return "Error: index must be a number. " + str(index) + " is not a number"
    for i, (key, value) in enumerate(dataBase.items()):
        max_index += 1
        if i == int(index):
            return "ID: " + str(key) + '\n' + "Name: " + str(value['name']) + '\n' + "Age: " + str(value['age'])
    return "Error: index is out of range. The maximun index allowed is " + str(max_index - 1)
            
def continue_msg():
        enter = input("Press enter to continue")
        while enter not in [""]:
            enter = input("Press enter to continue")
        if enter == "":
            print("")

dataBase = {}

while True:
    print(""
    "\n---- Main Menu ----"     
    "\n1. Save a new  entry "
    "\n2. Search by ID "
    "\n3. Print ages average "
    "\n4. Print all names "
    "\n5. Print all IDs"
    "\n6. Print all entries"
    "\n7. Print entry by index"
    "\n8. Exit")
    user_input = input("Please choose an option: ")
    if user_input == "1":
        print("\n-----------")
        saveNewEntry()
        continue_msg()
    elif user_input == "2":
        print("\n-----------")
        print(searchById())
        continue_msg()
    elif user_input == "3":
        print("\n-----------")
        print(ageAverage())
        continue_msg()
    elif user_input == "4":
        print("\n-----------")
        printAllNames()
        continue_msg()
    elif user_input == "5":
        print("\n-----------")
        printAllIDs()
        continue_msg()
    elif user_input == "6":
        print("\n-----------")
        printAllEntries()
        continue_msg()
    elif user_input == "7":
        print("\n-----------")
        print(entryByIndex())
        continue_msg()
    elif user_input == "8":
        quit = input("Are you sure? (y/n) ")  
        while quit not in ["y", "n"]:
            quit = input("Are you sure? (y/n) ")
        if quit == "y":
            print("Goodbye!")
            break
        elif quit == "n":
            print("Returning to the main menu... ")
    else:
        if not user_input.isdigit():
            print("\n-----------")
            print("Invalid input. Please choose a number between 1 and 8")
        else:
            print("\n-----------")
            print("Option" + " [" + user_input + "] " + "does not exist. Please try again")
