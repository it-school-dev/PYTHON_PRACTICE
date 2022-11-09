
# 1

# a = input()
# def hiFunction(name):
#     return("Hi, " + name)
# print(hiFunction(a))
#
# 2
#
# a = int(input())
# b = int(input())
# def sum(x, y):
#     return(x + y)
# print(sum(a, b))
#
# x = int(input())
# def isEven(x):
#     if x % 2 == 0:
#         return "true"
#     else:
#         return "false"
# print(isEven(x))
#
# x = int(input())
# def apples(x):
#     return "i have", x, "apples"
# print(apples(x))
#
# x = int(input())
# def getPower(x):
#     return x ** 2
# print(getPower(x))
#
# a = [1, 5, 2]
# x = int(input())
# def sorting(a):
#     if x == 1:
#         a.sort()
#         return a
#     elif x == -1:
#         a.sort()
#         a.reverse()
#         return a
# print(sorting(a))
#
#
# def DeepSorting(age, height):
#     return sorted(age, key=lambda x: x[height])
# print(DeepSorting([{'age': 15, 'height': 140}, {'age': 14, 'height': 150}], 'height'))
#
#
#
# def f(a):
#     ret = []
#     for i in a:
#         if type(i) == int:
#             ret.append(i)
#     return ret
# a = [1, 2, -5]
# def f(a):
#     v = a[0]
#     for i in a:
#         v = min(i, v)
#     return v
# print(f(a))
#
#
# def f(x):
#     a = sorted(set(x), key=lambda v: x.index(v))
#     return a
# print(f(x))
#
# d = [1, 1, 2]
# v = []
# def f(d):
#     counts = {x: d.count(x) for x in d}
#     return max(counts.keys(), key=lambda k: counts[k])
# print(f(d))

x = input()
c = input()
def g(x):
    if c in x:
        return "true"
    else:
        return "false"
print(g(x))




