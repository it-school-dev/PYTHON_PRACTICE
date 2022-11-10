def sorting(list, flag):
    if flag==1:
        return sorted(list)
    else:
        return sorted(list, reverse=True)

def getNumbers(list):
    listNew=[]
    for i in list:
        try:
            listNew.append(float(i))
        except ValueError:
            print
    return listNew

def min(list):
    listnew=sorted(list)
    return listnew[0]

def getSet(list):
    i=0
    while i<=len(list)-1:
        while list.count(list[i])>1:
            list.remove(list[i])
        i+=1
    return list

def findTheMostReapetedEls(list):
    i=0
    max=0
    listnew=[list[0]]
    while i<=len(list)-1:
        if list.count(list[i])>max:
            max=list.count(list[i])
            listnew.clear()
            listnew.append(list[i])
        elif ((list.count(list[i])==max)and(list[i] not in listnew)):
            listnew.append(list[i])
        i+=1
    return listnew

def stack(list):
    str=''.join(list)
    while str>'':
        if str[0]==']':
            return 'false'
            break
        else:
            str=str.replace('[]','')
    if str=='':
        return 'true'

def checkForBadWord(stroka, slovo):
    if stroka.find(slovo)>=0:
        return 'True'
    else:
        return 'False'

print(sorting([1, 5, 2], 1))
print(getNumbers(['d', -1, 3.5, 'null']))
print(min([1, 5, 34, -100]))
print(getSet([1, 1, 1, 3, 4, 2, 2]))
print(findTheMostReapetedEls([1, 1, 1, 3, 4, 2, 2, 2]))
print(stack([']', '[', ']', '[']))
print(checkForBadWord('Hi, Nikita', 'Hi'))