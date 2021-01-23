for t in range(int(input())):
    inputstr = input().split(" ")
    A,B=int(inputstr[0]),int(inputstr[1])
    combins =0
    xeven,xodd,yeven,yodd=0,0,0,0
    xeven = int(A/2)
    xodd=A-xeven
    yeven = int(B/2)
    yodd = B-yeven
    # for val in range(0,A):
    #     if val%2==0:
    #         xeven+=1
    #     else:
    #         xodd+=1
    # for val in range(0,B):
    #     if val%2==0:
    #         yeven+=1
    #     else:
    #         yodd+=1
    combins=(xeven*yeven) + (xodd*yodd)
    print(combins)