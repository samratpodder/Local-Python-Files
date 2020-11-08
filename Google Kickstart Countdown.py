for i in range(int(input())):
    lenarray,m = input().split()
    lenarray = int(lenarray)
    m= int(m)
    in_array = input().split()
    for j in range(len(in_array)):
        in_array[j] = int(in_array[j])
    counter = 0

    temp=-999
    count = 0
    for j in range(len(in_array)):
        flag = False
        if(m==in_array[j]):
            for k in  range(j,lenarray):
                if in_array[k] == 1:
                    temp = k
                    # print(temp)
            if temp<0:
                flag = False
                continue
            for index,val in zip(range(j,temp+1),range(temp-j+1)):
                # print(index,val)
                if(m-val == in_array[index]-val):
                    flag = True
        if(flag):
            counter+=1
    print(f"Case #1: {counter}")
