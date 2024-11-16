numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for n in range(len(numbers)):
    if numbers[n] == 1:
        continue
    is_prime = True
    divisors = 0
    for a in range(2, numbers[n]):
        while divisors == 0:
            if numbers[n] % a == 0:
                divisors = divisors + 1
                if divisors > 0:
                    is_prime = False
                break
            else:
                break
    if is_prime == False:
        not_primes.append(numbers[n])
    else:
        primes.append(numbers[n])
print(f'{primes}')
print(f'{not_primes}')
