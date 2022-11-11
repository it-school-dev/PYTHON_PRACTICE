#sorting
num = ([int(i) for i in input().split(", ")])

a = int(input())
if a == 1:
    a = 0
num.sort(reverse = -a)

#getNumbers
print(num)

import re
s = [int(s) for s in re.findall(r'\b\d+\b', input(str()))]
print(s)

#min
a = [int(i) for i in input().split(", ")]

print(min(a))

#getSet
a = [int(i) for i in input().split(", ")]

print(set(a))


#findTheMostReapetedEls
a = [int(i) for i in input().split(", ")]
max = 0
b = []

for n in a:
    d = a.count(n)
    if d > max:
        max = d

for n in a:
    if a.count(n) == max:
        b.append(n)

print(set(b))

#stack
a = [str(i) for i in input().split()]

count1 = 0
count2 = 0
pr = True
for n in a:
    if n == '[':
        count1 = count1 + 1
    elif n == ']':
        count1 = count1 - 1
    if count1 < 0:
        pr = False
    
if count1 == 0 and pr == True:
    print(a, " -> true")
else:
    print(a, " -> false")

#checkForBadWord
S1 = input(str())
S2 = input(str())

print(S2 in S1)

def deepsorting(a, b, s):
    if a[s] > b[s]:
        print(b,a)
    else:
        print(a,b)

d1 = {'age': 15, 'height': 140}
d2 = {'age': 14, 'height': 150}
s1 = 'age'

deepsorting(d1,d2,s1)