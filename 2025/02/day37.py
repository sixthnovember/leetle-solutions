# Leetle Day 37 - Count Prime Numbers
# 06.02.2025

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solve(n):
    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    return count