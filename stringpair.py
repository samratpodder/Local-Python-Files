def numvowel(str):
    countvowel=0
    for elements in str:
        if(elements=="a" or elements=="e" or elements=="i" or elements=="o" or elements=="u"):
            countvowel+=1
    return countvowel

if  __name__ == "__main__":
    numword=["zero","one","two","three","four","five","six","seven","eight","nine"]
    inp = int(input())
    inseries = input()
    inlist = inseries.split()
    for i in range(len(inlist)):
        inlist[i]=int(inlist[i])
    vowelcountlist=[]
    for items in inlist:
        inword = numword[items]
        vowelcountlist.append(numvowel(inword))
    d=0
    for items in vowelcountlist:
        d=d+items
    pair =set()
    for i in range(0,len(inlist)-1):
        for j in range(i+1,len(inlist)):
            if inlist[i]+inlist[j] == d:
                pair.add((inlist[i],inlist[j]))
    ans = len(pair)
    print(numword[ans])
    