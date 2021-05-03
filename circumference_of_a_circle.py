#!/usr/bin/env python3
# Created by: Sam. Garcon
# Created on: april 2021
# This program calculates the circumference of a circle
# with user input

import math

radius = float(input("Enter the radius of the circle : "))

circumference = 2 * math.pi * radius

print("Circumference of the circle is : %.2f" % circumference)
