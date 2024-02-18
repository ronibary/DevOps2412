# def get_user_age():
#     try:
#         user_age = int(input("enter age"))
#     except BaseException as e:
#         print("error occurred : " + str(e.args[0]))
#     if user_age < 0:
#         raise ValueError("age is wrong format")
#
#
# get_user_age()


class NegativeAgeError(Exception):
    """Exception raised for negative user age."""

    def _init_(self, age, message="Age cannot be negative"):
        self.age = age
        self.message = message
        super()._init_(self.message)

    def _str_(self):
        return f"{self.message}: {self.age}"


# example how to raise exception when you detect the age is negetive
# raise a custom Error class

def get_user_age():
    try:
        user_age = int(input("enter age"))
    except BaseException as e:
        print("error occurred : " + str(e.args[0]))
    if user_age < 0:
        raise NegativeAgeError("")
    return user_age


# try:
#     get_user_age()
# except NegativeAgeError:
#     print("age cannot be negative")
