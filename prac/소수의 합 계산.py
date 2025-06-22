def is_prime(n, divisor=2):
    if n == divisor:
        return True
    if n % divisor == 0:
        return False
    else:
        return is_prime(n, divisor + 1)

def sum_of_primes(n):
    sum_ = 0
    if n < 2:
        return "Incorrect input"
    else:
        for i in range(2, n + 1):
            if is_prime(i):
                sum_ += i
        return sum_

print(sum_of_primes(20))