def summing(a, b):
    return a + b


def extract(a, b):
    return a - b


def power(a, b):
    return a ** b


def product(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    return "Error: Second number shouldn't be 0. Try again from the start"


def root(a, b):
    if b >= 2:
        return a ** (1 / b)
    return "Error: Second number shouldn't be less then 2 and should be integer. Try again from the start"


user_input = 0

while user_input != "7":
    print("Options: \n1.a+b \n2.a-b \n3.a*b \n4.a\\b \n5.a^b \n6.Root of power b from number a \n7.Exit\n")
    user_input = input("Choose an option 1-7 and input ONLY ONE INTEGER number: ")
    result = 0

    if user_input.isdigit() and (1 <= int(user_input) and int(user_input) <= 6):
        print(f"You've chosen option {user_input}. Input 2 numbers.")

        a = input("Input a: ")
        b = input("Input b: ")

        if "." in a or '.' in b or ',' in a or ',' in b:
            a = float(a)
            b = float(b)
        else:
            a = int(a)
            b = int(b)

        user_input = int(user_input)

        if user_input == 1:
            result = summing(a, b)

        elif user_input == 2:
            result = extract(a, b)

        elif user_input == 3:
            result = product(a, b)

        elif user_input == 4:
            result = division(a, b)

        elif user_input == 5:
            result = power(a, b)

        elif user_input == 6:
            result = root(a, b)

        else:
            break

        print(f"Result of calculations is : {result}\n")

    elif user_input.isdigit() and (1 > int(user_input) or int(user_input) > 7) or not user_input.isdigit():
        print("Error: Invalid option. Try again and input integer between 1  and 7 ")

else:
    print("Thank you for usage! ")
