# pathlib
# this is a in-built module which helps to add, check,
# remove directories or number of a certain type of file
# ex: we can list all the .py files or .xls file

from pathlib import Path
# note that the "P" is capital in Path, means it is a class
path1 = Path("ecommerce")
print(path1.exists())

path2 = Path("emails")
print(path2.exists())
# since there is no package of emails therefore boolean is
# False

# we can also make a directory by mkdir
# path3 = Path("email")
# print(path3.mkdir())

# we can also remove dir by rmdir
# path4 = Path("email")
# path4.rmdir()

path5 = Path()
for file in path5.glob("*.py"):
    print(file)
# all the py files is the directory

for file in path5.glob("*"):
    print(file)
# all the directories and files
