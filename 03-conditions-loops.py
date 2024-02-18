a = 5
b = 14
my_name = "ron"
if a < 8 and b > 15:
    print("number in range")
elif my_name == "ron":
    print("you are ron")
    print("hello")
else :
    print("bilbol condition is wrong")


my_list = []
if my_list:                          # when no items in the list this is FALSE
    print("you have items")
else:
    print("no items in the list")

my_list = [12]
if len(my_list) > 0:                          # when no items in the list this is FALSE
    print("you have items")
else:
    print("no items in the list")


my_other_list = ["or","tohar","adam"]
my_other_name = "adam"


# operator in
if my_other_name in my_other_list:
    print(f"{my_other_name} exists in the list")
else:
    print(f"{my_other_name} not exists in the list")


# is operator , check if memory location for 2 variables are in the same place in the memory

tt = [1,2,3]
rr = [1,2,3]
print(tt is rr)

# use is to check if type of variable is -> list
print(type(tt) is list)
