from typing import List


class RollingCounter:
    def __init__(self, n: int):
        self.n = n
        self.counter = [0] * n

    def printCurrentState(self):
        pass

    def rollCondition(self):
        pass

    def enumerate(self):
        counter_pointer = 0
        while counter_pointer < self.n:
            self.printCurrentState()
            counter_pointer = 0
            while counter_pointer < self.n:
                self.counter[counter_pointer] += 1
                if self.rollCondition():
                    self.counter[counter_pointer] = 0
                else:
                    break
                counter_pointer += 1

class CountingPennies(RollingCounter):
    def __init__(self, values: List[int], denominations: List[str], target: int):
        super(CountingPennies, self).__init__(len(values))
        self.values = values
        self.target = target
        self.denominations = denominations

    def rollCondition(self):
        return self.getValues() > self.target

    def printCurrentState(self):
        print(' '.join([str(self.target - self.getValues()) + ' Pennies'] +
                       [str(self.counter[i]) + ' ' + self.denominations[i] for i in range(self.n)]))

    def getValues(self):
        return sum([self.values[i] * self.counter[i] for i in range(self.n)])

# tester = CountingPennies([25, 100], ["Quarters", "Dollars"], 200)
tester= CountingPennies([5, 10, 25, 100], ["Nickles", "Dimes", "Quarters", "Dollars"], 200)
tester.enumerate()