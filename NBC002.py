# dictin1={}
# dictin2={}
# def mode1(string):
#     count=0
#     charec = string[0]
#     for c in string:
#         if(charec==c):
#             count+=1
#             dictin1[c] = count
#         else:
#             count=1
#             dictin1[c]=count
# def mode2(string):
#     count=0
#     charec = string[0]
#     for c in string:
#         if(charec==c):
#             count+=1
#             dictin2[c] = count
#         else:
#             count=1
#             dictin2[c]=count
def split(word): 
    return [char for char in word] 
def most_frequent(List): 
    counter = 0
    num = List[0] 
      
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
  
    return num 
direction = {'n':'north','e':'east','w':'west','s':'south'}
for t in range(int(input())):
    s1 = input()
    s2 = input()
    first = s1[-1]
    second = s2[-1]
    # frequent1 = mode1(s1)
    # frequent2 = mode2(s2)
    # print(dictin1,dictin2)
    lists1 = split(s1)
    lists2 = split(s2)
    # print(lists1,lists2)
    s1c = most_frequent(lists1)
    s1count = lists1.count(s1c)
    s2c = most_frequent(lists2)
    s2count = lists2.count(s2c)
    print(s1count,direction[first],s2count,direction[second])
