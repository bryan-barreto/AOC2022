import re

class Sensor():
    def __init__(self, input) -> None:
        hold = re.search("Sensor at x=(.+), y=(.+):", input).groups()
        self.position = (int(hold[0]), int(hold[1]))
        hold = re.search("closest beacon is at x=(.+), y=(.+)", input).groups()
        self.beacon = (int(hold[0]), int(hold[1]))
        self.distance = abs(self.position[0] - self.beacon[0]) + abs(self.position[1] - self.beacon[1])
        self.edge = []
    
    def find_beacon(self):
        hold = []
        counter = 0
        distance = self.distance
        while counter <= distance:
            hold.append((self.position[0] + counter, self.position[1] + distance))
            hold.append((self.position[0] + counter, self.position[1] - distance))
            hold.append((self.position[0] - counter, self.position[1] + distance))
            hold.append((self.position[0] - counter, self.position[1] - distance))
            hold.append((self.position[0] + distance, self.position[1] + counter))
            hold.append((self.position[0] + distance, self.position[1] - counter))
            hold.append((self.position[0] - distance, self.position[1] + counter))
            hold.append((self.position[0] - distance, self.position[1] - counter))
            counter += 1
            distance -= 1
        hold.sort()
        for x in hold:
            if x not in self.edge:
                self.edge.append(x)
        # hold = self.full_signal.copy()
        # while len(hold) > 1:
        #     val1 = hold.pop(0)
        #     if val1[0] != hold[0][0]:
        #         continue
        #     val2 = hold.pop(0)
        #     between = abs(val1[1] - val2[1]) - 1
        #     while between > 0:
        #         self.full_signal.append((val1[0], val1[1] + between))
        #         between -= 1
                

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
        
full_list = open("problems/day15ex.txt").read().split("\n")

def part1():
    sensor_list = []
    for x in full_list:
        sensor = Sensor(x)
        sensor.find_beacon()
        sensor_list.append(sensor)
    column = []
    beacons_at_column = []
    # y=2000000
    y=10
    for x in sensor_list:
        column_array = x.return_column(y)   
        for move in column_array:
            if move not in column:
                column.append(move)
        beacon = x.beacon_at_y(y)
        if beacon != None and beacon not in beacons_at_column:
            beacons_at_column.append(beacon)
    print(len(column) - len(beacons_at_column))
    
part1()