from collections import Counter

def sorting(arr, direction):
    if direction == 1:
        return sorted(arr) # sorted(arg) = arg.sort()
    else:
        return sorted(arr, reverse=True)

def deepSorting(arr, key):
    new_list = sorted(arr, key=lambda d: d[key])
    return new_list

def getNumbers(arr):
    new_list = []
    for elem in arr:
        if type(elem) == int or type(elem) == float:
            new_list.append(elem)
    return new_list

def min(arr):
    return sorted(arr)[0]

def getSet(arr):
    output = []
    for elem in arr:
        if not elem in output:
            output.append(elem)
    return output

def findTheMostRepeatedEls(arr):
    counts = Counter(arr)
    # print(counts)
    max_count = max(counts.values())
    freq_els = []
    # print(counts.items())
    # test = counts.items()[0]
    # print(test)
    for elem in counts.items():
        if elem[1] == max_count:
            freq_els.append(elem[0])
        # print(elem[0])
    return freq_els

def stack(arr):
    cntr = 0
    for elem in arr:
        if elem == '[':
            cntr += 1
        else:
            cntr -= 1
    if cntr == 0:
        return True
    else:
        return False

def checkForBadWord(str, word):
    # if word in str:
    #     return True
    # else:
    #     return False
    
    return word in str
    
    
 
# print(sorting([1, 5, 2], 1))
# print(deepSorting([{'age': 15, 'height': 140}, {'age': 14, 'height': 150}], 'age'))
# print(getNumbers(['d', 1, 3, 2.3, 'null', 4, 5, True, False, 'dict']))
# print(min([1, 5, 34, -100]))
# print(getSet([1, 1, 1, 3, 4, 2, 2]))
# print(findTheMostRepeatedEls([1, 1, 1, 3, 4, 2, 2, 2]))
# print(stack(['[', ']', '[', ']']))
# print(checkForBadWord('Hi, Nikita', 'Hi'))
