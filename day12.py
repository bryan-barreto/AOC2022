full_map = open("problems/day12.txt").read().split()

class Step():
    def __init__(self, location, height, path, goal) -> None:
        self.location = location
        self.height = height
        self.path = path
        self.huer = len(path) + find_dist(location, goal)
        
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

def check_fringe(fringe, testing):
    for not_here in fringe:
        if not_here.test_previous(testing):
            return True

def part1():
    counter = 0
    goal = find_pos('E')
    fringe = [Step(find_pos('S'), ord('a')-1, [], goal)]
    while 1 > 0:
        counter +=1
        # if counter % 100 == 0:
        #     print(len(fringe))
        step = fringe.pop(0)
        step_location = step.get_location() 
        for test in (-1,0), (1,0), (0, -1), (0,1):
            test = (step_location[0] + test[0], step_location[1] + test[1])
            if test[0] >= len(full_map[0]) or test[0] < 0 or test[1] >= len(full_map) or test[1] < 0:
                continue
            new_height = ord('z')+1 if full_map[test[1]][test[0]] == 'E' else ord(full_map[test[1]][test[0]])
            if check_fringe(fringe, test):
                continue               
            if new_height - 1 != step.get_height() and new_height != step.get_height() and new_height + 1 != step.get_height():
                continue
            if new_height == ord('z') + 1:
                to_print = step.get_path().copy()
                to_print.append(step.get_location())
                print(to_print)
                return len(to_print)
            if step.test_previous(test):
                continue
            path = step.get_path().copy()
            path.append(step.get_location())
            fringe.append(Step(test, new_height, path, goal))
        # fringe.sort(key = lambda x : x.height, reverse=True)
        fringe.sort(key = lambda x : x.huer)

print(part1())