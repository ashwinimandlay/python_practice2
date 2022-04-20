# modules
# we use it to better organize our code
# we can access modules from same project by using import
import prog43_convertors

print(prog43_convertors.kg_to_pound(70))
# here we imported the entire module

# we can also import just the function from module too
from prog43_convertors import pounds_to_kg

print(pounds_to_kg(155))

# IMPORTANT !!!
# we can also use alias so we don't have to write full name
import prog43_convertors as convertor

print(convertor.kg_to_pound(80))
