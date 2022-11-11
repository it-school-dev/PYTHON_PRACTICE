def hiFunction(name):
    print('Hi, ' + name)

inname = input(str())
hiFunction(inname)

a = [int(i) for i in input().split(", ")]
print(sum(a))

def isEven(a):
    n = 0
    for i in a:
        if (abs(a[n]) == 1) or (abs(a[n] % 2) == 0):
            print(a[n], '->', 'true')
        else:
            print(a[n], '->', 'false')
        n = n + 1

numbers =  [int(i) for i in input().split(", ")]
isEven(numbers)

def apples(num):
    print('I have ' + num + ' apples')

nums = input(str())
apples(nums)

def get_power(a):
    print(a, '->', a ** 2)

b = int(input())
get_power(b)