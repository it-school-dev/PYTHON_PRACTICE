#1
a = [1, 5, 2]
x = int(input("1.введите аргумент: "))
def sorting(a):
    if x == 1:
        a.sort()
        return a
    elif x == -1:
        a.sort()
        a.reverse()
        return a
print(sorting(a))

#2
def DeepSorting(age, height):
    return sorted(age, key=lambda x: x[height])
print(DeepSorting([{'age': 15, 'height': 140}, {'age': 14, 'height': 150}], 'age'))

#3
def f(l):
    ret = []
    for i in l:
        if type(i) == int:
            ret.append(i)
            return ret
l = [1, 2, -5]
def f(l):
    v = a[0]
    for i in l:
        v = min(i, v)
        return v
print(f(l))
#не вижу ошибку

#4
def f(x):
    a = sorted(set(x), key=lambda v: x.index(v))
    return a
print(f(x))
d = [1, 1, 2]
v = []
def f(d):
    counts = {x: d.count(x) for x in d}
    return max(counts.keys(), key=lambda k: counts[k])
print(f(d))
# не могу понять почему неправильно

#5-

#6
def findTheMostReapetedEls(arr):
    int_dict={}
    for i in arr:
        if i not in int_dict:
            int_dict[i]=1
        else:
            int_dict[i]+=1
    return list({k: v for k,v in sorted(int_dict.items(), key=lambda item: item[1], reverse=True)}.keys())[:2]

print(findTheMostReapetedEls([1, 1, 1, 3, 4, 2, 2, 2]))
