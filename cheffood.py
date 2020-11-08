#chefland
t=int(input())
maxpro=0
ty=0
for i in range(0,t):
    
    ty=int(input())
    for j in range(0,ty):
        temp=0
        in_list = input().split()
        temp = (int(in_list[2])/int(in_list[0])) * int(in_list[1])
    if temp>maxpro:
        maxpro = temp

    if ty == 1:
        print("0")    
    else:
        print(maxpro)