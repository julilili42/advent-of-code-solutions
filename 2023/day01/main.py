from __future__ import annotations

from typing import *
from collections import defaultdict, Counter, deque
from functools import lru_cache, cache
from itertools import *
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
from math import inf, gcd, lcm
import sys
import re


INPUT_FILE = "input.txt"


def parse(raw: str) -> List[str]:
    return raw.strip().splitlines()


def part1(data):
    cleaned_data = [l.strip() for l in data]
    sum = 0

    for l in cleaned_data:
        num_filter = [ch for ch in l if ch.isnumeric()]
        total = num_filter[0] + num_filter[-1]
        sum += int(total)
    
    return sum

# first tried to replace substrings in line. This however fails for overlapping strings, for example: twone -> tw1 != 21
def part2(data):
    total_sum = 0
    valid_num = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    

    for line in data:
        line = line.strip()
        nums = []

        for i in range(len(line)):
            if line[i].isnumeric():
                nums.append(line[i])
            
            # beginning at index i look if the line contains any of the keys in the dictionary. If this is the case
            # we add the number to the numbers array. This method works on overlapping strings. 
            for word, digit in valid_num.items():
                if line.startswith(word, i):
                    nums.append(digit)
        
        total_sum += int(str(nums[0]) + str(nums[-1]))


    return total_sum


def part1Pointer(data):
    res = [0] * len(data)
    
    for i, line in enumerate(data):
        line = line.strip()
        
        l = 0
        r = len(line) - 1
        
        l_done, r_done = None, None
       
        while l <= r:
            if l_done == None:
                if line[l].isnumeric():
                    l_done = line[l]
                else:
                    l += 1
                    
            if r_done == None:
                if line[r].isnumeric():
                    r_done = line[r]
                else:
                    r -= 1

            if (l_done != None and r_done != None):
                res[i] = str(l_done) + str(r_done)
                break
    return sum(int(num) for num in res)



SAMPLES = [
    ("""
    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    """, 142, None),
    ("""
    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen
    """, None, 281)
]


def run_samples():
    if not SAMPLES:
        print("No samples yet.")
        return

    for i, (raw, expected1, expected2) in enumerate(SAMPLES, 1):
        raw = raw.strip("\n")

        if expected1 is not None:
            got1 = part1(parse(raw))
            if got1 == expected1:
                print(f"Sample {i} Part 1: OK")
            else:
                print(f"Sample {i} Part 1: FAIL")
                print(f"  got:      {got1}")
                print(f"  expected: {expected1}")

        if expected2 is not None:
            got2 = part2(parse(raw))
            if got2 == expected2:
                print(f"Sample {i} Part 2: OK")
            else:
                print(f"Sample {i} Part 2: FAIL")
                print(f"  got:      {got2}")
                print(f"  expected: {expected2}")


def run_real_input():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        raw = f.read()

    print("Part 1:", part1(parse(raw)))
    print("Part 2:", part2(parse(raw)))


if __name__ == "__main__":
    run_samples()
    print()
    run_real_input()
