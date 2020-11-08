for i in range(int(input())):
    lenarray,m = input().split()
    lenarray = int(lenarray)
    m= int(m)
    in_array = input().split()
    for j in range(len(in_array)):
        in_array[j] = int(in_array[j])
    print("Case #"+str(i+1)+": " ,end=" ")
    visited = list()
    while(len([elem for elem in in_array if elem<=0])<lenarray):
        # print(in_array)
        for j in range(len(in_array)):
            in_array[j] -= m
            # print(in_array)
            if (in_array[j]<=0 and j not in visited):
                visited.append(j)
                print(j+1,end=" ")
    print()