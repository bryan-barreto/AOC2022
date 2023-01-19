cube_list = open("problems/day18.txt").read().split()
cubes = []
grid = []
plain = []
air = []

class Cube():
    def __init__(self, input):
        self.x = input[0]
        self.y = input[1]
        self.z = input[2]
        self.exposed = 6

    def sides(self):
        return (self.x, self.y, self.z)
    
    def connected(self):
        self.exposed -= 1
        
    def compare(self, test):
        test_sides = test.sides()
        if ((self.x-1,self.y,self.z) == test_sides or 
            (self.x+1,self.y,self.z) == test_sides or
            (self.x,self.y-1,self.z) == test_sides or
            (self.x,self.y+1,self.z) == test_sides or
            (self.x,self.y,self.z-1) == test_sides or
            (self.x,self.y,self.z+1) == test_sides):
            self.connected()
            test.connected()
    
    def show_exposed(self):
        return self.exposed

def create_grid():
    for cube in cube_list:
        split = cube.split(",")
        toint = (int(split[0]), int(split[1]), int(split[2]))
        cubes.append(Cube(toint))
        plain.append(toint)

    while len(cubes) > 0:
        current = cubes.pop(0)
        for cube in grid:
            cube.compare(current)
        grid.append(current)

def find_air(space):
    for x in ([1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]):
        test = [space[0] + x[0], space[1] + x[1], space[2] + x[2]]
        if test not in plain and test in air: 
            return False
        for cube in plain:
            if ((space[0] > cube[0] or 
                space[0] < cube[0]) and
                (space[1] > cube[1] or 
                space[1] < cube[1]) and
                (space[2] > cube[2] or 
                space[2] < cube[2])):
                break                
    air.append(space)
    return True

def fludd_scan(grid):
    grid.sort()
    left = grid[0][0] - 1
    right = grid[len(grid) - 1][0] + 1
    grid.sort(key = lambda x : x[1])
    bottom = grid[0][1] - 1
    top = grid[len(grid) - 1][1] + 1
    grid.sort(key = lambda x : x[2])
    backward = grid[0][2] - 1
    forward = grid[len(grid) - 1][2] + 1
    fringe = [(left,bottom,backward)]
    past = []
    found = []
    while len(fringe) > 0:
        test = fringe.pop(0)
        past.append(test)
        for x in ((0,1,0),(1,0,0),[0,-1,0],(-1,0,0),(0,0,1),(0,0,-1)):
            x = (test[0] + x[0],test[1] + x[1], test[2] + x[2])
            if x in fringe or x in past or x in found:
                continue
            if (x[0] < left or
                x[0] > right or
                x[1] < bottom or
                x[1] > top or
                x[2] < backward or
                x[2] > forward):
                continue
            if x in grid:
                found.append(test)
                continue
            fringe.append(x)
    return len(found)
            

create_grid()

def part1():
    total = 0
    for cube in grid:
        total += cube.show_exposed()
    return total

    
print(part1())

print(fludd_scan(plain))
