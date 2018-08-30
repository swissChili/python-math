import prime
import sys

num = sys.argv[1]

primes = []
factors = []
prime_factors = []
i = 1 
while i < int(num):
    i += 1
    if prime.is_prime(i) == None:
        primes.append(i)
    else:
        pass 

def get_factors(num, factors, primes):
    for i in primes:
        if int(num) % i == 0:
            factors.append(i)
        else:
            pass

def all_factors(num, factors, prime_factors):
    if prime.is_prime(num) == None:
        return int(num)
    else:
        for i in factors:
            prime_factors.append(i)
            print(prime_factors)
            new_num = int(num) / i
            new_factors = []
            get_factors(new_num, new_factors, primes)
            return all_factors(new_num, new_factors, prime_factors)

get_factors(num, factors, primes)
factor_msg = "Factors:"
spacing = len(factor_msg)
print(factor_msg)
print("[%d]" % all_factors(int(num), factors, prime_factors))
