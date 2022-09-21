import turtle as trtl
from threading import Thread
from time import sleep

def make_stomach(daddy):
    #hot bod
    daddy.pu()
    daddy.sety(-100)
    daddy.pd()
    daddy.color("#FFE9D1")
    daddy.begin_fill()
    daddy.circle(150)
    daddy.end_fill()
    
    #belly button
    daddy.pu()
    daddy.sety(-80)
    daddy.pd()
    daddy.color('#e75480')
    daddy.begin_fill()
    daddy.circle(10)
    daddy.end_fill()
    
    daddy.pu()
    daddy.goto(-75, 75)
    daddy.pd()
    daddy.begin_fill()
    daddy.circle(15)
    daddy.end_fill()

    daddy.pu()
    daddy.goto(75, 75)
    daddy.pd()
    daddy.begin_fill()
    daddy.circle(15)
    daddy.end_fill()

    daddy.hideturtle()

def make_arms(daddy2):
    daddy2.color("#FFE9D1")
    daddy2.pu()
    daddy2.begin_fill()
    daddy2.goto(-150, 169)
    daddy2.pd()
    daddy2.goto(-255, 169)
    daddy2.goto(-255, -169)
    daddy2.goto(-150, -169)
    daddy2.goto(-150, 169)
    daddy2.end_fill()

    daddy2.pu()
    daddy2.begin_fill()
    daddy2.goto(150, 169)
    daddy2.pd()
    daddy2.goto(255, 169)
    daddy2.goto(255, -169)
    daddy2.goto(150, -169)
    daddy2.goto(150, 169)
    daddy2.end_fill()

    daddy2.hideturtle()
    
def make_head(daddy3):
    daddy3.pu()
    daddy3.goto(0, 200)
    daddy3.color("#FFE9D1")
    daddy3.begin_fill()
    daddy3.pd()
    daddy3.circle(50)
    daddy3.end_fill()
    daddy3.pu()
    
    #eyes
    daddy3.color("Black")
    daddy3.goto(-50, 250)
    daddy3.begin_fill()
    daddy3.pd()
    daddy3.circle(10)
    daddy3.end_fill()
    daddy3.pu()
    daddy3.goto(50, 250)
    daddy3.begin_fill()
    daddy3.pd()
    daddy3.circle(10)
    daddy3.end_fill()
    daddy3.pu()

    #sick beard
    daddy3.color("red")
    daddy3.goto(-100, 225)
    daddy3.begin_fill()
    daddy3.pd()
    daddy3.goto(100, 225)
    daddy3.goto(75, 175)
    daddy3.goto(50, 225)
    daddy3.goto(0, 125)
    daddy3.goto(-50, 225)
    daddy3.goto(-75, 175)
    daddy3.goto(-100, 225)
    daddy3.end_fill()
    daddy3.pu() 

    daddy3.hideturtle()

def make_pants(daddy4):
    daddy4.pu()
    daddy4.color("#00008b")
    daddy4.goto(-100, -75)
    daddy4.begin_fill()
    daddy4.pd()
    daddy4.goto(100, -75)
    daddy4.goto(75, -125)
    daddy4.goto(50, -75)
    daddy4.goto(0, -200)
    daddy4.goto(-50, -75)
    daddy4.goto(-75, -125)
    daddy4.goto(-100, -75)
    daddy4.end_fill()
    daddy4.pu()
    daddy4.hideturtle()

def make_casket(daddy5):
    daddy5.pu()
    daddy5.color("brown")
    daddy5.goto(150, -169)
    daddy5.begin_fill()
    daddy5.pd()
    daddy5.goto(50, -169)
    daddy5.goto(50, -229)
    daddy5.goto(250, -229)
    daddy5.goto(250, -169)
    daddy5.goto(150, -169)
    daddy5.end_fill()
    daddy5.pu()
    daddy5.hideturtle()

def make_legs(daddy6):
    daddy6.color("#FFE9D1")
    daddy6.pu()
    daddy6.goto(-100, -75)
    daddy6.begin_fill()
    daddy6.pd()
    daddy6.goto(-100, -125)
    daddy6.goto(-50, -125)
    daddy6.goto(-50, -75)
    daddy6.goto(-100, -75)
    daddy6.end_fill()
    daddy6.pu()

    daddy6.goto(100, -75)
    daddy6.begin_fill()
    daddy6.pd()
    daddy6.goto(100, -125)
    daddy6.goto(50, -125)
    daddy6.goto(50, -75)
    daddy6.goto(100, -75)
    daddy6.end_fill()



t1 = trtl.Turtle(shape="square")
t2 = trtl.Turtle(shape="triangle")
t3 = trtl.Turtle(shape="turtle")
t4 = trtl.Turtle(shape="square")
t5 = trtl.Turtle(shape="turtle")
t6 = trtl.Turtle(shape="triangle")

make_legs(t6)
make_arms(t1)
make_stomach(t2)
make_head(t3)
make_pants(t4)
make_casket(t5)


wn = trtl.Screen()
wn.mainloop()