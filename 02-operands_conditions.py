x = 2
if x == 2:
    print("roni")

# my_name = input("enter your name: ")

my_name = "ron"

if my_name == "ron":
    print("you have nice name")

# operators

a = 4
b = 14
if a < b:
    print("a is lower than b")

fname = "ron"
lname = "bar yosef"
age = 55
full_name = "%s %s age: %d" % (fname, lname, age)
full_name2 = "{} {} {}".format(fname, lname, age)
another_full_name = f"my full name {fname} {lname}"

print(full_name)
print(full_name2)
print(another_full_name)

# my_full_description = 'name: "ron"\nmarried: yes\nage: 55'

# using escape
my_full_description = "name: \"ron\"\nmarried: yes\nage: 55"
print(my_full_description)
