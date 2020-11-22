primes=[True for i in range(4000000)]
primes[0]=False
primes[1]=False
p = 2
while (p * p <= 4000000): 
    if (primes[p] == True): 
        for i in range(p * p, 4000000, p): 
            primes[i] = False
    p += 1
prime=list()
for i in range(len(primes)):
    if(primes[i]==True):
        prime.append(i)


def primeList(size):
    return prime[0:size]





for t in range(int(input())):
    size = int(input())
    B = input().split()
    for i in range(0,len(B)):
        B[i]=int(B[i])
    A=primeList(len(B))
    for i in range(0,len(B)):
        j=B[i]
        j=j-1
        while(A[j]%A[i]!=0):
            if(A[i]<=A[j]):
                A[i]+=1
            if(A[i]>A[j]):
                A[i]-=1
    for i in range(0,size):
        if(i==size-1):
            print(A[i])
        else:
            print(A[i],end=" ")