# Leetle Day 39 - Armstrong Number
# 08.02.2025

def solve(num):
    base  = list(str(num))
    power = len(base)
    sum = 0
    for i in base:
        sum += int(i)**power
    if sum == num:
        return True
    else:
        return False