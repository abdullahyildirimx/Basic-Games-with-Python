maze=[]
maze=open("maze.txt").read().splitlines()
row=len(maze)
column=len(maze[0])
startpoint=[0,0]
finishpoint=[0,0]
for i in range(0,row):
    for j in range(0,column):
        if maze[i][j]=='S':
            startpoint=[i,j]
for i in range(0,row):
    for j in range(0,column):
        if maze[i][j]=='F':
            finishpoint=[i,j]
def valid(maze,x,y):   
    if x>= 0 and x < row and y >= 0 and y < column and maze[x][y]!='W': 
        return True
def inrange(maze,x,y):
    if x >= 0 and x < row and y >= 0 and y < column:
        return True
def solver(maze): 
    s=[[0 for j in range(column)] for i in range(row)] 
    if solverhelper(maze, startpoint[0], startpoint[1], s,used) == False: 
        return False
    printmaze(s)
    return True
used=[[0 for j in range(column)] for i in range(row)] 
def solverhelper(maze,x,y,s,used): 
    if x ==finishpoint[0] and y==finishpoint[1]: 
        s[x][y] = 1
        return True
    used[x][y]=1
    if valid(maze,x,y) == True:  
        s[x][y] = 1
        if inrange(maze,x+1,y):
            if used[x+1][y]==0:
                if solverhelper(maze,x+1,y,s,used) == True: 
                    return True
        if inrange(maze,x-1,y):
            if used[x-1][y]==0:
                if solverhelper(maze,x-1,y,s,used) == True: 
                    return True
        if inrange(maze,x,y-1):
            if used[x][y-1]==0:
                if solverhelper(maze,x,y-1,s,used) == True: 
                    return True
        if inrange(maze,x,y+1):
            if used[x][y+1]==0:
                if solverhelper(maze,x,y+1,s,used) == True: 
                    return True
        s[x][y]=0
        return False
    return False
def printmaze(s):
    s[startpoint[0]][startpoint[1]]='S'
    s[finishpoint[0]][finishpoint[1]]='F'
    for i in range(0,row):
        string1=""
        for j in range(0,column):
            if j==column-1:
                string1=string1+str(s[i][j])
            else:
                string1=string1+str(s[i][j])+", "
        print (string1)
solver(maze)
print ("")
