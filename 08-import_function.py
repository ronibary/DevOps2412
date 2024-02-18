
import fibo as fib_regular
import fibo_ron as fib_ron

# using alias for function in a module
from fibo import fib2 as fib2_reg

#from fibo
#from fibo import fib

#fibo.fib(100)

fib_regular.fib(100)
fib_ron.fib2(100)

print(fib2_reg(100))