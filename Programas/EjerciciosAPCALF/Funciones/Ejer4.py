from ctypes.wintypes import PINT
import math

def AreaCirculo(radius):
    pi = 3.1415
    return pi * radius**2

def volumenCilindo(radius,high):
    return AreaCirculo(radius)*high

print(volumenCilindo(3,5))