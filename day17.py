rocks_list = open("problems/day17rocks.txt").read().split("\n\n")
move_list = open("problems/day17ex.txt").read()

class Rock():
    def __init__(self, input) -> None:
        self.image = input
        self.height = 0
        self.shape = self.setshape(input)
        self.pos = []
        
    def __repr__(self) -> str:
        return f"{self.image}"
    
    def setshape(self, input):
        toreturn = []
        y = 0
        input = input.split("\n")
        self.height = len(input)
        for horiz in input:
            x = 0
            for vert in horiz:
                if vert != '#':
                    x += 1
                    continue
                toreturn.append((x,y))
                x += 1
            y -= 1
        return toreturn

    def canfall(self, grid):
        for part in self.pos:
            test = (part[0], part[1] - 1)
            if test in grid or test[1] <= 0:
                return False
        return True
    
    def draw(self, height):
        self.pos = []
        for segment in self.shape:
            self.pos.append((segment[0], segment[1] + self.height + height + 3 ))
            
    def moveleft(self, grid):
        for test in self.pos:
            if test[0] <= -2 or (test[0] - 1, test[1]) in grid:
                return
        counter = 0
        while counter < len(self.pos):
            shift = self.pos.pop(0)
            shift = (shift[0] - 1, shift[1])
            self.pos.append(shift)
            counter += 1
    
    def moveright(self, grid):
        for test in self.pos:
            if test[0] >= 4 or (test[0] + 1, test[1]) in grid:  
                return
        counter = 0
        while counter < len(self.pos):
            shift = self.pos.pop(0)
            shift = (shift[0] + 1, shift[1])
            self.pos.append(shift)
            counter += 1
        
    def movedown(self):
        counter = 0
        while counter < len(self.pos):
            shift = self.pos.pop(0)
            shift = (shift[0], shift[1] - 1)
            self.pos.append(shift)
            counter += 1
                     
    def rest(self):
        return self.pos
    
    def full_shift(self, old_height, new_height):
        new_pos = []
        for x in self.pos:
            difference = old_height - x[1]
            new_pos.append((x[0], new_height + difference))
        self.pos = new_pos


def find_visible(list, height):
    test_height = height + 1
    return_list = []
    past = []
    fringe = [(0, test_height)]
    while len(fringe) > 0:
        test_loc = fringe.pop()
        past.append(test_loc)
        for x in (1,0), (0,-1), (-1,0):
            new_loc = (test_loc[0] + x[0], test_loc[1] + x[1])
            if new_loc[0] < -2 or new_loc[0] > 4:
                continue
            if (new_loc not in list and 
                new_loc not in fringe and 
                new_loc not in past):
                fringe.append(new_loc)
            elif new_loc in list:
                return_list.append(new_loc)
    return return_list

rocks = []       
for part in rocks_list:
    rocks.append(Rock(part))

def play(drops):
    grid = []
    height = 0
    first_height = 0
    counter = 0
    total_counter = 0
    rock = 0
    wind_loops = 0
    while rock < drops:
        current_rock = rocks[rock%5]
        current_rock.draw(height)
        loop = True
        rock += 1
        while loop: 
            move = move_list[counter]
            if move == '<':
                current_rock.moveleft(grid)
            else:
                current_rock.moveright(grid)
            counter += 1
            total_counter += 1
            # if total_counter % 1_000_000 == 0:
            #     print(float(total_counter / drops))
            if counter == len(move_list):
                if wind_loops == 1:
                    last_height = height - first_height
                    last_rocks = rock - first_rocks
                    multi = int(drops/last_rocks) - 1
                    rock = drops - (drops%last_rocks)
                    visible = find_visible(grid, height)
                    visible.sort(key = lambda x : x[1], reverse=True)
                    new_height = first_height + (last_height * multi)
                    for x in visible:
                        difference = visible[0][1] - x[1]
                        grid.append((x[0], new_height - difference))
                    current_rock.full_shift(visible[0][1], new_height)
                    height = new_height 
                first_height = height
                first_rocks = rock

            
            if counter >= len(move_list):
                counter = 0
                
            if not current_rock.canfall(grid):
                setting = current_rock.rest()
                for rest in setting:
                    grid.append(rest)
                loop = False
                continue
            current_rock.movedown()

        grid.sort(key = lambda x : x[1], reverse=True)
        height = grid[0][1]
        while height > grid[len(grid) - 1][1] + 100:
            grid.pop()
        # if rock%5 == 0:
        #     if len(loop_heights) == 0:
        #         loop_heights.append((height, total_counter))
        #     else:
        #         for x in loop_heights:
        #             if height % x[0] == 0:
        #                 return (drops/x[1]) * x[0]
        #         loop_heights.append((height, total_counter))
        
    return height

print(play(1_000_000_000_000))