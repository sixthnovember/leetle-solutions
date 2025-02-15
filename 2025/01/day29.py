# Leetle Day 29 - Queue Reconstruction by Height
# 29.01.2025

def solve(people):
    people.sort(key=lambda x: (-x[0], x[1]))
    result = []
    for i in people:
        result.insert(i[1], i)
    return result