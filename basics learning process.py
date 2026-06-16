"""
temp = 22
is_snowing = False
is_raining = False
is_weekend = True
if ((temp > 20 and not is_snowing) and not is_raining) or is_weekend:
    print("Can go out for a walk")
else:
    print("Bad weather to go out for a walk")
"""



"""
def include(arr, item):
    return item in arr   #for codewars
"""



"""
username = "murodboyovich"
password = "secretwars123"
is_verified = True
if (username and password) and is_verified:
    print("Logged in succesfully")
else:
    print("Error occurred in log in")
"""



"""
age = 18
has_license = True
has_car = False
if age >= 18:
    if has_license:
        if has_car:
            print("You can drive")
        else: print("Buy or rent a car first!")
    else: print("Get the driving license first")
else: print("You have to be 18 or older")
"""


"""
score = 81
attendance = 16
submit = True
if score >= 80:
    if attendance > 15:
        if submit:
            print("Passed")
        else: print("not submitted")
    else: print("Low attendance")
else: print("Low score")
"""


"""
score = 99
if score >= 90:
    print("A+")
elif score >= 50:
    pass
else: print("Learn more")
"""


"""
day = 2
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Maybe at the weekend")
"""


"""
day = 2
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
"""



"""
month = 2
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 1:
        print("Weekday in January")
    case 1 | 2 | 3 | 4 | 5 if month == 2:
        print("Weekday in Fevbruary")
"""


"""
def my_func(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
print(my_func(3, 4, 2, 5, 6,))
"""



"""
def changecase(func):
    def myinner():
        return func().upper()
    return myinner

def addgreeting(func):
    def myinner():
        return "Hello " + func() + " Have a great day"
    return myinner

@changecase
@addgreeting
def my_func():
    return "Alex"

print(my_func()) 
"""


"""
def enough(cap, on, wait): #codewars challenge https://www.codewars.com/kata/5875b200d520904a04000003/python
    return max(0, on + wait -cap)

x = enough(10, 6, 5)
print(x)
"""



"""
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
increment = counter()
print(increment())
print(increment())
print(increment())
print(increment())
"""

'''
def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(" ")
    for word in words:
        say(word)

talk("Nigga shut the fuck up")
'''


"""
def counter():
    count = 0

    def increase():
        nonlocal count
        count = count + 1
        return count
    return increase

increase = counter()

print(increase())
print(increase())
print(increase())
"""


"""
def make_negative( number ):
    if number > 0:
        return -(number)
    elif number <= 0:
        return number #for codewars
"""


"""
def mk_ng(num):
    return -abs(num)

print(mk_ng(0)) #easier way
"""


"""
def twice_as_old(dad_years_old, son_years_old):
    f = dad_years_old
    s = son_years_old
    x = f - 2*s
    return abs(x)

print(twice_as_old(55, 30))  #for codewars
"""


"""
def cookie(x):
    if isinstance(x, str):
        name = "Zach"
    elif isinstance(x, (int, float)):
        name = "Monica"
    else: name = "the dog"
    return  "Who ate the last cookie? It was "+name+"!"

x = cookie("string")
print(x)  #for codewars
"""


"""
def bmi(w, h):
    bmi = w/h**2
    if bmi <= 18.5:
        return  "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    elif bmi > 30:
       return "Obese" #for codewars
"""


"""
class animal():
    def walk(self):
        return "Walking..."

class Dog(animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "woof!"

roger = Dog("Roger", 3)

print(roger.name)
print(roger.age)
print(roger.bark())
print(roger.walk())
"""
