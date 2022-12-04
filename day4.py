list = open("problems/day4.txt").read().split("\n")
counter = 0

for x in list:
    is_first_elf = True
    both_elves = x.split(",")
    elf_1 = ""
    elf_2 = ""
    for y in both_elves:
        range = y.split("-")
        small_range = int(range[0])
        large_range = int(range[1])
        while small_range <= large_range:
            if is_first_elf:
                elf_1 += "00" + str(small_range) + "."
            else:
                elf_2 += "00" + str(small_range) + "."
            small_range += 1
        is_first_elf = False
    if elf_1.__contains__(elf_2) or elf_2.__contains__(elf_1): 
        counter += 1
    
print(counter)

counter = 0

def elf_test(elf_1, elf_2):
    y = 0
    while y < len(elf_1):
        z = 0
        while z < len(elf_2):
            if elf_1[y] == elf_2[z]:
                return 1
            z += 1
        y += 1
    return 0

for x in list:
    is_first_elf = True
    both_elves = x.split(",")
    elf_1 = []
    elf_2 = []
    for y in both_elves:
        range = y.split("-")
        small_range = int(range[0])
        large_range = int(range[1])        
        while small_range <= large_range:
            if is_first_elf:
                elf_1.append(small_range)
            else:
                elf_2.append(small_range)
            small_range += 1
        is_first_elf = False
    
    if len(elf_1) > len(elf_2):
        counter += elf_test(elf_1, elf_2)
    else:
        counter += elf_test(elf_2, elf_1)
    
print(counter)