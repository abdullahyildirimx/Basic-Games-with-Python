n=int(input("What Size of TicTacToe?"))
a=n*n
board=[0 for index in range(a)]
for i in range (0,a):
    board[i]=i
def boardprinter(board):
    a=0;
    b=len(board)
    b=n

    while a<len(board): 
        for j in range(0,b):
            if j<b-1:
                print(" "+str(board[a]), end=' ')
                a=a+1
            elif j==b-1:
                print(" "+str(board[a]))
                a=a+1
def errorcheck1(board):
    x=int(input("Player 1 turn--> "))
    if x<0:
        print("Your choice is smaller than board.")
        return "error"
    elif x>=len(board):
        print("Your choice is bigger than board.")
        return "error"
    elif board[x]=="X":
        print("You have made this choice before")
        return "error"
    elif board[x]=="O":
        print("The other player select this cell before.")
        return "error"
    else:
        return x
def errorcheck2(board):
    x=int(input("Player 2 turn--> "))
    if x<0:
        print("Your choice is smaller than board.")
        return "error"
    elif x>=len(board):
        print("Your choice is bigger than board.")
        return "error"
    elif board[x]=="O":
        print("You have made this choice before")
        return "error"
    elif board[x]=="X":
        print("The other player select this cell before.")
        return "error"
    else:
        return x
boardprinter(board)
winner1=0
winner2=0
def wincondition1(board):
    for i in range(0,n):
        t=i*n
        t2=t+n
        test=0
        while t<t2:
            if board[t]=="X":
                test=1
                t=t+1
            else:
                test=0
                t=t2
        if test==1:
            return 1
    for i in range(0,n):
        t=i
        t2=n*n
        test=0
        while t<t2:
            if board[t]=="X":
                test=1
                t=t+n
            else:
                test=0
                t=t2
        if test==1:
            return 1
    for i in range(0,1):
        p=0
        test=0
        while (p<n*n):
            if board[p]=="X":
                test=1
                p=p+n+1
            else:
                test=0
                p=n*n
        if test==1:
            return 1
    for i in range(n-1,n):
        p=n-1
        test=0
        while (p<2*n+1):
            if board[p]=="X":
                test=1
                p=p+n-1
            else:
                test=0
                p=2*n+1
        if test==1:
            return 1
    return 0
    
        
def wincondition2(board):
    for i in range(0,n):
        t=i*n
        t2=t+n
        test=0
        while t<t2:
            if board[t]=="O":
                test=1
                t=t+1
            else:
                test=0
                t=t2
        if test==1:
            return 1
    for i in range(0,n):
        t=i
        t2=t+1+(n-1)*n
        test=0
        while t<t2:
            if board[t]=="O":
                test=1
                t=t+n
            else:
                test=0
                t=t2
        if test==1:
            return 1
    for i in range(0,1):
        p=0
        test=0
        while (p<n*n):
            if board[p]=="O":
                test=1
                p=p+n+1
            else:
                test=0
                p=n*n
        if test==1:
            return 1
    for i in range(n-1,n):
        p=n-1
        test=0
        while (p<2*n+1):
            if board[p]=="O":
                test=1
                p=p+n-1
            else:
                test=0
                p=2*n+1
        if test==1:
            return 1
    return 0
        
    
while winner1==0 and winner2==0:

    player1=errorcheck1(board)
    if player1=="error":
        player1=player1
    else:
        board[player1]="X"
    boardprinter(board)
    winner1=wincondition1(board)
    if winner1==1:
        print("Winner: X")
        break

    player2=errorcheck2(board)
    if player2=="error":
        player2=player2
    else:
        board[player2]="O"
    boardprinter(board)
    winner2=wincondition2(board)
    if winner2==1:
        print("Winner: O")
        break
