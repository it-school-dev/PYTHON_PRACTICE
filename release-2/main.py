from collections import Counter

def sorting(arr, direction):
    if direction==1:
        return sorted (arr)
    elif direction==-1:
        return sorted (arr, reverse=True)
# print (sorting([1,5,2],-1))
# print(sorting([1,5,2],1))



def DeepSorting (a,key):
    mylist =sorted(a, key=lambda d: d[key])
    return mylist
#print (DeepSorting ([{'age': 15, 'height': 140}, {'age': 14, 'height': 150}], 'age'))



def getNumbers (a):
    mylist=[]
    for elem in a:
        if type(elem)==int or type(elem)==float:
            mylist.append(elem)
    return mylist
#print (getNumbers (['d', 1, 3, 'null']))



def min (a=[]):
    return sorted(a)[0]
#print (min ([1, 5, 34, -100]))



def getSet (a=[]):
    mylist=[]
    for elem in a:
        if not elem in mylist:
            mylist.append(elem)
        return mylist
#print (getSet(a=[1,1,1,3,4,2,2]))



def findTheMostReapetedEls (a):
    counts =Counter(a)
    #print (counts)  
    max_count=max(counts.values())
    my_list=[]
    for elem in counts.items():
        if elem[1]==max_count:
            my_list.append(elem[0])
    return(my_list)
#print (findTheMostReapetedEls ([1,1,1,2,2,2,3,4]))




def checkForBadWords (a,word):
        if word in a:
            return 'True'
        else:
            return 'False'
#print(checkForBadWords('Hi, Nikita', 'Hi'))


    
def stack(arr):
    counter=0
    for elem in arr:
        if elem =='[':
            counter +=1
        else:
            counter -=1
    if counter==0:
        return True
    else:
        return False
print (stack(['[','[', ']', ']' ]))
print (stack([']', '[', ']']))

