def f(*args, **kwargs):
    s = 0
    for i in args:
        if type(i) in [int, float]:
            s += i
    return s

my_function_1 = f(1, 5, -3, 'abc', [12, 56, 'cad'])
print(my_function_1)

my_function_2 = f()
print(my_function_2)

my_function_3 = f(2, 4, 'abc', param_1=2)
print(my_function_3)

n = 10


def rec_function(n):
    if n == 0:
        return 0

    return n + rec_function(n - 1)
print('sum of all numbers =', rec_function(n))

def rec_function(n):
    if n == 0:
        return 0
    if not n % 2 == 0:
        return rec_function(n-1)
    else:
        return n + rec_function(n-1)

print('sum of even numbers =', rec_function(10))

def rec_function(n):
    if n == 0:
        return 0
    if not n % 2 != 0:
        return rec_function(n-1)
    else:
        return n + rec_function(n-1)

print('sum of odd numbers =', rec_function(10))

def check_is_digit(my_var):
    if my_var.strip().isdigit():
        return my_var
    else:
        return 0
my_var = input('Enter a number:')
print(check_is_digit(my_var))