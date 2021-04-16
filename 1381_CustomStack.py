class CustomStack:
    EMPTY_STACK: int = -1

    def __init__(self, max_size: int):
        """
        CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the
        stack or do nothing if the stack reached the maxSize.

        :param max_size: maximum number of elements in the stack
        """
        self.top_pointer = -1
        self.initial_value = [0] * max_size
        # Lazy increment
        # upon pop(), stack[0], ..., stack[i] all needs to add self.increment_value[i] at pop()
        self.increment_value = [0] * max_size
        self.max_size = max_size

    def push(self, x: int) -> None:
        """
        :param x: adds x to the top of the stack if the stack hasn't reached the maxSize.
        """
        if self.top_pointer < self.max_size - 1:
            self.top_pointer += 1
            self.initial_value[self.top_pointer] = x
            self.increment_value[self.top_pointer] = 0

    def pop(self) -> int:
        """
        :return: pops and returns the top of stack or -1 if the stack is empty.
        """
        if self.top_pointer >= 0:
            i_inc = self.increment_value[self.top_pointer]
            if self.top_pointer > 0 and i_inc != 0:
                self.increment_value[self.top_pointer - 1] += i_inc
            self.top_pointer -= 1
            return self.initial_value[self.top_pointer + 1] + i_inc
        return CustomStack.EMPTY_STACK

    def increment(self, k: int, val: int) -> None:
        """
        Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, just
        increment all the elements in the stack.
        """
        if self.top_pointer >= 0:
            self.increment_value[min(k - 1, self.top_pointer)] += val


customStack = CustomStack(3)  # Stack is Empty []
customStack.push(1)  # stack becomes [1]
customStack.push(2)  # stack becomes [1, 2]
assert customStack.pop() == 2  # return 2 --> Return top of the stack 2, stack becomes [1]
customStack.push(2)  # stack becomes [1, 2]
customStack.push(3)  # stack becomes [1, 2, 3]
customStack.push(4)  # stack still [1, 2, 3], Don't add another elements as size is 4
customStack.increment(5, 100)  # stack becomes [101, 102, 103]
customStack.increment(2, 100)  # stack becomes [201, 202, 103]
assert customStack.pop() == 103  # return 103 --> Return top of the stack 103, stack becomes [201, 202]
assert customStack.pop() == 202  # return 202 --> Return top of the stack 102, stack becomes [201]
assert customStack.pop() == 201  # return 201 --> Return top of the stack 101, stack becomes []
assert customStack.pop() == customStack.EMPTY_STACK  # return -1 --> Stack is empty return -1
