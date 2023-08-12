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

def move(valves, current_room, current_timer, flow_rate, score, turned_valves, highest_score):
    if current_timer > TIMER:
        if score > highest_score:
            return score
        else:
            return highest_score
    current_timer += 1
    if flow_rate < max_flow:
        compare_score = []
        for room in valves[valves.index(current_room)].tunnels_to:
            if room not in turned_valves and valves[valves.index(room)].flow_rate != 0:
                compare_score.append(turn(valves, room, current_timer, flow_rate, score, turned_valves.copy(), highest_score))
            compare_score.append(move(valves, room, current_timer, flow_rate, score, turned_valves.copy(), highest_score))
        return max(compare_score)
    else: 
        return move(valves, current_room, TIMER + 1, flow_rate, score, turned_valves.copy(), highest_score)
                 

def turn(valves, current_room, current_timer, flow_rate, score, turned_valves, highest_score):
    if current_timer > TIMER:
        if score > highest_score:
            return score
        else:
            return highest_score
    current_timer += 1
    current_valve = valves[valves.index(current_room)]
    score += current_valve.flow_rate * (TIMER - current_timer)
    flow_rate += current_valve.flow_rate
    turned_valves.append(current_room)
    return move(valves, current_room, current_timer, flow_rate, score, turned_valves.copy(), highest_score)

def part1(): 
    valves = []
    turned_valves = []
    
    while len(full_list) > 0:
        valves.append(Valve(full_list.pop(0)))
        
    highest_score = move(valves=valves, current_room='AA', current_timer=0, flow_rate=0, score=0, turned_valves=turned_valves, highest_score=0)
    
    print(highest_score)      
part1()