

def my_printer(prefix, amount_of_times):
    my_var = 5
    for i in range(1,amount_of_times+1):
        print(prefix + str(i))


def mul_five(my_number):
    result = my_number * 5
    return result



my_printer("hello ",5)
my_printer("you are number ",10)

the_result =  mul_five(10)
print(the_result)