#1
a=input("1.введите имя:")
def hiFunction(name):
    print("Hi, "+ name)
hiFunction(a)

#2
x=int(input("2.Ведите 1 число:"))
y=int(input("введите 2 число:"))
def sum(x,y):
    return x+y
print(sum(x,y))

#3
b=int(input("3.введите число:"))
def isEven(x):
    if x%2==0:
        return True 
    else:
        return False
print(isEven(b))

#4
c=int(input("4.введите число:"))
def apples(number):
    print("i have "+ str(number) + " apples")
print(apples(c))

#5
d=int(input("5.введите число:"))
def getPower(a1):
    return a1**2
print(getPower(d))
