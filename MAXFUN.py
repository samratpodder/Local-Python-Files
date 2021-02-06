for t in range(int(input())):
    N=int(input())
    arr = input().split(" ")
    for i in range(N):
        arr[i]=int(arr[i])
    # print(arr)
    arr.sort()
    x=arr[0]
    y=arr[N//2]
    z=arr[N-1]
    print((abs(x-y))+(abs(y-z))+(abs(z-x)))