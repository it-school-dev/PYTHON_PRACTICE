from collections import Counter


#1
def sorting(arr, direction):
    if direction == 1:
        return sorted(arr)
    else:
        return sorted(arr, reverse=True)

print(sorting([2, 1, 9, 4, 5], 1))


#2
def deepSorting(arr, key):
    new_list = sorted(arr, key=lambda d: d[key])
    return new_list

print(deepSorting([{'age': 15, 'height': 140}, {'age': 14, 'height': 150}], 'age'))



#3
def getNumbers(arr):
    new_list = []
    for elem in arr:
        if type(elem) == int or type(elem) == float:
            new_list.append(elem)
    return new_list

print(getNumbers(["d", 1, 3, 2.3, "null"]))


#4
def min(arr):
    return sorted(arr)[0]

print(min([1, 5, 34, -100]))


#5
def getSet(arr):
    output = []
    for elem in arr:
        if not elem in output:
            output.append(elem)
    return output

print(getSet([1, 1, 1, 3, 4, 2, 2]))


#6
def findTheMostReapetedEls(arr):
    counts = Counter(arr)
    #print(counts)
    max_count = max(counts.values())
    freq_els = []
    for elem in counts.items():
        if elem[1] == max_count:
            freq_els.append(elem[0])
        # print(elem[0])
    return freq_els

print(findTheMostReapetedEls([1, 1, 1, 3, 4, 2, 2, 2]))


#7
def stack(arr):
    cntr = 0
    for elem in arr:
        if elem == "[":
            cntr += 1
        else:
            cntr -= 1
    if cntr == 0:
        return True
    else:
        return False

print(stack(['[', '[', ']', ']']))
# print(stack(['[', '[', '[', ']'])) is gonna return False as an output


#8
def checkForBadWord(str, word):
    if word in str:
        return True
    else:
        return False

print(checkForBadWord('Hi, Nikita', 'Hi'))