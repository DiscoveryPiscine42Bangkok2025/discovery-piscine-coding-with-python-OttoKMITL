def checkmate(Board):
    Board=[list(row) for row in Board.strip().split('\n')]
    BoardSize=len(Board)
    for i in Board:
        if(BoardSize!=len(i)):
            print("Error")
            return
    King=None
    for i in range(BoardSize):
        for j in range(BoardSize):
            if Board[i][j]=='K':
                King=[i, j]
    if(not King):
        print("Error")
        return
    for i in range(BoardSize):
        for j in range(BoardSize):
            if((Board[i][j]=='P') and (i==King[0]+1) and (abs(King[1]-j)==1)):
                print("Success")
                return
            if((Board[i][j]=='B') and (abs(King[0]-i)==abs(King[1]-j)) and (ClearPath(Board, i, j, King[0], King[1]))):
                print("Success")
                return
            if((Board[i][j]=='R') and ((i==King[0]) or (j==King[1])) and (ClearPath(Board, i, j, King[0], King[1]))):
                print("Success")
                return
            if((Board[i][j]=='Q') and ((i==King[0]) or (j==King[1]) or (abs(King[0]-i)==abs(King[1]-j))) and (ClearPath(Board, i, j, King[0], King[1]))):
                print("Success")
                return
    print("Fail")
    return
def ClearPath(Board, x1, y1, x2, y2):
    if(x1==x2):
        for i in range(min(y1, y2)+1, max(y1, y2)):
            if(Board[x1][i]!='.'):
                return False
    elif(y1==y2):
        for i in range(min(x1, x2)+1, max(x1, x2)):
            if(Board[i][y1]!='.'):
                return False
    else:
        Step=abs(x1-x2)
        if(x1>x2):
            RowStep=-1
        else:
            RowStep=1
        if(y1>y2):
            ColumnStep=-1
        else:
            ColumnStep=1
        for i in range(1, Step):
            if(Board[x1+i*RowStep][y1+i*ColumnStep]!='.'):
                    return False
    return True