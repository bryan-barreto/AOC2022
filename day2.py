rounds = open("problems/day2.txt").read().split("\n")
part_1_total_score = 0
part_2_total_score = 0
current_score = 0

for x in rounds:
    current_round = x.split()
    current_score = 0
    elf_current = ord(current_round[0]) - 64
    me_current = ord(current_round[1]) - 87
    
    #Part 2
    if me_current == 1:
        read = elf_current -1
        if read <= 0:
            read = 3
        current_score += read
    if me_current == 2:
        current_score += elf_current + 3
    if me_current == 3:
        read = elf_current +1
        if read >= 4:
            read = 1
        current_score += read + 6
    part_2_total_score += current_score
    
    #Part 1
    current_score = 0
    current_score += me_current

    compare = me_current - elf_current
    if compare == 0:
        current_score += 3
    elif me_current == 1 and elf_current == 3:
        current_score += 6
    elif me_current == 2 and elf_current == 1:
        current_score += 6
    elif me_current == 3 and elf_current == 2:
        current_score += 6
    part_1_total_score += current_score



print("Part 1:\t" + str(part_1_total_score))
print("Part 2:\t" + str(part_2_total_score))
