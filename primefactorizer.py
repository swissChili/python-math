import prime
import sys

num = sys.argv[1]

primes = []
factors = []

i = 0 
while i < int(num):
    i += 1
    if prime.is_prime(i) == None:
        primes.append(i)
    else:
        pass 

def factor ( num, factors ):
    for prime in primes:
        if int(num) % prime:
            pass 
        else:
            new_num = int(num) / prime
            return factor(new_num, factors)


def all_factors(num):
    all_nums = []
    for i in xrange(num):
        all_nums.append(i)
    print(factor(num, all_nums))

factor_msg = "Factors:"
spacing = len(factor_msg)
print(factor_msg)
all_factors(int(num))
