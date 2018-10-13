import sys

def is_prime(num):
    i = 2
    while i < num:
        quotient = num % i
        if quotient == 0:
            return i
        i += 1
print(is_prime(int(sys.argv[1])))
