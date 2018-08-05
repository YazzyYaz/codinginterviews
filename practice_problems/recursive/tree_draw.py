import turtle
import random

def tree(branch_len, t, p):
    if branch_len > 5:
        if branch_len <= 10:
            t.color("green")
        t.forward(branch_len)
        t.pensize(p)
        p -= 1
        t.right(random.randint(1, 20))
        tree(branch_len-10, t, p)
        t.left(random.randint(1, 20))
        tree(branch_len-10, t, p)
        t.right(random.randint(1, 20))
        t.backward(branch_len)

def main():
    t = turtle.Turtle()
    my_window = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(300)
    t.down()
    t.color("brown")
    t.pensize(10)
    tree(100, t, 9)
    my_window.exitonclick()

main()
