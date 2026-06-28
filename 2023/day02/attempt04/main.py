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

def parse_games(data): 
    res = {}
    for row in data:
        row = row.strip()
        left, right = row.split(":")
        _, game_id = left.split(" ")
        game_id = int(game_id.strip())
        
        game_sets = []
        for game_set in right.split(";"):
            game = {}
            for draw in game_set.split(","):
                amount, color = draw.strip().split(" ")
                game[color] = int(amount)
            game_sets.append(game)
        res[game_id] = game_sets

    return res


def part1(data):
    games_parsed = parse_games(data)
    
    available = {"red": 12, "green": 13, "blue": 14}
    res = 0

    for game_id, games in games_parsed.items():
        invalid = any(available[color] < amount for game in games for color, amount in game.items())
        
        if invalid:
            continue
        else:
            res += game_id

    return res

def part2(data):
    games_parsed = parse_games(data)
    
    res = 0

    for game_id, games in games_parsed.items():
        needed = {"red": 0, "green": 0, "blue": 0}
        for game in games:
            for color, amount in game.items():
                needed[color] = max(needed[color], amount)

        product = 1
        for amount in needed.values():
            product *= amount

        res += product
        
    return res




SAMPLES = [
    ("""
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    """, 8, 2286),
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
