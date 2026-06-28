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


def parse(raw: str):
    return raw.strip().splitlines()


def part1(data):
    res = 0
    for row in data:
        row = row.strip()
        temp = []
        for ch in row:
            if ch.isnumeric():
                temp.append(ch)

        res += int(temp[0] + temp[-1])

    return res


def part2(data):
    numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    res = 0

    for row in data:
        row = row.strip()
        temp = []
        for i,ch in enumerate(row):
            for num in numbers.keys():
                if row.startswith(num, i):
                    temp += numbers[num]
            if ch.isnumeric():
                temp += ch
        res += int(temp[0] + temp[-1])

    return res


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
    """, None, 281),
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
