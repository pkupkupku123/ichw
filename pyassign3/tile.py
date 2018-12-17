"""tile.py: Cover a wall with given tiles

__author__ = "Liye"
__pkuid__ = "1800011779"
__email__ = "pkupkupku@pku.edu.cn"
"""

import turtle as t    # 将turtle记为t，便于可视化模块的编写，并使看起来简洁。



def convert(i, j, m):
    """A function to convert a 2D coordinate into an 1D coordinate.
    
    Parameter i: x-coordinate of a given unit of the wall.
    Precondition: i is an int which is positive and no more than m.
        
    Parameter j: y-coordinate of a given unit of the wall.
    Precondition: j is an int which is positive.
        
    Parameter m: width of the wall.
    Precondition: m is an int which is positive.
        
    Returns: the 1D coordinate of the given unit.
    The value returned has type int.
    """
    return (j - 1)*m + i - 1


def anti_convert(k, m):
    """The anti-function of function 'convert'.
    
    Parameter k: the 1D coordinate of a given unit of the wall.
    Precondition: k is an int which is not negative.
        
    Parameter m: width of the wall.
    Precondition: m is an int which is positive.
        
    Returns: the 2D coordinate of the given unit.    
    The values returned have type int.
    """
    if (k + 1)% m == 0:    # 整除时，坐标换算公式有所不同，因此用if条件句单独写出。
        return m, ((k + 1)// m)
    else:
        return (k + 1)% m, ((k + 1)// m) + 1
    
    
def conflict(tile, Alltiles):
    """A function to judge whether a new tile conflicts with 
    the tiles that allready existed.
    
    Parameter tile: a tile's position. (the unit in this tile)
    Precondition: tile is a tuple consists of the units' 1D coordinates.
        
    Parameter Alltiles: the tiles already existed.
    Precondition: Alltiles is a list consists of tuples that represent the
    tiles existed.
        
    Returns: conflict or not(True or False).
    The value returned has type bool.
    """
    for k in tile:    # 遍历新铺的砖中的单元格，以k记。
        for i in Alltiles:
            for n in i:    # 两个循环遍历所有已铺上砖的单元格，以n记。
                if k == n:
                    return True    # 一旦k==n，说明有单元格重复，出现矛盾，返回True。
    return False    # 如果始终不相等，说明单元格不会重复，返回False。


def find_k(m, n, a, b, Alltiles, k):
    """A function to find the uncovering unit with the smallest 1D coordinate.
    
    Parameter m: width of the wall.
    Precondition: m is an int which is positive.
        
    Parameter n: height of the wall.
    Precondition: n is an int which is positive.
        
    Parameter a: width of the tile.
    Precondition: a is an int which is positive.
        
    Parameter b: length of the tile.
    Precondition: b is an int which is positive.
        
    Parameter Alltiles: the tiles already existed.
    Precondition: Alltiles is a list consists of tuples that represent the
    tiles existed.
        
    Parameter k: 1D coordinate of the latest unit we cover.
    Precondition: k is an int which is in [0, m*n-1]
        
    Returns: 1D coordinate of the next unit to cover, if all units have been 
    covered, return None.
    The value returned has type int or None
    """
    if len(Alltiles) < m*n/(a*b):    # 判断是否已经铺满，避免之后语句列表越界报错。
        state = [0]*m*n
        for tiles in Alltiles:
            for i in tiles:
                state[i] = 1    # 新建一维列表，用于表示各个单元格所处的状态。
        while state[k] == 1:
            k += 1
        return k    # 从上一个铺了的单元格开始，找到编号最小的未铺单元格。
    # 如果已经铺满，这里将直接返回None，但不影响cover函数的运行。
    

def cover(m, n, a, b, Allmethods, Alltiles=[], k=0):
    """A function to cover a given wall with given tiles, printing all methods
    and the number of methods in total.
    
    Parameter m: width of the wall.
    Precondition: m is an int which is positive.
        
    Parameter n: height of the wall.
    Precondition: n is an int which is positive.
        
    Parameter a: width of the tile.
    Precondition: a is an int which is positive.
        
    Parameter b: length of the tile.
    Precondition: b is an int which is positive.
        
    Parameter Allmethods: the solutions we have already worked out.
    Precondition: Allmethods is a list consists of sub-lists that represent the 
    solutions we have worked out.
        
    Parameter Alltiles: the tiles allready existed.
    Precondition: Alltiles is a list consists of tuples that represent the
    tiles existed.
        
    Parameter k: 1D coordinate of the unit which we will try to cover next.
    Precondition: k is an int in [0,m*n-1]
        
    This function has no value returned, or the return is None.
    """
    if len(Alltiles) == m*n/(a*b):    # 如果已经铺满，则打印出铺法，并将铺法记录进解法列表。
        print(Alltiles)
        Allmethods.extend([Alltiles])
    else:    # 如果没有铺满，则继续往下铺
        i, j = anti_convert(k, m)    # 解析待铺单元格二维坐标。
        
        # 由于确定了待铺的单元格编号最小，针对这一单元格至多只可能有两种铺法。
        
        if i+a-1 <= m and j+b-1 <= n:    # 判定横着铺是否超出墙，如否，将砖块列表化。
            tile = [convert(i1,j1,m)
            for j1 in range(j, j+b)
            for i1 in range(i, i+a)]    # i的循环放在内层，保证砖块内单元格编号是由小到大。
            
            if not conflict(tile, Alltiles):    # 如果不超出墙又不重复，进入下一层递归。
                cover(m, n, a, b, Allmethods, Alltiles+[tuple(tile)], \
                      find_k(m, n, a, b, Alltiles+[tuple(tile)], k))
        
        if i+b-1 <= m and j+a-1 <= n and a != b:    # 如果砖块是正方形则不用分支，其余同上。
            tile = [convert(i1, j1, m)
            for j1 in range(j, j+a)
            for i1 in range(i, i+b)]
        
            if not conflict(tile, Alltiles):
                cover(m, n, a, b, Allmethods, Alltiles+[tuple(tile)], \
                      find_k(m, n, a, b, Alltiles+[tuple(tile)], k))


def visualization(m, n, Alltiles):
    """A function to visualize a method by draw a picture of the 
    covered wall with the help of the turtle module.
    
    Parameter m: width of the wall.
    Precondition: m is an int which is positive.
        
    Parameter n: height of the wall.
    Precondition: n is an int which is positive.
        
    Parameter Alltiles: a solution.
    Precondition: Alltiles is a list consists of tuples that represent the
    tiles existed, and those tiles have covered all units of the wall.
        
    This function has no value returned, or the return is None.
    """
    t.reset()    # 因为后期程序对于一种情形，用户可以多次选择不同解法可视化，因此reset。
    t.screensize(400,400,"white")
    t.speed(0)    # 绘图过程较多，加快绘图，节省用户时间。
    t.pensize(0.25)
    t.color('blue')
    for i in range(0,m+1):    # 绘制墙面铅垂线。
        t.penup()
        t.goto((2*i-m)*20, n*20)
        t.pendown()
        t.goto((2*i-m)*20, -n*20)
    for i in range(0,n+1):    # 绘制墙面水平线。
        t.penup()
        t.goto(m*20, (2*i-n)*20)
        t.pendown()
        t.goto(-m*20, (2*i-n)*20)
    t.penup()
    for k in range(0,m*n):    # 为单元格添加编号。
        i, j = anti_convert(k, m)
        t.goto((2*i-m-2)*20+20, (n+2-2*j)*20-25)
        t.write(k)
    t.color('black')
    t.pensize(5)
    for tile in Alltiles:    # 调用铺法信息，实现可视化。
        i1, j1 = anti_convert(tile[0], m)
        i2, j2 = anti_convert(tile[-1],m)    # 对于一块砖，解析其首末两个单元格即可确定位置。
        t.penup()
        t.goto((2*i1-m-2)*20, (n+2-2*j1)*20)
        t.pendown()
        t.goto((2*i2-m)*20, (n+2-2*j1)*20)
        t.goto((2*i2-m)*20, (n-2*j2)*20)
        t.goto((2*i1-m-2)*20, (n-2*j2)*20)
        t.goto((2*i1-m-2)*20, (n+2-2*j1)*20)
    t.hideturtle()    # 隐藏画笔，避免尴尬。

    
def contiune(m, n, Allmethods):
    """A function to help users use this program, after the function 'cover' 
    is called and all methods are printed, this function gives users three 
    choices: select a plan and visualize it, restart the whole program or
    close this program.
    
    Parameter m: width of the wall.
    Precondition: m is an int which is positive.
        
    Parameter n: height of the wall.
    Precondition: n is an int which is positive.
        
    Parameter Allmethods: all solutions under the given condition.
    Precondition: Allmethods is a list consists of sub-lists that represent the 
    solutions we have worked out.
        
    This function has no value returned, or the return is None.
    """
    if len(Allmethods) == 0:    # 没有铺法时的人机交互。
        s = t.numinput('NO SOLUTION!','Enter 1 to try again'+ \
                   '(cover a new wall with new tiles)'+ \
                   ' ,enter any other integer to close this program')
        
        if s == 1:    # 如果用户输入1，重启铺砖程序。
            main()
        else:    # 如果用户输入其他数字，关闭turtle界面并退出程序。
            t.bye()
            
    else:    # 有铺法时的人机交互。
        s = t.numinput(str(len(Allmethods)) + ' solutions in total', \
                       'Enter 1 to select a plan, enter 2 to restart the '+ \
                       'whole prongram(cover a new wall with new tiles) '+ \
                       ',enter any other integer to close this program')
        
        if s == 1:    # 如果用户输入1，则用户可以选择一种铺法可视化，并重新进入交互界面。
            num = int(t.numinput('Select a plan','Input an integer from 1 to'+ \
                             str(len(Allmethods)), None, 1, len(Allmethods))) - 1
            visualization(m, n, Allmethods[num])
            contiune(m, n, Allmethods)    # 使得用户不必多次计算铺法就可以多次可视化。
            
        elif s == 2:    # 如果用户输入2，重启铺砖程序。
            main()
        else:    # 如果用户输入其他数字，关闭turtle界面并推出程序。
            t.bye()

             
def main():
    """The Main Module
    
    Get input and start the whole program.
    """
    m = int(t.numinput('Width of the wall','Enter a positive integer', None,\
                       1, None))
    n = int(t.numinput('Height of the wall','Enter a positive integer', None,\
                       1, None))
    a = int(t.numinput('Width of the tile','Enter a positive integer', None,\
                       1, None))
    b = int(t.numinput('Length of the tile','Enter a positive integer', None,\
                       1, None))
    Allmethods = []
    cover(m, n, a, b, Allmethods)
    print('we have',len(Allmethods),'solution(s)')
    contiune(m, n, Allmethods)

    
if __name__=='__main__':
    main()
