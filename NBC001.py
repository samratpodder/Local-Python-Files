for t in range(int(input())):
    inputlist = input().split()
    for i in range(len(inputlist)):
        inputlist[i] = int(inputlist[i])
    # print((inputlist[1]**2),(inputlist[0]**2),inputlist[2]**2)
    if((inputlist[1]**2)+(inputlist[0]**2)==inputlist[2]**2):
        print("YES %.5f"%(0.5*(inputlist[0]*inputlist[1])))
    else:
        print("NO")