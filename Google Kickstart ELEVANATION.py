import copy
listofnums=list()

def combinations(numlist):
    for i in range(len(numlist)):
        for j in range(i,len(numlist)):
            temp=numlist[i]
            numlist[i]=numlist[j]
            numlist[j]=temp
            # print(numlist,i,j,listofnums)
            if(numlist not in listofnums):
                listofnums.append(copy.deepcopy(numlist))
    for i in range(0,len(numlist)):
        idxi=len(numlist)-i-1
        # print(idxi)
        for j in range(0,idxi+1):
            idxj=len(numlist)-j-1
            # print(idxj)
            temp=numlist[idxi]
            numlist[idxi]=numlist[idxj]
            numlist[idxj]=temp
            # print(numlist,i,j,listofnums)
            if(numlist not in listofnums):
                listofnums.append(copy.deepcopy(numlist))
for t in range(int(input())):
    listofnums.clear()
    inputarray = input().split()
    for i in range(0,len(inputarray)):
        inputarray[i]=int(inputarray[i])
    number=list()
    for i in range(0,9):
        for j in range(inputarray[i]):
            number.append(i+1)
    combinations(number)
    print(listofnums)
    # print(listofnums)
    flag=False
    for currnum in listofnums:
        
        counter=1
        sumofdigits=0
        # print(listofnums)
        for nums in currnum:
            if (counter >= 2 and counter % 2 == 0):
                sumofdigits-=nums
            else:
                sumofdigits+=nums
            counter+=1
        if(sumofdigits%11==0):
            
            flag=True
            break
    if(flag):
        print("Case #"+str(t+1)+": YES")
    else:
        print("Case #"+str(t+1)+": NO")