from typing import List


class RollingCounter:
    def __init__(self, n: int):
        """
        :param n: n units/levels
        """
        self.n = n
        self.counter = [0] * n
        self.has_next = True

    def print_current_state(self):
        pass

    def _roll_to_next_pointer(self):
        pass

    def enumerate(self):
        """
        enumerate through all remaining states of counters
        """
        while self.has_next:
            self.print_current_state()
            self.__next__()

    def __next__(self):
        counter_pointer = 0
        while counter_pointer < self.n:
            self.counter[counter_pointer] += 1
            if self._roll_to_next_pointer():
                self.counter[counter_pointer] = 0
                counter_pointer += 1
            else:
                break
        self.has_next = counter_pointer < self.n


class CountingPennies(RollingCounter):
    def __init__(self, values: List[int], denominations: List[str], target: int):
        super(CountingPennies, self).__init__(len(values))
        self.values = values
        self.target = target
        self.denominations = denominations

    def _roll_to_next_pointer(self):
        return self.get_values() > self.target

    def print_current_state(self):
        print(' '.join([str(self.target - self.get_values()) + ' Pennies'] +
                       [str(self.counter[i]) + ' ' + self.denominations[i] for i in range(self.n)]))

    def get_values(self):
        return sum([self.values[i] * self.counter[i] for i in range(self.n)])


# tester = CountingPennies([25, 100], ["Quarters", "Dollars"], 200)
tester = CountingPennies([5, 10, 25, 100], ["Nickles", "Dimes", "Quarters", "Dollars"], 200)
tester.enumerate()
