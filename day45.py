# Leetle Day 45 - Regular Expression Matching
# 14.02.2025

import re

def solve(s, p):
    return bool(re.fullmatch(p, s))