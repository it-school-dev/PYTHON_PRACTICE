def sorting(arr, direction):
    if direction == 1:
        return sorted(arr)
    if direction == -1:
    return sorted(arr)[::-1]


def deepSorting(listd, strd):
    return sorted(listd, key= lambda elem: elem[strd])
        
    
def getNumbers(list1):
    listofnums = []
    for i in range(len(list1)):
        if type(list1[i]) == int or type(list1[i]) == float:
            listofnums.append(list1[i])
    return listofnums
    

def mymin(list1):
    m = list1[0]
    for i in range (1, len(list1)):
        if list1[i] < m:
            m = list1[i]
    return m


def getSet(list1):
    newlist = list(set(list1))
    return newlist


def findTheMostReapetedEls(list1):
    listcount = [list1.count(elem) for elem in list1]
    newlist = []
    maxcount = max(listcount)
    for i in range (len(list1)):
        if listcount[i] == maxcount:
            newlist.append(list1[i])
    return list(set(newlist))


def checkForBadWord(string, word):
    if word in string:
        return True
    else:
        return False
