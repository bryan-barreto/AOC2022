import math

h_move_list = open("problems/day9ex2.txt").read().split("\n")

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
        while not_caught > 0:
            test = h
            t = snake[snake_len - not_caught][len(snake[snake_len - not_caught])-1]
            dis = math.sqrt((test[0]-t[0])*(test[0]-t[0]) + (test[1]-t[1])*(test[1]-t[1]))
            counter = 0
            while counter < not_caught:
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
                dis = math.sqrt((test[0]-t[0])*(test[0]-t[0]) + (test[1]-t[1])*(test[1]-t[1]))
                test = snake[counter][len(snake[counter])-1]
                if dis <= math.sqrt(2) + 0.1: # prevent any weird rounding error
                    counter += 1
            not_caught -= 1
    return len(snake[snake_len - 1])
print(follow_tail(1))
print(follow_tail(9))