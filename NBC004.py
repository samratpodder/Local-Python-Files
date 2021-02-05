for t in range(int(input())):
    num = int(input())
    sum=0
    listsums=list()
    for i in range(num):
        # print(((i+1)**3)+(i**2))
        sum=(((i+1)**3)+(i**2))%1000000007
        listsums.append(sum)
    print(listsums)