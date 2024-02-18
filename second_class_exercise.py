#A

x = 20
y = 50

if x > y:
    print("BIG")
elif x < y:
    print("small")

# B

for n in range(5):
    print(n + 1)

# C

season = 4

if season == 1:
    print("summer")
elif season == 2:
    print("winter")
elif season == 3:
    print("fall")
elif season == 4:
    print("spring")

# D

# 1.  10 times
# last print will be 10

# E

age = 35
first_letter = "b"
dollar = 3.60
flew_abroad = True
apartment_number = 20

print(f"age: {age} first letter: {first_letter} currency dollar: {dollar} "
      f"flew abroad: {flew_abroad} apartment number: {apartment_number} ")
sum = dollar + age
if sum == 38.60:
    print("you got the right value")

# F

phone_number = input("please enter your phone number: ")
print(f"phone number {phone_number}")


# G

def printHello():
    print("hello")


def calculate():
    result = 5 + 3.2
    print(result)


#H

def print_my_name(name):
    print(f"my name is {name}")


def divide_a_number(number):
    result = number / 2
    print(result)


#I

def sum(number1, number2):
    return number1 + number2


def strings_concatination(str1, str2):
    return f"{str1} {str2}"


#K

def draw_pyramid_shape(rows):
    for i in range(rows):

        for j in range(i + 1):
            print("*", end="")

        print()

draw_pyramid_shape(5)

#M

def get_number():
    number = int(input("please enter a number: "))
    return number

def compute_sum_of_digits():
    user_number = get_number()
    temp = user_number
    sum = 0

    while temp > 0:
        reminder = int(temp % 10)
        sum += reminder
        temp /= 10

    print(f"the sum of digits for {user_number} is : {sum}")

compute_sum_of_digits()