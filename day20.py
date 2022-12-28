full_list = open("problems/day20.txt").read().split()

class Coord():
    def __init__(self, value, pos) -> None:
        self.value = value * 811589153
        self.pos = pos
        
    def __repr__(self) -> str:
        return f"{self.value}"
    
    def get_pos(self):
        return self.pos
    
    def get_value(self):
        return self.value
 

def find_zero(coord_list):
    test_count = 0
    for x in coord_list:
        if x.get_value() == 0:
            return test_count
        test_count += 1
   
counter = 0
coord_list = []
for x in full_list:
    coord_list.append(Coord(int(x), counter))
    counter += 1

rounds = 0
while rounds < 10:    
    counter = 0
    while counter < len(coord_list):
        for x in coord_list:
            if counter != x.get_pos():
                continue
            move = x.get_value() % (len(coord_list) - 1)
            while move <= -len(coord_list) + coord_list.index(x):
                move += len(coord_list) - 1
            while move >= len(coord_list) - coord_list.index(x):
                move -= len(coord_list) - 1
            # if coord_list.index(x) + move == 0:
            #     coord_list.insert(len(coord_list) - 1, coord_list.pop(coord_list.index(x)))
            # else:
            coord_list.insert(coord_list.index(x) + move, coord_list.pop(coord_list.index(x)))
            counter += 1      
    rounds += 1
    
zero_pos = find_zero(coord_list)
counter = 1
final = 0
while counter <=3:
    pos = (counter * 1000) + zero_pos
    while pos > len(coord_list):
        pos -= len(coord_list)
    final += coord_list[pos].get_value()
    counter += 1
print(final)