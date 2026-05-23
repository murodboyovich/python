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


