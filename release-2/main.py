"""
def sorting(m, o):
    m1 = []
    l = len(m)
    if o == 1:
        while len(m1) != l:
            for i in range(l-1):
                if m[i] > m[i+1]:
                    a = m[i]
                    m1.append(a)
                    m.pop(i)
        return m1
    #elif o == -1:

    else:
        return "InputError"
list = [1, 5, 2]
n = 1
print(sorting(list, n))
"""


def deepSorting():
    return


def getNumbers(m):
    m1 = []
    for i in range(len(m)):
        if type(m[i]) == int or type(m[i]) == float:
            m1.append(m[i])
    return m1


def min(m):
    min = m[0]
    for i in range(len(m)):
        if m[i] < min:
            min = m[i]
    return min


def getSet():
    return


def findTheMostReapetedEls():
    return


def stack(m):
    lsum = 0
    rsum = 0
    len(m)
    for i in range(len(m)):
        if m[i] == '[':
            lsum = lsum + 1
        elif m[i] == ']':
            rsum = rsum + 1
    if lsum == rsum:
        return 'true'
    else:
        return 'false'


def checkForBadWord(s, w):
    S = s.split()
    r = 0
    for i in range(len(S)):
        if S[i] == w:
            r += 1
    if r == 1:
        return 'true'
    else:
        return 'false'


def customs():
    return
