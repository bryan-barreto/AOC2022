import functools

distress_signal = open("problems/day13.txt").read().split("\n\n")
sorting_list = distress_signal.copy()

def array_layer(list):
    return_array = []
    number_string = ""
    while len(list) > 0:
        list = list[1:]
        char = list[:1]  
        if char == '[':
            if len(number_string) > 0:
                return_array.append(int(number_string))
                number_string = ""
            return_list = array_layer(list)
            list = return_list[0]
            return_array.append(return_list[1])
        elif char == ",":
            if len(number_string) > 0:
                return_array.append(int(number_string))
                number_string = ""
            continue
        elif char == "]":
            if len(number_string) > 0:
                return_array.append(int(number_string))
                number_string = ""
            return [list,return_array]
        else:
            number_string += char


def cmp(left,right):
    counter = 0
    while 1 > 0:
        if len(left) <= counter and len(right) <= counter:
            return 0
        if len(left) <= counter:
            return -1
        if len(right) <= counter:
            return 1
        x = left[counter]
        y = right[counter]
        if type(x) == list or type(y) == list:
            if type(y) != list:
                y = [y]
            if type(x) != list:
                x = [x]
            check = cmp(x,y)
            if check == 0:
                counter += 1
                continue
            else:
                return check
        if x < y:
            return -1
        elif x > y:
            return 1
        counter += 1


def part1():
    correct_order = 0
    pair = 0
    for line in distress_signal:
        pair += 1
        left, right = line.split("\n")
        left = array_layer(left)[1]
        right = array_layer(right)[1]
        if cmp(left,right) <= 0:
            correct_order += pair
    print(correct_order)

def part2():
    full_list = [[[2]],[[6]]]
    for line in sorting_list:
        one, two = line.split()
        full_list.append(array_layer(one)[1])
        full_list.append(array_layer(two)[1])
    full_list = sorted(full_list,key = functools.cmp_to_key(cmp))
    print((full_list.index([[2]])+1) * (full_list.index([[6]])+1))
        
        
part1()
part2()