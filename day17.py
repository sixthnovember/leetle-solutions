# Leetle Day 17 - Count Vowels
# 17.01.2025

def solve(text):
    vowels = ["a", "e", "i", "o", "u"]
    counter = 0
    for i in text:
        if i.lower() in vowels:
            counter += 1
    return counter