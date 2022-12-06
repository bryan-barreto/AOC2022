list = open("problems/day6.txt").read()


def findCounter(max):
    marker = ""
    counter = 0
    for x in list:
        counter += 1
        while x in marker:
            marker = marker[1:]
        marker += x
        if len(marker) > max:
            return counter 

print("Part 1:\t" + str(findCounter(3)))
print("Part 2:\t" + str(findCounter(13)))