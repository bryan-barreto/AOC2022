list = open("problems/day1.txt").read().split("\n\n")
total_list = []

for x in list:
    current_elf = x.split()
    elf_carry = 0
    for y in current_elf:
        elf_carry += int(y)
    total_list.append(elf_carry)

total_list.sort(reverse=True)

print("Part 1:\t" + str(total_list[0]))
print("Part 2:\t" + str(total_list[0] + total_list[1] + total_list[2]))
