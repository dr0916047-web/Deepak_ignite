'''import datetime

today = datetime.date.today()

print(today)'''



'''import datetime

now = datetime.datetime.now()

print(now)'''


'''import datetime

now = datetime.datetime.now()

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)'''



'''from datetime import date

birth_year = int(input("Enter birth year: "))

current_year = date.today().year

age = current_year - birth_year

print("Your age is:", age)'''



'''
def decorator(func):

    def wrapper():
        print("Before function")

        func()

        print("After function")

    return wrapper


@decorator
def greet():
    print("Hello Deepak")


greet()
'''


'''def decorator(func):

    def wrapper(*args, **kwargs):
        print("Function started")

        result = func(*args, **kwargs)

        print("Function ended")

        return result

    return wrapper


@decorator
def add(a, b):
    return a + b


print(add(10, 20))'''



'''def outer():

    message = "Hello"

    def inner():
        print(message)

    return inner
    
x = outer()

x()'''




'''numbers = [10, 20, 30]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))'''


'''def numbers():
    yield 10
    yield 20
    yield 30
    
    x = numbers()

print(next(x))
print(next(x))
print(next(x))'''


'''def numbers():
    yield 1
    yield 2
    yield 3

for num in numbers():
    print(num)'''


'''with open("data.txt", "r") as file:

    data = file.read()

    print(data)'''