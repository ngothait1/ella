import time

print("Hello, This is my final project")
username = input("What is your name? ")
print("Hi " + username + ", nice to meet you")

goodbye_msg = "Thank you " + username + " for using the calculator | " + time.ctime()

print("This is a special calculator, I would need 2 numbers from you.")
num1 = int(input("First number > "))
num2 = int(input("Second Number > "))
print("Thank you for putting in your numbers, " + str(num1) + " and " + str(num2))

#Odd & Even
is_num1_even = "odd"
is_num2_even = "odd"

if num1 % 2 == 0:
    is_num1_even = "even"
if num2 % 2 ==0:
    is_num2_even = "even"

print("I can see that the first number is " + is_num1_even)
print("And the second is " + is_num2_even)

if is_num1_even == is_num2_even:
    print("So both are " + is_num1_even)
else:
    print("So one of them is " + is_num1_even + " and one is " + is_num2_even)

#Operation
operation = input("Operator (+, -, *, /): ")

if operation == "+":
    symbol = " + "
    result = num1 + num2

elif operation == "-":
    symbol = " - "
    result = num1 - num2

elif operation == ("*"):
    symbol = " * "
    result = num1 * num2

elif operation == ("/"):
    symbol = " / "
    user_choice = input("You chose division, should the result be an integer? (y/n) ")
    if num2 == 0:
        print("Error: num_2 is zero \nan error had eccured, please try again")
        print(goodbye_msg)
        exit()
    elif user_choice == "n":
        result = float(num1 / num2)
    elif user_choice == "y":
        result = int(num1 / num2)

else:
    print("Error: invalid operator, please try again")
    exit()

print(num1, symbol, num2, " = ", result)
print(goodbye_msg)