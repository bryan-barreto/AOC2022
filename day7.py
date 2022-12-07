list = open("problems/day7.txt").read().split("\n")

class Resource:
    def __init__(self, parent, type, name, size):
        self.parent = parent
        self.name = name 
        self.size = size
        self.type = type
    def __str__(self) -> str:
        return f"{self.parent}{self.name} Size:{self.size} Type:{self.type}"
       

def get_dir(directory):
    directory = ""
    for y in current_dir:
        directory += y
    return directory
    
def create_db():
    x = list.pop(0)
    command = x.split()
    if command[0] == "$":
        if command[1] == "cd":
            if command[2] == "..":
                current_dir.pop()
            elif command[2] == "/":
                current_dir.append(command[2])
            else:
                current_dir.append(command[2] + "/")
        elif command[1] == "ls":
            pass
    elif command[0] == "dir":
        directory = get_dir(current_dir)
        filelist.append(Resource(directory, "dir", command[1], 0))
    else:
        size = int(command[0])
        file = command[1]
        directory = get_dir(current_dir)
        filelist.append(Resource(directory, "file", file, size))

def part1():
    final_count = 0

    for x in filelist:
        for y in filelist:
            if (x.parent + x.name + "/") == y.parent:
                x.size += y.size
            
    for x in filelist:
        if x.type == "dir" and x.size <= 100000:
            final_count += x.size
    print("Part 1:\t" + str(final_count))


def part2():
    final_count = 70000000
    system_size = 0
    
    for x in filelist:
        if x.type =="file":
            system_size += x.size
        
    for x in filelist:
        for y in filelist:
            if (x.parent + x.name + "/") == y.parent:
                test = (system_size - x.size)
                if test < 40000000 and test > (system_size - final_count):
                    final_count = x.size
    print("Part 2:\t" + str(final_count))

current_dir = []
filelist = []
while len(list) > 0:
        create_db()
filelist.reverse()
part1()
part2()