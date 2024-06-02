from turtle import *
import random


shape("turtle")
col = ["orange", "limegreen", "gold", "plum", "tomato"]
def line(a, b, c):
    for i in range(a):
        color(random.choice(col))
        forward(b)
        left(c)
    forward(b)


for i in range(5):
    line(25, 75, 75)

done()
