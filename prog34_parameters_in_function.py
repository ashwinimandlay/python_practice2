# parameters on function
# positional arguments
# instead of hi there the person name appears
def greet_user(first_name, last_name):
    # this is same as defining john in greet function
    # but if multiple user present then it gets repetative
    print(f"hi {first_name} {last_name}!")
    print("welcome aboard")


# always keep 2 empty spaces after function
print("start")
greet_user("john", "smith")
# if a parameter is defined then we are obligated to pass
# that parameter or we will get error
greet_user("mary", "jane")
print("finish")
