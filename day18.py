cube_list = open("problems/day18.txt").read().split()
cubes = []
grid = []

class Cube():
    def __init__(self, input):
        self.x = input[0]
        self.y = input[1]
        self.z = input[2]
        self.exposed = 6

    def sides(self):
        return [self.x, self.y, self.z]
    
    def connected(self):
        self.exposed -= 1
        
    def compare(self, test):
        test_sides = test.sides()
        if ([self.x-1,self.y,self.z] == test_sides or 
            [self.x+1,self.y,self.z] == test_sides or
            [self.x,self.y-1,self.z] == test_sides or
            [self.x,self.y+1,self.z] == test_sides or
            [self.x,self.y,self.z-1] == test_sides or
            [self.x,self.y,self.z+1] == test_sides):
            self.connected()
            test.connected()
    
    def show_exposed(self):
        return self.exposed

counted_list = []
for cube in cube_list:
    split = cube.split(",")
    toint = []
    for x in split:
        toint.append(int(x))
    cubes.append(Cube(toint))

while len(cubes) > 0:
    current = cubes.pop(0)
    for cube in grid:
        cube.compare(current)
    grid.append(current)

total = 0
for cube in grid:
    total += cube.show_exposed()
print(total)