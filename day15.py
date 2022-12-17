import re

class Sensor():
    def __init__(self, input) -> None:
        hold = re.search("Sensor at x=(.+), y=(.+):", input).groups()
        self.position = (int(hold[0]), int(hold[1]))
        hold = re.search("closest beacon is at x=(.+), y=(.+)", input).groups()
        self.beacon = (int(hold[0]), int(hold[1]))
        self.distance = abs(self.position[0] - self.beacon[0]) + abs(self.position[1] - self.beacon[1])
        self.edge = []
    
    def find_edges(self): # earlier attempt, not used
        counter = 0
        distance = self.distance
        while counter <= distance:
            for x in ((self.position[0] + counter, self.position[1] + distance),
                      (self.position[0] + counter, self.position[1] - distance),
                      (self.position[0] - counter, self.position[1] + distance),
                      (self.position[0] - counter, self.position[1] - distance),
                      (self.position[0] + distance, self.position[1] + counter),
                      (self.position[0] + distance, self.position[1] - counter),
                      (self.position[0] - distance, self.position[1] + counter),
                      (self.position[0] - distance, self.position[1] - counter)):
                if x not in self.edge:
                    self.edge.append(x) 
                    
            counter += 1
            distance -= 1

    def signal_at_y(self, y):
        if y <= self.position[1] + self.distance and y >= self.position[1] - self.distance:
            difference = None
            if y >= self.position[1]:
                difference = self.position[1] + self.distance - y
            else:
                difference = self.position[1] - self.distance - y
            if (self.position[0] + difference) > (self.position[0] - difference):
                return ((self.position[0] - difference), (self.position[0] + difference))
            else:
                return ((self.position[0] + difference), (self.position[0] - difference))
        return None

    
    def beacon_at_y(self, y):
        if self.beacon[1] == y:
            return self.beacon
        return None
    
    def return_column(self, y):
        hold = []
        for x in self.edge:
            if x[1] == y:
                hold.append(x)
        return hold        

def beacon_in_range(range, beacon):
    for x in range:
        if beacon > x[0] and beacon < x[1]:
            return 1
    return 0

def range_merger(test_tuple, range_tuples):
    counter = 0
    test_merge = False
    range = [test_tuple[0], test_tuple[1]]
    while counter < len(range_tuples):
        if ((test_tuple[0] <= range_tuples[counter][1] and test_tuple[1] >= range_tuples[counter][0]) or
            (range_tuples[counter][0] <= test_tuple[1] and range_tuples[counter][1] >= test_tuple[0])):
            test_merge = True
            range.append(range_tuples[counter][0])
            range.append(range_tuples[counter][1])
            range.sort()
            range_tuples[counter] = (range[0], range[len(range)-1])
            while counter < len(range_tuples):
                if counter + 1 < len(range_tuples) and range_tuples[counter][1] >= range_tuples[counter + 1][0]:
                    merge = range_tuples.pop(counter + 1)
                    range.append(merge[0])
                    range.append(merge[1])
                    range.sort()
                    range_tuples[counter] = (range[0], range[len(range)-1])
                    continue
                else:
                    counter += 1
        counter += 1
    if not test_merge:
        range_tuples.append(test_tuple)
    range_tuples.sort()
    return range_tuples

    
full_list = open("problems/day15.txt").read().split("\n")

def part1():
    beacons_at_column = []
    y=2000000
    # y=10
    range_tuples = []
    for x in full_list:
        sensor = Sensor(x)
        test_tuple = sensor.signal_at_y(y)
        if test_tuple == None:
            continue    
        if len(range_tuples) == 0:
            range_tuples.append(test_tuple)
        else:
            range_tuples = range_merger(test_tuple, range_tuples)   
        beacon = sensor.beacon_at_y(y)
        if beacon != None and beacon not in beacons_at_column:
            beacons_at_column.append(beacon)
    
    beacons_in = 0
    for beacon in beacons_at_column:
            beacons_in += beacon_in_range(range_tuples, beacon[0])
    
    final_count = 0
    for test_tuple in range_tuples:
        final_count += test_tuple[1] - test_tuple[0] + 1
    print(final_count - beacons_in)


def part2():
    max = 4000000
    # max = 20
    min = 0
    # counter = 0
    counter = 1260725
    while counter < max:
        range_tuples = []
        for x in full_list:     
            sensor = Sensor(x)
            test_tuple = sensor.signal_at_y(counter)
            if test_tuple == None:
                continue
            if test_tuple[1] < min:
                continue
            if test_tuple[0] > max:
                continue
            if test_tuple[0] < min:
                test_tuple = (min, test_tuple[1])
            if test_tuple[1] > max:
                test_tuple = (test_tuple[0], max)
            if len(range_tuples) == 0:
                range_tuples.append(test_tuple)
            else:
                range_tuples = range_merger(test_tuple, range_tuples)
                
        if len(range_tuples) > 1:
            return 4000000 * (range_tuples[0][1] + 1) + counter
        counter += 1
            
              
    
part1()
print(part2())