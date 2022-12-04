list = open("problems/day3.txt").read().split()
total = 0

def find_common(x):
    array_size = int(len(x)/2)
    test_pos = 0
    while test_pos < array_size:
        test_inner = 0
        while test_inner < array_size:
            if x[test_pos] == x[test_inner+array_size]:
                return x[test_pos]
            test_inner += 1
        test_pos += 1

def group_common(x):
    first = 0
    while first < len(x[0]):
        second = 0
        while second < len(x[1]):
            third = 0
            while third < len(x[2]):
                if x[0][first] == x[1][second] and x[1][second] == x[2][third]:
                    return x[0][first]
                third += 1
            second += 1
        first += 1

def variable_to_total(x, total):
    if ord(x) >= 65 and ord(x) <= 90:
        total += ord(x) - 38
    if ord(x) >= 97 and ord(x) <= 122:
        total += ord(x) - 96
    return total

def part_1():
    total = 0
    for x in list:
        total = variable_to_total(find_common(x), total)        
    print("Part 1:\t" + str(total))
    
def part_2():
    total = 0
    while len(list) > 0:
        group = []
        group.append(list.pop(0))
        group.append(list.pop(0))
        group.append(list.pop(0))
        total = variable_to_total(group_common(group), total)
    print("Part 2:\t" + str(total))
    
    
part_1()
part_2()