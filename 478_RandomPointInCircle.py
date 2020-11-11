"""
Given the radius and x-y positions of the center of a circle, write a function randPoint which generates a uniform
random point in the circle.

Note:
- input and output values are in floating-point.
- radius and x-y position of the center of the circle is passed into the class constructor.
- a point on the circumference of the circle is considered to be in the circle.
- randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.
"""
from math import sqrt, sin, cos, pi
from random import random
from typing import List


class RandomPointCircle:
    def __init__(self, radius: float, x_center: float, y_center: float):
        """
        Circle of radius centered at (x_center, y_center)
        """
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def random_point(self) -> List[float]:
        """
        Polar coordinates
        :return: [x, y] randomly selected within the circle
        """
        distance = sqrt(random()) * self.radius
        degree = random() * 2 * pi
        return [self.x_center + distance * cos(degree),
                self.y_center + distance * sin(degree)]


test_x_center, test_y_center = random() * 10 + 10, random() * 5 + 10
test_radius = 5
N = 500
x_list, y_list = [0] * N, [0] * N

circle = RandomPointCircle(radius=test_radius, x_center=test_x_center, y_center=test_y_center)
for i in range(N):
    x, y = circle.random_point()
    assert (x - test_x_center) * (x - test_x_center) + (y - test_y_center) * (y - test_y_center) <= test_radius ** 2
    x_list[i], y_list[i] = x, y

"""
import matplotlib.pyplot as plt
plt.plot(x_list, y_list, 'x')
plt.show()
"""
