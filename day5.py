import math
import numpy as np
import re

list = open("problems/day5.txt").read().split('\n')
linelen = len(list[0])


def obtain_list():
    cargo_list = []
    while len(list) > 0:
        test = list.pop(0)
        if test == "":
            return cargo_list
        cargo_list.append(test)


def part1():
    full_set = [ ['G', 'D', 'V', 'Z', 'J', 'S', 'B'],
            ['Z', 'S', 'M', 'G', 'V', 'P'],
            ['C', 'L', 'B', 'S', 'W', 'T', 'Q', 'F'],
            ['H', 'J', 'G', 'W', 'M', 'R', 'V', 'Q'],
            ['C', 'L', 'S', 'N', 'F', 'M', 'D'],
            ['R', 'G', 'C', 'D'],
            ['H', 'G', 'T', 'R', 'J', 'D', 'S', 'Q'],
            ['P', 'F', 'V'],
            ['D', 'R', 'S', 'T', 'J']]
    for x in list:
        counter = 0
        move_to = re.findall("\d+", x)
        while counter < int(move_to[0]):
            full_set[int(move_to[2])-1].append( full_set[int(move_to[1])-1].pop())
            counter += 1
    counter = 0
    answer = ""
    while counter < total_rows:
        answer += str(full_set[counter][-1])
        counter += 1
    print(answer)


def part2():
    full_set = [ ['G', 'D', 'V', 'Z', 'J', 'S', 'B'],
            ['Z', 'S', 'M', 'G', 'V', 'P'],
            ['C', 'L', 'B', 'S', 'W', 'T', 'Q', 'F'],
            ['H', 'J', 'G', 'W', 'M', 'R', 'V', 'Q'],
            ['C', 'L', 'S', 'N', 'F', 'M', 'D'],
            ['R', 'G', 'C', 'D'],
            ['H', 'G', 'T', 'R', 'J', 'D', 'S', 'Q'],
            ['P', 'F', 'V'],
            ['D', 'R', 'S', 'T', 'J']]
    for x in list:
        counter = 0
        move_to = re.findall("\d+", x)
        maxcarry = int(move_to[0])
        while counter < int(move_to[0]):
            full_set[int(move_to[2])-1].append( full_set[int(move_to[1])-1].pop(-maxcarry))
            counter += 1
            maxcarry -= 1
    counter = 0
    answer = ""
    while counter < total_rows:
        answer += str(full_set[counter][-1])
        counter += 1
    print(answer)


cargo_list = obtain_list()
total_rows = math.ceil(linelen/4)       
part1()
part2()


