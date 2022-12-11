import re

monkey_list = open("problems/day11.txt").read().split("\n\n")

class Monkey():
    def __init__(self, monkey) -> None:
        self.number = re.search("Monkey (\d+)", monkey).group(1)
        # items = self.get_list(monkey)
        self.items =  re.search("Starting items: (.+)", monkey).group(1).split(", ")
        self.operation = re.search("Operation: new = (.+) (.) (.+)", monkey).groups()
        self.test = int(re.search("Test: divisible by (.+)", monkey).group(1))
        self.true_to = int(re.search("If true: throw to monkey (.+)", monkey).group(1))
        self.false_to = int(re.search("If false: throw to monkey (.+)", monkey).group(1))
        self.inspected = 0
    
    def run_operation(self, monkeys, worry):
        pass
        while len(self.items) > 0:
            x = 0
            y = 0
            old = int(self.items.pop())
            self.inspected += 1
            if self.operation[0] == "old":
                x = old
            else:
                x = int(self.operation[0])
            if self.operation[2] == "old":
                y = old
            else:
                y = int(self.operation[2])
            if self.operation[1] == "*":
                old = int((x*y) % worry)
            if self.operation[1] == "+":
                old = int((x+y) % worry)

        
            self.throw(monkeys, old)
        
    def throw(self, monkeys, old):
        test = old % self.test
        if test == 0:
            monkeys[self.true_to].catch(old)
        else:
            monkeys[self.false_to].catch(old)
    
    def catch(self, value):
        self.items.append(value)
        
    def return_inspected(self):
        return self.inspected
    
    def return_test(self):
        return self.test

    def print_list(self):
        print(self.items)
   
  
def part1():
    monkeys = []
    worry = 3
    for monkey in monkey_list:
        monkeys.append(Monkey(monkey))
    monkey_business(monkeys, worry, 20)


def part2():
    monkeys = []
    worry = 1
    counter = 0
    for monkey in monkey_list:
        monkeys.append(Monkey(monkey))
        worry *= monkeys[counter].return_test()
        counter += 1
    monkey_business(monkeys, worry, 10000)


def monkey_business(monkeys, worry, loops):
    counter = 0
    while counter < loops:
        for monkey in monkeys:
            monkey.run_operation(monkeys, worry)
        counter += 1
            
    first = 0
    second = 0
    for monkey in monkeys:
        inspected = monkey.return_inspected()
        if inspected > first:
            second = first
            first = inspected
        elif inspected > second:
            second = inspected
    print(first * second)

part1()
part2()