__author__ = 'hangui'
import math


class Solver:

    def calculate(self):
        while True:
            a = int(input("a "))
            b = int(input("b "))
            c = int(input("c "))
            d = b ** 2 - 4 * a * c
            if d>=0:
                dis = math.sqrt(d)
                root1 = (-b + dis) / (2 * a)
                root2 = (-b - dis) / (2 * a)
                print(root1, root2)
            else:
                print('error')
Solver().calculate()
