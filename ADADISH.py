for t in range(int(input())):
    size = int(input())
    inputarray = input().split()
    for i in range(0,len(inputarray)):
        inputarray[i]=int(inputarray[i])
    timetocook=-999
    list1=[]
    list2=[]
    inputarray.sort(reverse=True)
    if(len(inputarray)==1):
        timetocook=inputarray[0]
    if(len(inputarray)==2):
        timetocook=max(inputarray[0],inputarray[1])
    if(len(inputarray)>=3):
        for k in range(len(inputarray)):
            sum1=sum(list1)
            sum2=sum(list2)
            if(sum1<sum2):
                list1.append(inputarray[k])
            elif(sum2<sum1):
                list2.append(inputarray[k])
            else:
                list1.append(inputarray[k])
        sum1=sum(list1)
        sum2=sum(list2)
        timetocook=max(sum1,sum2)
    print(timetocook)