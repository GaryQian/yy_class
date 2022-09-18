

# def add_everything(n1, n2, n3):
#     answer = n1 + n2 + n3
#     if (answer > 2):
#         return answer
#     else:
#         return "too small"


def add_everything_n_times(n1, n2, n3):
    if n3 > 0:
        return n1 + n2 + add_everything_n_times(n1, n2, n3 - 1)
    else:
        return n1 + n2

blah = 2
print(add_everything_n_times(1, blah, 3))
print(add_everything_n_times(n3=4, n1=4, n2=6))



def isEven(n):
    if n >= 2:
        return isEven(n-2)
    elif n == 1: 
        return False  
    else:
        return True

def isOdd(n):
    if n >= 2:
        return isOdd(n-2)
    elif n == 1: 
        return True  
    else:
        return False 

def easyIsEven(n):
    return n % 2 == 0


print(easyIsEven(12356788789090987))# True
print(isOdd(3))# False

# 1, 1, 2, 3, 5, 8, 13, 21

def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
    

print(fib(0)) # 1
print(fib(1)) # 1
print(fib(2)) # 2
print(fib(3)) # 3


fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)