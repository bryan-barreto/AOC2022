import re

full_list = open("problems/day16ex.txt").read().split("\n")
max_flow = 0
TIMER = 30

class Valve():
    def __init__(self, input) -> None:
        global max_flow
        self.valve = re.search("Valve (.+) has", input).group(1)
        self.flow_rate = int(re.search("has flow rate=(.+);", input).group(1))
        self.tunnels_to = re.search("tunnels? leads? to valves? (.+)", input).group(1).split(", ") 
        max_flow += self.flow_rate
        
    def __eq__ (self, other):
        return self.valve == other

def move(valves, current_room, current_timer, flow_rate, turned_valves, best_route):
    if current_timer > TIMER:
        pass
    current_timer += 1
    if flow_rate < max_flow:
        for room in valves[valves.index(current_room)].tunnels_to:
            first_route = best_route.copy()
            second_route = best_route.copy()
            first_route.append(turn(valves, room, current_timer, flow_rate, turned_valves.copy(), best_route=best_route))
            second_route.append(move(valves, room, current_timer, flow_rate, turned_valves.copy(), best_route=best_route))
            
    else:
        move(valves, current_room, current_timer, flow_rate, turned_valves.copy(), best_route=best_route)
                 

def turn(valves, current_room, current_timer, flow_rate, turned_valves, best_route):
    if current_timer > TIMER:
        pass
    current_timer += 1
    score += flow_rate * (TIMER - current_timer)
    current_valve = valves[valves.index(current_room)]
    if current_room not in turned_valves and current_valve.flow_rate != 0:  
        flow_rate += current_valve.flow_rate
        turned_valves.append(current_room)
    move(valves, current_room, current_timer, flow_rate, turned_valves.copy(), best_route=best_route)

def part1(): 
    valves = []
    best_route = []

    while len(full_list) > 0:
        valves.append(Valve(full_list.pop(0)))
        
    best_route.append(move(valves=valves, current_room='AA', current_timer=0, flow_rate=0, turned_valves=[], best_route=best_route))
    

part1()