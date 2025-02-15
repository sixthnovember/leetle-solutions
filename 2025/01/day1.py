# Leetle Day 1 - Fizzbuzz
# 01.01.2025

def solve(n):
    result = []
    for i in range(n):
        num = i + 1
        if num % 3 == 0 and num % 5 == 0:
            result.append("FizzBuzz")
        elif num % 3 == 0:
            result.append("Fizz")
        elif num % 5 == 0:
            result.append("Buzz")
        else:
            result.append(num)
    return result