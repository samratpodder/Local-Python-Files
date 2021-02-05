import os
if __name__ == "__main__":
    for t in range(int(input())):
        inputarr=input().split()
        for i in range(len(inputarr)):
            inputarr[i] = int(inputarr[i])
        N,K,x,y = inputarr[0],inputarr[1],inputarr[2],inputarr[3]
        retval=list()
        for i in range(4):
            retval.append(0)
        if x>y:
            diff = N-x
            retval[0]=[N,y+diff]
            retval[1]=[y+diff,N]
            retval[2]=[0,N-diff-y]
            retval[3]=[N-diff-y,0]
        elif y>x:
            diff = N-y
            retval[0]=[x+diff,N]
            retval[1]=[N,x+diff]
            retval[2]=[N-diff-x,0]
            retval[3]=[0,N-diff-x]
        elif x==y:
            print(N,N)
            continue
        idx = (K%4 )-1
        print(retval[idx][0],retval[idx][1])