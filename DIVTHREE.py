for t in range(int(input())):
    inputarray=input().split()
    for i in range(len(inputarray)):
        inputarray[i] = int(inputarray[i])
    n=inputarray[0]
    k=inputarray[1]
    d=inputarray[2]
    inputarr = input().split()
    for i in range(len(inputarr)):
        inputarr[i] = int(inputarr[i])
    Sum =sum(inputarr)
    if (k*d<Sum):
        print(d)
    else:
        print(Sum//k)