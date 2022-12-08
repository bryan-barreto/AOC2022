grid_input = open("problems/day8.txt").read().split()

def check_visible(x, y):
    if (x == 0 or x == (len(grid_input[0]) - 1) or y == 0 or y == (len(grid_input) -1)):
        return 0
    left_check = False
    test_x = 0
    while test_x < x and not left_check:
        if int(grid_input[test_x][y]) >= int(grid_input[x][y]):
            left_check = True
            continue
        test_x += 1
        
    right_check = False
    test_x = len(grid_input[0]) - 1
    while test_x > x and not right_check:
        if int(grid_input[test_x][y]) >= int(grid_input[x][y]):
            right_check = True
            continue
        test_x -= 1
    
    top_check = False    
    test_y = 0
    while test_y < y and not top_check:
        if int(grid_input[x][test_y]) >= int(grid_input[x][y]):
            top_check = True
            continue
        test_y += 1
    
    bottom_check = False    
    test_y = len(grid_input) - 1
    while test_y > y and not bottom_check:
        if int(grid_input[x][test_y]) >= int(grid_input[x][y]):
            bottom_check = True
            continue
        test_y -= 1
    
    if left_check and right_check and top_check and bottom_check:
        return 1 
    return 0

def check_view(x, y):
    if (x == 0 or x == (len(grid_input[0]) - 1) or y == 0 or y == (len(grid_input) -1)):
        return 0
    left_check = 0
    test_x = x - 1
    while test_x > -1:
        if int(grid_input[test_x][y]) < int(grid_input[x][y]):
            left_check += 1
        else: 
            left_check += 1
            test_x = -1
            continue
        test_x -= 1
        
    right_check = 0
    test_x = x + 1
    while test_x != (len(grid_input[0])):
        if int(grid_input[test_x][y]) < int(grid_input[x][y]):
            right_check += 1
        else:
            right_check += 1
            test_x = (len(grid_input[0]))
            continue
        test_x += 1
    
    top_check = 0
    test_y = y - 1
    while test_y > -1:
        if int(grid_input[x][test_y]) < int(grid_input[x][y]):
            top_check += 1
        else: 
            top_check += 1
            test_y = -1
            continue
        test_y -= 1
    
    bottom_check = 0
    test_y = y + 1
    while test_y != (len(grid_input[0])):
        if int(grid_input[x][test_y]) < int(grid_input[x][y]):
            bottom_check += 1
        else:
            bottom_check += 1
            test_y = (len(grid_input))
            continue
        test_y += 1
    
    return right_check * left_check * top_check * bottom_check


invisible = 0
best_view = 0
best_loc = 0

pos_y = 0
while pos_y < len(grid_input):
    pos_x = 0
    while pos_x < len(grid_input[0]):
        invisible += check_visible(pos_x, pos_y) #part 1
        new_view = check_view(pos_x, pos_y) #part 2
        if new_view > best_view:
            best_view = new_view
            best_loc = (pos_x,pos_y)
        pos_x += 1
    pos_y += 1
for y in range(0, len(grid_input)):
    for x in range(0, len(grid_input[0])):
        if check_visible(x,y):
            print("　", end=" ")
        elif (x,y) == best_loc:
            print("🎅", end=" ")
        else:
            print("🎄", end=" ")
    print("")

print("Part 1:\t" + str((len(grid_input) * len(grid_input[0])) - invisible))    
#print(grid_input[best_loc[0]][best_loc[1]]) #best view location
print("Part 2:\t" + str(best_view))
