
import requests

try:

    response = requests.get("kndfklg:.//moasfdg")      # create exception
except BaseException as e:
    print("something went wrong with the requests")
    print(e.args)      # print the stack trace on the error

while True:
    try:
        a = int(input("enter first number"))
        b = int(input("enter second number"))
        result = a / b
        print(result)
        break
    except ValueError:
        print("something went wrong ... enter a correct number ")
    except ZeroDivisionError:
        print("Error division by zero")
    except BaseException as e:
        print(e.args)


