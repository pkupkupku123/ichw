"""tile.py: Cover a wall with given tiles

__author__ = "Liye"
__pkuid__ = "1800011779"
__email__ = "pkupkupku@pku.edu.cn"
"""

import turtle as t



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
    if (k + 1)% m == 0:
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
    for k in tile:
        for i in Alltiles:
            for n in i:
                if k == n:
                    return True
    return False


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
    if len(Alltiles) < m*n/(a*b):
        state = [0]*m*n
        for tiles in Alltiles:
            for i in tiles:
                state[i] = 1
        while state[k] == 1:
            k += 1
        return k
    

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
    if len(Alltiles) == m*n/(a*b):
        print(Alltiles)
        Allmethods.extend([Alltiles])
    else:
        i, j = anti_convert(k, m)
        if i+a-1 <= m and j+b-1 <= n:
            tile = [convert(i1,j1,m)
            for j1 in range(j, j+b)
            for i1 in range(i, i+a)]
            
            if not conflict(tile, Alltiles):
                cover(m, n, a, b, Allmethods, Alltiles+[tuple(tile)], \
                      find_k(m, n, a, b, Alltiles+[tuple(tile)], k))
        
        if i+b-1 <= m and j+a-1 <= n and a != b:
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
    t.reset()
    t.screensize(400,400,"white")
    t.speed(0)
    t.pensize(0.25)
    t.color('blue')
    for i in range(0,m+1):
        t.penup()
        t.goto((2*i-m)*20, n*20)
        t.pendown()
        t.goto((2*i-m)*20, -n*20)
    for i in range(0,n+1):
        t.penup()
        t.goto(m*20, (2*i-n)*20)
        t.pendown()
        t.goto(-m*20, (2*i-n)*20)
    t.penup()
    for k in range(0,m*n):
        i, j = anti_convert(k, m)
        t.goto((2*i-m-2)*20+20, (n+2-2*j)*20-25)
        t.write(k)
    t.color('black')
    t.pensize(5)
    for tile in Alltiles:
        i1, j1 = anti_convert(tile[0], m)
        i2, j2 = anti_convert(tile[-1],m)
        t.penup()
        t.goto((2*i1-m-2)*20, (n+2-2*j1)*20)
        t.pendown()
        t.goto((2*i2-m)*20, (n+2-2*j1)*20)
        t.goto((2*i2-m)*20, (n-2*j2)*20)
        t.goto((2*i1-m-2)*20, (n-2*j2)*20)
        t.goto((2*i1-m-2)*20, (n+2-2*j1)*20)
    t.hideturtle()

    
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
    if len(Allmethods) == 0:
        s = t.numinput('NO SOLUTION!','Enter 1 to try again'+ \
                   '(cover a new wall with new tiles)'+ \
                   ' ,enter any other integer to close this program')
        if s == 1:
            main()
        else:
            t.bye()
    else:
        s = t.numinput(str(len(Allmethods)) + ' solutions in total', \
                       'Enter 1 to select a plan, enter 2 to restart the '+ \
                       'whole prongram(cover a new wall with new tiles) '+ \
                       ',enter any other integer to close this program')
        if s == 1:
            num = int(t.numinput('Select a plan','Input an integer from 1 to'+ \
                             str(len(Allmethods)), None, 1, len(Allmethods))) - 1
            visualization(m, n, Allmethods[num])
            contiune(m, n, Allmethods)
        elif s == 2:
            main()
        else:
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
