#TASK1
# def sorting(a, k):
#     if k==1:
#         a.sort()
#     else:
#         a.sort(reverse=True)
#     return a
# a1=[1,5,2]
# print(sorting(a1,1))
    

#TASK2
# import operator
# def deepSorting(a, x):
#     a.sort(key=operator.itemgetter(x))                    #эта штука достает конкретный х из списка
#     return a
# a1 = [{'age': 15, 'height': 140}, {'age': 14, 'height': 150}]
# x1 = 'age'
# print(deepSorting(a1, x1)) 


    
#TASK3
# def getNumbers(a):
#     b=[]
#     for i in range(len(a)):
#         if type(a[i])==int:
#             b.append(a[i])
#     return b
# a1=['d',1,3,'null',8]
# print(getNumbers(a1))

#TASK4
# def min(a):
#     mn=0
#     for i in range(len(a)-1):
#         if a[i]<a[i+1]:
#             mn=a[i]
#         else:
#             mn=a[i+1]
#     return mn
# a1=[1,5,34,-100]
# print(min(a1))

#TASK5
# def getSet(a):
#     b=[]
#     for i in range(len(a)-1):
#         if a[i]!=a[i-1]:
#             b.append(a[i])
#     return b
# a1=[1,1,1,3,4,2,2]
# print(getSet(a1))

#TASK6
# def findTheMostReapetedEls(a):
#     b=[]
#     for i in range(len(a)-1):
#         if a[i]!=a[i-1]:
#             b.append(a[i])
#     c=[]
#     for i in range(len(b)):
#         k=a.count(b[i])
#         if k>=3:
#             c.append(b[i])
#     return c
# a1=[1,1,1,3,4,2,2,2]
# print(findTheMostReapetedEls(a1))

# #TASK7
# def stack(a):
#     open=a.count('[')
#     close=a.count(']')
#     if open==close:
#         return 'true'
#     else:
#         return 'false'
# a1=['[','[',']',']']
# a2=['[','[',']']
# print(stack(a1))
# print(stack(a2))

# #TASK8
# def checkForBadWord(list):
#     if 'Hi' in list:
#         return 'true'
#     else:
#         return 'false'
# str='Hi, Nikita'
# print(checkForBadWord(str))
