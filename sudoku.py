import numpy
import tkinter


root = tkinter.Tk()
puzzle = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0], 
        [5, 2, 0, 0, 0, 0, 0, 0, 0], 
        [0, 8, 7, 0, 0, 0, 0, 3, 1], 
        [0, 0, 3, 0, 1, 0, 0, 8, 0], 
        [9, 0, 0, 8, 6, 3, 0, 0, 5], 
        [0, 5, 0, 0, 9, 0, 6, 0, 0], 
        [1, 3, 0, 0, 0, 0, 2, 5, 0], 
        [0, 0, 0, 0, 0, 0, 0, 7, 4], 
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]
def possible(x,y,n):
    global puzzle
    for i in range(0,9):
        if puzzle[x][i]==n:
            return False
    for i in range(0,9):
        if puzzle[i][y]==n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if puzzle[x0+i][y0+j]==n:
                return False
    return True

def solve():
    global puzzle
    for i in range(9):
        for j in range(9):
            if puzzle[i][j]==0:
                for temp in range(1,10):
                    if possible(i,j,temp):
                        puzzle[i][j] = temp
                        solve()
                        puzzle[i][j]=0
                return
    print(numpy.matrix(puzzle))
    input("More?")

def main():
    global puzzle
    for i in range(9):
        for j in range(9):
            mylabel = tkinter.Label(root,text=""+str(puzzle[i][j]))
            mylabel.grid(row=i,column=j)

if __name__ == '__main__':
    main()
    root.mainloop()