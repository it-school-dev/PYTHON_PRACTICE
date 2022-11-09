def sorting(arr, direction):
    return 


#1
def sorting(a,direction):
    a.sort()
    if direction == 1:
        return a
    elif direction == -1:
        return a
print(sorting([1,4,3,5,7],1))
print(sorting([1,4,3,5,7],-1))

#2
def DeepSorting(age, height):
    return sorted(age, key=lambda x: x[height])
print(DeepSorting([{'age': 15, 'height': 140}, {'age': 14, 'height': 150}], 'height'))

#3


#4
def f(a):
    ret = []
    for i in a:
        if type(i) == int:
            ret.append(i)
    return ret
a = [1, 2, -5]
def f(a):
    v = a[0]
    for i in a:
        v = min(i, v)
    return v
print(f(a))

#6
def findthemostrepeated(y):
    int_dict = {}
    for i in range (y):
        if 1 not in int_dict:
            int_dict[i] = 1
        else:
            int_dict[i] += 1
    return list({k: v for k, v in sorted(int_dict.items(), key=lambda item: item[1],reverse=True)}.keys())[:2]

print(findthemostrepeated([1,1,1,3,4,2,2,2]))