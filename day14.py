path_list = open("problems/day14.txt").read().split("\n")

class Sand():
    def __init__(self, start) -> None:
        self.position = start
        
    def fall(self, map, sand, fallout):
        for test in (0,1),(-1,1),(1,1):
            test = (self.position[0] + test[0], self.position[1] + test[1])
            if test not in map and test not in sand:
                self.position = test
                if test[1] > fallout:
                    return "fallout"
                return self.position
        return False

def create_rock_list(path_list):
    rock_list = []
    while len(path_list) > 0:
        row = path_list.pop(0)
        row = row.split(" -> ")
        row_list = []
        for x in row:
            x = x.split(",")
            row_list.append((int(x[0]),int(x[1])))
        row_list = create_rock(row_list)
        for x in row_list:
            rock_list.append(x)
    return rock_list

def create_rock(path):
    return_list = []
    while len(path) > 1:
        return_list.append(path[0])
        testx, testy = path.pop(0)
        heading = path[0]    
        x = heading[0] - testx
        y = heading[1] - testy
        distance = abs(x) + abs(y)
        while distance > 0:
            if x > 0:
                testx = testx + 1
            if x < 0:
                testx = testx - 1
            if y > 0:
                testy = testy + 1
            if y < 0:
                testy = testy - 1
            return_list.append((testx, testy))
            x = heading[0] - testx
            y = heading[1] - testy
            distance = abs(x) + abs(y)
    return return_list

def part1():
    sand_list = []
    rock_list = create_rock_list(path_list)
    rock_list.sort(key = lambda x : x[1], reverse=True)
    end = rock_list[0][1]
    start = (500,0)
    sand = Sand(start)
    last = None
    while 1 > 0:     
        test = sand.fall(rock_list, sand_list, end)
        if test == 'fallout':
            return len(sand_list)
        elif not test:
            sand_list.append(last)
            sand = Sand(start)
            last = None
        else:
            last = test
            

print(part1())