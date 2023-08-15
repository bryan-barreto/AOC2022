import re

full_list = open("problems/day16ex.txt").read().split("\n")
max_flow = 0
TIMER = 30
#GOAL: Compare all valves to their potential output and determine which is the best valve to head to next
class Valve():
    def __init__(self, input) -> None:
        global max_flow
        self.valve = re.search("Valve (.+) has", input).group(1)
        self.flow_rate = int(re.search("has flow rate=(.+);", input).group(1))
        self.tunnels_to = re.search("tunnels? leads? to valves? (.+)", input).group(1).split(", ") 
        max_flow += self.flow_rate
        self.ranges = {}
        
    def __eq__ (self, other):
        return self.valve == other
    
    def find_ranges(self, valves):
        check_again = []
        self.ranges[self.valve] = 0
        for valve in valves:
            valve = valve.valve
            if valve not in self.ranges:
                returned_value = self.find_range(valve, valves, 0)
                if isinstance(returned_value, int):
                    self.ranges[valve] = returned_value
                else:
                    check_again.append(returned_value)
        if len(check_again) is not 0:
            self.find_ranges(valves)
    
    def find_range(self, valve, valves, counter):
        counter += 1
        if valve not in self.tunnels_to:
            next_valve_array = valves[valves.index(valve)].tunnels_to
            for next_valve in next_valve_array:
                test_range = self.ranges.keys()
                if next_valve in test_range:
                    return counter + self.ranges[next_valve]
            return valve    
        return counter
        
    
# def determine_values(all_valves, turned_valves):
#     for check_valve in all_valves:
#         if check_valve not in turned_valves:
            

# def move(valves, current_room, current_timer, flow_rate, score, turned_valves, highest_score):
#     if current_timer > TIMER:
#         if score > highest_score:
#             return score
#         else:
#             return highest_score
#     current_timer += 1
#     if flow_rate < max_flow:
#         compare_score = []
#         for room in valves[valves.index(current_room)].tunnels_to:
#             if room not in turned_valves and valves[valves.index(room)].flow_rate != 0:
#                 compare_score.append(turn(valves, room, current_timer, flow_rate, score, turned_valves.copy(), highest_score))
#             compare_score.append(move(valves, room, current_timer, flow_rate, score, turned_valves.copy(), highest_score))
#         return max(compare_score)
#     else: 
#         return move(valves, current_room, TIMER + 1, flow_rate, score, turned_valves.copy(), highest_score)
                 

# def turn(valves, current_room, current_timer, flow_rate, score, turned_valves, highest_score):
#     if current_timer > TIMER:
#         if score > highest_score:
#             return score
#         else:
#             return highest_score
#     current_timer += 1
#     current_valve = valves[valves.index(current_room)]
#     score += current_valve.flow_rate * (TIMER - current_timer)
#     flow_rate += current_valve.flow_rate
#     turned_valves.append(current_room)
#     return move(valves, current_room, current_timer, flow_rate, score, turned_valves.copy(), highest_score)

def part1(): 
    all_valves = []
    turned_valves = []
    
    while len(full_list) > 0:
        all_valves.append(Valve(full_list.pop(0)))

    for valve in all_valves:
        valve.find_ranges(all_valves)
    
    
    
part1()