def hiFunction(name):
    return("Hi, " + name)
print(hiFunction(a))
    
    
    
    def sum():
    print('Enter the first number:')
    a=int(input())
    print('Enter the second number:')
    b=int(input())
    print('Sum of numbers=', a+b)
sum()


def isEven(x,u,):
    if x%2==0:
        print('True')
    else:
        print('False')
a1=int(input())
a2=int(input())
a3=int(input())
print(isEven(a1,a2,a3))


x=0
def apples(x):
    print('Enter the number of apples')
    x=input()
    print("i have ", x ,"apples")
apples(x)


x=0
def getPower(x):
    print('Enter the number')
    x=input()
    c=int(x)
    print(c**2)
getPower(x)


def NumberSort(array, direction):
    if direction==1:
        array.sort()
    if direction==-1:
        array.sort(reverse=True)
    return array
res=NumberSort([1,6,8], -1)
print(res)



def DeepSorting(age, height):
    return sorted(age, key=lambda x: x[height])
print(DeepSorting([{'age': 15, 'height': 140}, {'age': 14, 'height': 150}], 'height'))





