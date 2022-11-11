# 1
b = [1, 5, 2]
c = int(input())
def sorting(b):
    if c == 1:
        b.sort()
        return a
    elif c == -1:
            b.sort()
            b.reverse()
            return b
print(sorting(b))

# 2
def deepSorting(age, height):
    return sorted(age, key=lambda d: d[height])
print(DeepSorting([{'age': 15, 'height': 140}, {'age': 14, 'height': 150}], 'height'))

# 3
def getNumbers(arr):
     new_list = []
     for elem in arr:
         if type(elem) == int or type(elem) == float:
             new_list.append(elem)
     return new_list

# 4
def min(arr):
     return sorted(arr)[0]

# 5
def getSet(arr):
     output = []
     for elem in arr:
         if not elem in output:
             output.append(elem)
     return output

# 6
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

# 7
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

# 8
def checkForBadWord(str, word):
    if word in str:
        return True
    else:
        return False
return word in str