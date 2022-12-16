import re

class Sensor():
    def __init__(self, input) -> None:
        hold = re.search("Sensor at x=(.+), y=(.+):", input).groups()
        self.position = (int(hold[0]), int(hold[1]))
        hold = re.search("closest beacon is at x=(.+), y=(.+)", input).groups()
        self.beacon = (int(hold[0]), int(hold[1]))
        self.distance = abs(self.position[0] - self.beacon[0]) + abs(self.position[1] - self.beacon[1])
        self.edge = [self.position]
        self.full_signal = []
    
    def find_beacon(self):
        hold = []
        beacon_reached = False
        while not beacon_reached:
            while len(self.edge) > 0:
                x = self.edge.pop(0)
                self.full_signal.append(x)
                for test in (-1,0),(1,0),(0,-1),(0,1):
                    test = (test[0] + x[0], test[1] + x[1])
                    if test in hold or test in self.edge or test in self.full_signal:
                        continue
                    if test == self.beacon:
                        beacon_reached = True
                    hold.append(test)
            self.edge = hold
        self.edge = []
    
    def beacon_at_y(self, y):
        if self.beacon[1] == y:
            return self.beacon
        return None
    
    def return_column(self, y):
        hold = []
        for x in self.full_signal:
            if x[1] == y:
                hold.append(x)
        return hold
        
full_list = open("problems/day15.txt").read().split("\n")

def part1():
    sensor_list = []
    for x in full_list:
        sensor = Sensor(x)
        sensor.find_beacon()
        sensor_list.append(sensor)
    column = []
    beacons_at_column = []
    y=2000000
    for x in sensor_list:
        column_array = x.return_column(y)   
        for move in column_array:
            if move not in column:
                column.append(move)
        beacon = x.beacon_at_y(y)
        if beacon != None:
            beacons_at_column.append(beacon)
    print(len(column) - len(beacons_at_column))
    
part1()