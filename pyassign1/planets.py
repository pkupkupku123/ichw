"""planets.py:模拟太阳系六大行星公转

__author__ = "Liye"
__pkuid__  = "1800011779"
__email__  = "pkupkupku@pku.edu.cn"
"""

import turtle as t
import math as m

def Planets(semimajor_axis, semi_focal_length, color, starsize):
    """输入行星参数以定义行星画笔并返回作图所需参数
    """
    star = t.Turtle()
    star.shape('circle')
    star.color(color)
    star.shapesize(starsize)
    star.speed(0)
    star.pensize(1.1)
    star.penup()
    star.fd(semimajor_axis - semi_focal_length)
    star.pendown()
    semiminor_axis = m.sqrt(semimajor_axis**2 - semi_focal_length**2)
    return [star,semimajor_axis,semi_focal_length,semiminor_axis]

def Sun():
    """画出太阳
    """
    Sun = t.Turtle()
    Sun.shape('circle')
    Sun.shapesize(1.5)
    Sun.color('yellow')

def Draworbit(star, semimajor_axis, semi_focal_length, semiminor_axis,i):
    """输入所需参数以控制行星画笔运动
    """
    star.goto(m.cos(m.radians(i))*semimajor_axis - semi_focal_length, m.sin(m.radians(i))*semiminor_axis)
    
def main():
    """main module
    """
    Earth = Planets(90,8,'blue',0.5)
    Venus = Planets(60,2,'lemonchiffon1',0.45)
    Jupiter = Planets(200,56,'navajowhite',0.7)
    Mercury =  Planets(35,15,'darkturquoise',0.2)
    Mars = Planets(135,35,'firebrick3',0.35)
    Saturn = Planets(350,100,'lightgoldenrod3',0.65)
    t.bgcolor('black')
    Sun()
    i = 1
    while True:
        Draworbit(Mercury[0],Mercury[1],Mercury[2],Mercury[3],i)
        Draworbit(Venus[0],Venus[1],Venus[2],Venus[3],i/2)
        Draworbit(Earth[0],Earth[1],Earth[2],Earth[3],i/3)
        Draworbit(Mars[0],Mars[1],Mars[2],Mars[3],i/5)
        Draworbit(Jupiter[0],Jupiter[1],Jupiter[2],Jupiter[3],i/7)
        Draworbit(Saturn[0],Saturn[1],Saturn[2],Saturn[3],i/9)
        i += 2.5
    
if __name__ == '__main__':
    main()
