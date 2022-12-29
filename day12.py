full_map = open("problems/day12.txt").read().split()

class Step():
    def __init__(self, location, height, path, goal) -> None:
        self.location = location
        self.height = height
        self.path = path
        self.huer = find_dist(location, goal)
        
    def get_location(self):
        return self.location
    
    def get_height(self):
        return self.height
    
    def get_path(self):
        return self.path
    
    def test_previous(self, other):
        return other in self.path

def find_pos(pos):
    y = 0
    for row in full_map:
        x = 0
        for column in row:
            if column == pos:
                return (x,y)
            x+=1
        y+=1
        
def find_dist(x,y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])

def have_i(been_there, testing):
    return testing in been_there


def part1():
    counter = 0
    goal = find_pos('E')
    fringe = [Step(find_pos('S'), ord('a'), [], goal)]
    been_there = []
    while 1 > 0:
        counter +=1
        step = fringe.pop(0)
        
        step_location = step.get_location() 
        for test in (-1,0), (1,0), (0,1), (0, -1):
            test = (step_location[0] + test[0], step_location[1] + test[1])
            if test[0] >= len(full_map[0]) or test[0] < 0 or test[1] >= len(full_map) or test[1] < 0:
                continue
            new_height = ord('z') if full_map[test[1]][test[0]] == 'E' else ord(full_map[test[1]][test[0]])
            if have_i(been_there, test):
                continue               
            if new_height - 1 > step.get_height():
                continue
            if test == goal:         
                to_print = step.get_path().copy()
                to_print.append(step.get_location())
                return len(to_print)
            
            path = step.get_path().copy()
            path.append(step.get_location())
            fringe.append(Step(test, new_height, path, goal))
            been_there.append(test)


def part2(x,y):
    counter = 0
    goal = find_pos('E')
    fringe = [Step((x,y), ord('a'), [], goal)]
    been_there = []
    while 1 > 0:
        counter +=1
        if len(fringe) == 0:
            return 1000
        step = fringe.pop(0)
        
        step_location = step.get_location() 
        for test in (-1,0), (1,0), (0,1), (0, -1):
            test = (step_location[0] + test[0], step_location[1] + test[1])
            if test[0] >= len(full_map[0]) or test[0] < 0 or test[1] >= len(full_map) or test[1] < 0:
                continue
            new_height = ord('z') if full_map[test[1]][test[0]] == 'E' else ord(full_map[test[1]][test[0]])
            if have_i(been_there, test):
                continue               
            if new_height - 1 > step.get_height():
                continue
            if test == goal:         
                to_print = step.get_path().copy()
                to_print.append(step.get_location())
                return len(to_print)
            
            path = step.get_path().copy()
            path.append(step.get_location())
            fringe.append(Step(test, new_height, path, goal))
            been_there.append(test)
        
# print(part1())

shortest = 1000
ycounter = 0
for y in full_map:
    xcounter = 0
    for x in y:
        if x != 'a':
            continue
        temp = part2(xcounter,ycounter)
        if temp < shortest:
            shortest = temp 
        xcounter += 1
    ycounter += 1
print(shortest)