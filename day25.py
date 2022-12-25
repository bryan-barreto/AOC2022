import math

snafu_list = open("problems/day25ex.txt").read().split()

full_snafu_conversion = 0

for x in snafu_list:
    snafu_value = 0
    pos = len(x) - 1
    for y in x:
        variable = 5**pos
        pos -= 1
        if y == '=':
            variable *= -2
        elif y == '-':
            variable *= -1
        else:
            variable *= int(y)
        snafu_value += variable
    full_snafu_conversion += snafu_value

while 1 > 0:
    print(full_snafu_conversion%5)
    full_snafu_conversion = int(full_snafu_conversion/5)