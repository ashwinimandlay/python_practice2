# try except
age = int(input("enter age: "))
print(age)
# if we pass alphabets then age gives value error
# to overcome that we use try and except
# exit code will not be 0
try:
    age = int(input("age: "))
    print(age)
except ValueError:
    print("invalid age !!!")
# here even if we pass alphabet the program ends with code 0

try:
    age = int(input("Age-> "))
    income = 2000
    risk = income / age
    print(age)
    # here if age is zero it gives zero error
except ZeroDivisionError:
    print("age cannot be zero")
except ValueError:
    print("invalid age !!!")
# as a programmer we have to anticipate the error

# also we can use as keyword
try:
    age = int(input("Age-> "))
    income = 2000
    risk = income / age
    print(age)
    # here if age is zero it gives zero error
except ZeroDivisionError as e:
    print("Error:", e)
except ValueError as e:
    print("Error", e)

# if we don't know about the exception use generalized approach:
try:
    age = int(input("Age-> "))
    income = 2000
    risk = income / age
    print(age)
    # here if age is zero it gives zero error
except Exception as e:
    print('Error:', e)
