# as keyword is used for alias or instance
# it can be used in import, file handling or exception handling

try:
    print(1/0)
except ZeroDivisionError as e:
    print("Error Code:", e)
    # this is same as
    # result = 3+5
    # print('the result is:', result)
    # --> o/p = the result is 7
    # e will be printed as division by zero

# if alias/ instance (e) is not used then it prints
# class of the error
try:
    print(1/0)
except ZeroDivisionError:
    print("Error Code:", ZeroDivisionError)

b = '#'
try:
    print(1/int(b))
except ValueError as e:
    print("Error Code:", e)

# Import random module with alias
import random as geek


# Function showing working of as keyword
def Geek_Func():
    # Using random module with alias
    geek_RandomNumber = geek.randint(5, 10)
    geek_RandomNumber2 = geek.randint(1, 5)

    # Printing our number
    print(geek_RandomNumber)
    print(geek_RandomNumber2)


Geek_Func()

