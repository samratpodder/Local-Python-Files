inputint = int(input())
for i in range(1,11):
    i=11-i
    if inputint%i == 0:
        print(i)
        break