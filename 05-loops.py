
# my_name = "ron"
# prefix = "hello "
# print(list(range(5)))
# print(prefix + my_name)
# print(prefix + my_name)
# print(prefix + my_name)
# print(prefix + my_name)
# print(prefix + my_name)

# for loop

for i in range(5):
    print("hello " + str(i))

class_mate = ["maksim","yoni","gilad","oren"]

# foreach
for name in class_mate:
    if name == "yoni":
        name = "amir"
    print(name)

# for using index
for i in range(len(class_mate)):
    print(class_mate[i])


# while loop , when condition is met
# your_name = input("enter your name")
# while your_name != "ron":
#     print("you are not ron")
#     your_name = input("enter your name")


# you can combine else with the while loop
# when the while condition is not met amymore the else block will run

your_name = input("enter your name")
while your_name != "ron":
    print("you are not ron")
    your_name = input("enter your name")
else:
    print("your name is ron")