# keyword argument
# for keyword argument position doesn't matters
def greet_user(first_name, last_name):
    print(f"hi {first_name} {last_name}!")
    print("welcome aboard")


print("start")
greet_user("john", "smith")
greet_user(last_name="smith", first_name="john")
# this helps in readability of our code
# ex: shipment_of_goods(50, 2, 0.1)
# shipment_of_goods(mrp=50, shipping_charge=2, tax=0.1)

greet_user("mary", last_name="jane")
# keyword and positional argument can be combined
# but positional argument must come first
print("finish")
