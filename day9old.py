import math

h_move_list = open("problems/day9ex2.txt").read().split("\n")
h = (0,0)
t = (0,0)
t_past = [(0,0)]

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

    dis = math.sqrt((h[0]-t[0])*(h[0]-t[0]) + (h[1]-t[1])*(h[1]-t[1]))
    while dis > math.sqrt(2) + 0.001: # prevent any random roud=
        if h[0]> t[0]:
            t = (t[0] + 1,t[1])
        if h[0]< t[0]:
            t = (t[0] - 1,t[1])
        if h[1] > t[1]:
            t = (t[0], t[1] + 1)
        if h[1] < t[1]:
            t = (t[0], t[1] - 1)
        if not t_past.__contains__(t):
            t_past.append(t)
        dis = math.sqrt((h[0]-t[0])*(h[0]-t[0]) + (h[1]-t[1])*(h[1]-t[1]))
print(t_past)
print(len(t_past))