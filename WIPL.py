for t in range(int(input())):
    inputarr = input().split()
    for i in range(len(inputarr)):
        inputarr[i] = int(inputarr[i])
    N,K = inputarr[0],inputarr[1]
    H = input().split()
    for i in range(len(H)):
        H[i] = int(H[i])
    tower1=0
    tower2=0
    H.sort()
    used=0
    for i in range(0,N,2):
        i=N-i-1
        if tower1<K:
            tower1+=H[i]
            used+=1
        if tower2<K:
            tower2+=H[i-1]
            used+=1
        if(tower1>=K and tower2>=K):
            break
    if tower1<K and tower2<K:
        print(-1)
    else:
        print(used)
