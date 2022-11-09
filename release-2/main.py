#1

from unittest.util import sorted_list_difference

def sorting(sortedList):

    Input = input('введите числа от 1 до 9 без пробелов и запятых: ')
    List = list(Input)
    
    x = int(input("Введите -1 или 1: "))
    if x == 1:
        List.sort()
        print(List)
    if x == -1:
        List.sort(reverse=True)
        print(List)
sorting(sorted_list_difference)

#2

def deepsorting(a, b, s):
    if a[s] > b[s]:
        print(b,a)
    else:
        print(a,b)
p_1 = {'age': 15, 'height': 140}
p_2 = {'age': 14, 'height': 150}
s_1 = 'age'
deepsorting(p_1,p_2,s_1)

#3

def getNumbers(arr):
    list = []
    for elem in arr:
        if type(elem) == int or type(elem) == float:
            list.append(elem)
    return list
print(getNumbers( ['d', 6, 'null', 5] ))

#4

Input = input()
list = list(Input)  
low_num = list[0]
for i in list:
    if i < low_num:
        low_num = i
print(low_num)

#5

list = [1,2,21,21,1,4,6,6,6,7]   
mySet = set(list)
print(mySet)



