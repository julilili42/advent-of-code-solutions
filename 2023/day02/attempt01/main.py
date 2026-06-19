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


Games = dict[int, list[dict[str, int]]]

def parse_games(data) -> Games:
    res = {}
    for entry in data:
        entry = entry.strip()
        left, right = entry.split(": ", 1)
        
        game_id = int(re.search(r"(?<=Game\s)\d+", left).group(0))
        
        game_list = []
        for game_set in right.strip().split(";"):
            game = {}
            for cube in game_set.split(","):
                amount, color = cube.strip().split(" ")
                game[color] = amount
            game_list.append(game)

        res[game_id] = game_list
    
    return res

def part1(data): 
    games = parse_games(data)
    res = 0
    bag = {"red": 12, "green": 13, "blue": 14}


    for game_id, game_set in games.items():
        for game in game_set:
            if any(int(amount) > bag[color] for color, amount in game.items()):
                break
        # if the for loop does not break, we enter the else path
        else:
            res += game_id
        
    return res

    

def part2(data):
    games = parse_games(data)
    res = 0

    for game_id, game_set in games.items():
        max_bag = defaultdict(int)
        for game in game_set:
            for color, amount in game.items():
                max_bag[color] = max(max_bag[color], int(amount))
        
        power = 1
        for _, amount in max_bag.items():
            power *= amount
        
        res += power

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
