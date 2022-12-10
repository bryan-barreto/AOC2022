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

def draw(loop, x):
    to_append = ""
    loop = (loop % 40)
    # if loop == 0:
    #     loop = 40
    test = x-loop
    if test >= -2 and test <= 0:
        to_append += "#" 
    else:
        to_append += "."
    
    if loop% 40 == 0 :
        to_append += "\n"
    return to_append
    
    
        
strength = 0
loop = 0
x = 1
crt = ""
for cycle in circuit:
    cycle = cycle.split()
    if cycle[0] == "noop":
        loop += 1
        crt += draw(loop, x)
        strength += check_signal(loop, x)
    if cycle[0] == "addx":
        counter = 0
        while counter < 2:
            loop += 1
            crt += draw(loop, x)
            counter += 1 
            strength += check_signal(loop, x)
        x += int(cycle[1])
print(crt)
print(strength)

        