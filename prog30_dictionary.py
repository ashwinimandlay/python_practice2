# dictionary
# key values pair
# name, email, phone
# IMPORTANT: if we define a dictionary and print then it will
# print in the same order as we have defined the key/value pair
# but if we manually add the key/value pairs then they
# will be unordered

# colon ":" is used to define a block
customer = {
    "name": "john",
    "age": 30,
    "is_verified": True
}
print(customer)
print(customer["name"])
# we can also update after initialization
customer['name'] = 'jack smith'
customer['age'] -= 10
# case-sensitive so if Name is written it shows error
# so use get operator it will simply give NONE output
print(customer.get("NAME"))
# we can attach a default value in the get operator
# so instead of NONE we get that value
print(customer.get("birthdate", "1st march"))

# this prints all keys and values together
for keys, values in customer.items():
    print(keys, values)

# this prints all the keys and values
print(customer)
print(customer.items())
# keys and values separately
print(customer.keys())
print(customer.values())

# IMPORTANT: if you want to add in loop for values like
# in a loop price adds up use :
# dic[item] = dic.get(item, 0) + price
# get method is really useful because we can also select default value

