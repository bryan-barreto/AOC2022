import math
def testing_board_printout(h: tuple, h_move: str, snake: list, moves_processed: tuple = (), window_radius: int = 10) ->  None:
    """ Board printing visualization

    Parameters
    ----------
    h : tuple
        A tuple containing the (x, y) positions of the head of the rope
    h_move : str
        The command last executed upon the head of the rope
    snake : list
        A list whose size is the number of knots in the rope.
        Each element of the list contains a list of spaces the knot has visited.
        The final element in each knot should be the current position of the knot.
    moves_processed : tuple, optional
        A tuple containing (how many moves have been processed so far, total moves to process)
    window_radius : int, optional
        Represents the size of the view to be displayed, defaults to 10

    Author: https://github.com/dennis-lawter/
    """

    window_x_min: int = h[0] - window_radius
    window_x_max: int = h[0] + window_radius
    window_y_min: int = h[1] - window_radius
    window_y_max: int = h[1] + window_radius
    if moves_processed == ():
        moves_processed = "(all)"
    else:
        moves_processed = f"({moves_processed[0]} / {moves_processed[1]})"
    print(f"\n┌──╢   {h_move}   {moves_processed}   ╟".ljust((window_radius*4)+2,'─'), end="┐\n")
    for win_y in reversed(range(window_y_min, window_y_max)):
        print("│", end="")
        for win_x in range(window_x_min, window_x_max):
            test = (win_x, win_y)

            matched_snake = -1
            for i in range(0, len(snake)):
                if test == (snake[i][len(snake[i])-1][0], snake[i][len(snake[i])-1][1]):
                    matched_snake = i
                    break
            
            matched_footprint = False
            last_snake: list = snake[len(snake)-1]
            for i in range(0, len(last_snake)):
                if test == (last_snake[i][0], last_snake[i][1]):
                    matched_footprint = True
                    break

            if test == h:
                print("H ", end="")
            elif matched_snake != -1:
                # test == (snake[0][len(snake[0])-1][0], snake[0][len(snake[0])-1][1]):
                print(f"{matched_snake} ", end="")
            elif matched_footprint:
                print("░ ", end="")
            elif test == (0,0):
                print("╬═", end="")
            elif test[1] == 0:
                print("══", end="")
            elif test[0] == 0:
                print("║ ", end="")
            else:
                print(". ", end="")
        print("│")
    print("└" + ("──" * window_radius*2) + "┘")
#^^^^ Visual, not by me^^^^^



    
h_move_list = open("problems/day9.txt").read().split("\n")

def follow_tail(snake_len):
    h = (0,0)
    snake = []
    counter = 0
    while counter < snake_len:
        snake.append([(0,0)])
        counter +=1

    for h_move in h_move_list:
        x = h_move.split()
        h_dir = x[0]
        h_dis = int(x[1])
        match h_dir:
            case "L":
                h = (h[0] - h_dis,h[1])
            case "R":
                h = (h[0] + h_dis,h[1])
            case "U": 
                h = (h[0],h[1]+ h_dis)
            case "D":
                h = (h[0],h[1]- h_dis)

        not_caught = snake_len
        test = h
        front = h
        counter = 0
        if h_move == "R 17":
            pass
        while not_caught > 0:  
            t = snake[counter][len(snake[counter])-1]
            dis = math.sqrt((test[0]-t[0])*(test[0]-t[0]) + (test[1]-t[1])*(test[1]-t[1]))
            if dis > math.sqrt(2):
                if test[0]> t[0]:
                    t = (t[0] + 1,t[1])
                if test[0]< t[0]:
                    t = (t[0] - 1,t[1])
                if test[1] > t[1]:
                    t = (t[0], t[1] + 1)
                if test[1] < t[1]:
                    t = (t[0], t[1] - 1)
                if not snake[counter].__contains__(t):
                    snake[counter].append(t)
                else:
                    hold = snake[counter][snake[counter].index(t)]
                    snake[counter][snake[counter].index(t)] = snake[counter][len(snake[counter])-1]
                    snake[counter][len(snake[counter])-1] = hold
                    
                if snake_len - not_caught == counter:
                    front_dis = math.sqrt((front[0]-t[0])*(front[0]-t[0]) + (front[1]-t[1])*(front[1]-t[1]))
                    if front_dis <= math.sqrt(2):
                        front = t
                        not_caught -= 1
                        counter = snake_len - not_caught
                        test = t
                        continue

                test = t
                counter += 1
                
                if counter >= snake_len:
                    test = h
                    counter = 0
            elif counter < not_caught and counter > 0:
                test = h
                counter = 0
            else:
                not_caught -= 1

    return len(snake[snake_len - 1])


print(follow_tail(1))
print(follow_tail(9))
