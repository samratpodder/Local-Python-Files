# import sys
def makeBlack(puzzle,size):
    moves = 0
    firstcol = list()
    for i in range(size):
        firstcol.append((i,0))
    # print(firstcol)
    lastcol = list()
    for i in range(size):
        lastcol.append((i,size-1))
    for i in range(0,size):
        x,y=firstcol[i]
        for j in range(0,i+1):
            # print(x-j,y+j)
            if(puzzle[x-j][y+j] == '.'):
                puzzle[x-j][y+j] = '#'
                # print(moves)
                moves+=1
    # print("----------------------------")
    for i in range(0,size):
        x,y=lastcol[i]
        for j in range(0,i+1):
            # print(x-j,y-j)
            if(puzzle[x-j][y-j] == '.'):
                puzzle[x-j][y-j] = '#'
                # print(moves)
                moves+=1
    # print(puzzle)
    return moves-1
for t in range(int(input())):
    size = int(input())
    puzzle = list()
    for i in range(size):
        # puzzle.append(list())
        puzzle.append(input().split())
        puzzle[i] = list(puzzle[i][0])
    # if makeBlack(puzzle=puzzle,size=size) < 0:
        # print(0)
    moves=(int(makeBlack(puzzle,size)))
    if moves < 0:
        print('Case #'+str(t)+': '+str(0))
    else:
        print('Case #'+str(t)+': '+str(moves))