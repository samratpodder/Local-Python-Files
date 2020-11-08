import copy
for i in range(int(input())):
    all_in = (input().split())
    N = int(all_in[0])
    # N-=1
    K = int(all_in[1])
    # K-=1
    X = int(all_in[2])
    # X-=1
    Y = int(all_in[3])
    # Y-=1
    cities = list()
    curr = copy.deepcopy(X)
    infected = list()
    for j in range(N):
        cities.append(0)
    flag = 0
    while True:
        cities[curr] +=1
        curr = (curr+K)%N
        if (cities[Y]):

            print("YES")
            break
        else:
            if curr==X:
                print("NO")
                break