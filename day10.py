circuit = open("problems/day10.txt").read().split("\n")


def check_signal(loop, x):
    if (loop == 20 or
    loop == 60 or
    loop == 100 or
    loop == 140 or
    loop == 180 or
    loop == 220):
        return (loop * x)
    return 0

def draw(inner_loop, inner_x):
    to_append = ""
    inner_loop = (inner_loop % 40)
    if inner_loop == 0:
        inner_loop = 40
    test = inner_x-inner_loop
    if test >= -1 and test <= 1:
        to_append += "#" 
    else:
        to_append += "."
    
    if inner_loop == 40:
        to_append += "\n"
    return to_append
    
    
        
strength = 0
loop = 0
x = 1
crt = ""
for cycle in circuit:
    cycle = cycle.split()
    if cycle[0] == "noop":
        crt += draw(loop, x)
        loop += 1
        strength += check_signal(loop, x)
    if cycle[0] == "addx":
        counter = 0
        while counter < 2:
            crt += draw(loop, x)
            loop += 1
            counter += 1 
            strength += check_signal(loop, x)
        x += int(cycle[1])
print(crt)
print(strength)

        