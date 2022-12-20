import re

full_list = open("problems/day16ex.txt").read().split("\n")

class Valve():
    def __init__(self, input) -> None:
        self.valve = re.search("Valve (.+) has", input).group(1)
        self.flow_rate = int(re.search("has flow rate=(.+);", input).group(1))
        self.tunnels_to = re.search("tunnels? leads? to valves? (.+)", input).group(1).split(", ") 
        self.counter = None

    def connections(self):
        return self.tunnels_to
    
    def turn_valve(self, counter):
        counter -= 1
        self.counter = counter
        return self.flow_rate * counter
    
    def valve_on(self):
        self.flow_rate = 0

    def check_valve(self):
        return self.valve

    def get_counter(self):
        return self.counter

def next_valve(valve_list, current_valve):
    for x in valve_list:
        if current_valve == x.check_valve():
            return x 
    

def part1():
    counter = 30
    current_valve = "AA"
    valve_list = []
    for x in full_list:
        valve_list.append(Valve(x))
    temp_valve = next_valve(valve_list, current_valve)

    hueristics = [(current_valve, temp_valve.turn_valve(counter))]
    visiting = temp_valve.connections()
    visited = [temp_valve.check_valve()]
    
    final_list = []

    while counter > 0:
        while len(hueristics) < len(valve_list):
            counter -= 1
            loops = len(visiting)
            if loops == 0:
                break
            while loops > 0:
                loops -=1
                current_valve = visiting.pop(0)
                visited.append(current_valve)
                temp_valve = next_valve(valve_list, current_valve)
                temp_hueristics = (current_valve, temp_valve.turn_valve(counter))
                hueristics.append(temp_hueristics)
                hold_connections = temp_valve.connections()
                for x in hold_connections:
                    if x not in visiting and x not in visited:
                        visiting.append(x)
                    
        hueristics.sort(key = lambda x : x[1])
        to_add = hueristics.pop()
        if to_add[1] == 0:
            to_return = 0
            for x in final_list:
                to_return += x[1]
            return to_return
        final_list.append(to_add)
        current_valve = to_add[0]
        temp_valve = next_valve(valve_list, current_valve)
        counter = temp_valve.get_counter()
        temp_valve.valve_on()
        hueristics = [(current_valve, temp_valve.turn_valve(0))]
        visiting = temp_valve.connections()
        visited = [temp_valve.check_valve()]

    
    to_return = 0
    for x in final_list:
        to_return += x[1]
    return to_return

print(part1())