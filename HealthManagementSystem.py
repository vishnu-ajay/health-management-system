# Health Management System
# 3 clients - Harry, Rohan and Hammad
# log / retrieve their diet and exercise
# total 6 files

customer_list = ['Harry', 'Rohan', 'Hammad']


def getdate():
    import datetime
    return datetime.datetime.now()


def menu():
    print("Welcome to Health Management System")
    n = int(input("Enter 1 to log details\nEnter 2 to retrieve details: "))
    while n != 1 and n != 2:
        print("Wrong choice entered. Try again")
        n = int(input("Enter 1 to log details\nEnter 2 to retrieve details: "))
    name = input("Enter client name: ")
    name.capitalize()
    while name not in customer_list:
        print('Customer not registered, try again')
        name = input("Enter client name: ")
    if n == 1:
        enter_customer_details(name)
    else:
        retrieve_customer_details(name)
    s = input('Enter Y to continue, N to exit: ')
    s.capitalize()
    if s == 'Y':
        menu()


def enter_customer_details(name):
    query = input("Enter E to log exercise, D to log diet: ")
    query.capitalize()
    while query != 'E' and query != 'D':
        print('Wrong query entered. Try again')
        query = input("Enter E to log exercise, D to log diet: ")
    if name == "Harry" and query == 'E':
        f = open("HarryExercise.txt", "a")
        ex = input("Enter exercises done: ")
    elif name == "Harry" and query == 'D':
        f = open("HarryDiet.txt", "a")
        ex = input("Diet for the day: ")
    elif name == "Hammad" and query == 'E':
        f = open("HammadExercise.txt", "a")
        ex = input("Enter exercises done: ")
    elif name == "Hammad" and query == 'D':
        f = open("HammadDiet.txt", "a")
        ex = input("Diet for the day: ")
    elif name == "Rohan" and query == 'E':
        f = open("RohanExercise.txt", "a")
        ex = input("Enter exercises done: ")
    elif name == "Rohan" and query == 'D':
        f = open("RohanDiet.txt", "a")
        ex = input("Diet for the day: ")
    else:
        print("Customer not registered, try again")
        enter_customer_details()

    dt = getdate()
    f.write('\n' + '[' + str(dt) + '] ' + ex)
    print('Successfully updated')
    f.close()


def retrieve_customer_details(name):
    query = input("Enter E to retrieve exercise, D to retrieve diet: ")
    query.capitalize()
    file_open = True
    while query != 'E' and query != 'D':
        print('Wrong query entered. Try again')
        query = input("Enter E to log exercise, D to retrieve diet: ")
    if name == "Harry" and query == 'E':
        try:
            f = open("HarryExercise.txt")
        except Exception as e:
            print(e, 'No logs made yet')
            file_open = False
    elif name == "Harry" and query == 'D':
        try:
            f = open("HarryDiet.txt")
        except Exception as e:
            print(e, 'No logs made yet')
            file_open = False
    elif name == "Hammad" and query == 'E':
        try:
            f = open("HammadExercise.txt")
        except Exception as e:
            print(e, 'No logs made yet')
            file_open = False
    elif name == "Hammad" and query == 'D':
        try:
            f = open("HammadDiet.txt")
        except Exception as e:
            print(e, 'No logs made yet')
            file_open = False
    elif name == "Rohan" and query == 'E':
        try:
            f = open("RohanExercise.txt")
        except Exception as e:
            print(e, 'No logs made yet')
            file_open = False
    elif name == "Rohan" and query == 'D':
        try:
            f = open("RohanDiet.txt")
        except Exception as e:
            print(e, 'No logs made yet')
            file_open = False

    if file_open:
        content = f.read()
        print(content)
        f.close()


menu()
