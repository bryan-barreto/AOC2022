import re

class Sensor():
    def __init__(self, input) -> None:
        hold = re.search("Sensor at x=(.+), y=(.+):", input).groups()
        self.position = (int(hold[0]), int(hold[1]))
        hold = re.search("closest beacon is at x=(.+), y=(.+)", input).groups()
        self.beacon = (int(hold[0]), int(hold[1]))
        self.distance = abs(self.position[0] - self.beacon[0]) + abs(self.position[1] - self.beacon[1])
        self.edge = []
    
    def find_edges(self):
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
        
full_list = open("problems/day15.txt").read().split("\n")


def beacon_in_range(range, beacon):
    for x in range:
        if beacon > x[0] and beacon < x[1]:
            return 1
    return 0
    

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
            counter = 0
            test_merge = False
            while counter < len(range_tuples):
                if ((test_tuple[0] <= range_tuples[counter][1] and test_tuple[1] >= range_tuples[counter][0]) or
                    (range_tuples[counter][0] <= test_tuple[1] and range_tuples[counter][1] >= test_tuple[0])):
                    test_merge = True
                    range = [test_tuple[0], test_tuple[1], range_tuples[counter][0], range_tuples[counter][1]]
                    range.sort()
                    range_tuples[counter] = (range[0], range.pop())
                    if counter + 1 < len(range_tuples):
                        if range_tuples[counter][1] > range_tuples[counter + 1][0]:
                            merge = range_tuples.pop(counter + 1)
                            range_tuples[counter] = (range_tuples[counter][0], merge[1])
                    counter = len(range_tuples)
                counter += 1
            if not test_merge:
                range_tuples.append(test_tuple)
            range_tuples.sort()
            
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
    
part1()