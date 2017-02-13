### In the following infinite sequences, we define the set of natural numbers (N)
### as beginning with '0'.

#Infinite sequence of (n), for all n in N
def natural_numbers():
    number = 0
    while True:
        number += 1
        yield number

#Infinite sequence ((-1)^n), for all n in N
def oscillating_sign():
    number = -1
    while True:
        number = -number
        yield number

#Infinite Fibonacci sequence
def fibonacci():
    a = 0
    b = 1
    c = 0
    function_calls = 0
    while True:
        if (function_calls <= 1):
            function_calls += 1
            yield (function_calls - 1)
        else:
            c = a + b
            a = b
            b = c
            yield c

