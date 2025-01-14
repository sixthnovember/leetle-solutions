# Leetle Day 14 - Reverse Words
# 14.01.2025

def solve(s):
    words = s.split(" ")
    words_reversed = []
    for i in reversed(words):
        words_reversed.append(i)
    return " ".join(words_reversed)