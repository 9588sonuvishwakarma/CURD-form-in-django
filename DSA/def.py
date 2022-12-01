def son(n):
    print("sonu "+n)
son('vishwkarma')

def ao(n):
    n('sonu')
ao(print)
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))

def fabonaci(n):
    if n ==1:
        return 0
    elif n==2:
        return 1
    else:
        return fabonaci(n-1)+fabonaci(n-2)
print(fabonaci(5))
import time

result = time.localtime()
print(result)