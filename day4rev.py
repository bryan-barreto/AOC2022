elf_list = open("problems/day4.txt").read().split("\n")

part1counter = 0
part2counter = 0
test_array = []
for elf_pair in elf_list:
    elf1, elf2 = elf_pair.split(",")

    elf1small, elf1large = elf1.split("-")
    elf1small = int(elf1small)
    elf1large = int(elf1large)
    elf2small, elf2large = elf2.split("-")
    elf2small = int(elf2small)
    elf2large = int(elf2large)
    
    if ((elf1small <= elf2small and elf1large >= elf2large) or
        (elf2small <= elf1small and elf2large >= elf1large)):
        part1counter += 1
    
    if ((elf1small <= elf2large and elf1large >= elf2small) or
        (elf2small <= elf1large and elf2large >= elf1small)):
        part2counter += 1
        
print(part1counter)
print(part2counter)
