#1
def hiFunction(name):
    print('Hi, ' + name.title())

inname = input()
hiFunction(inname)

#2

def sum(a,b):
    c = a + b
    print(c)
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

sum(a,b)

#3

def isEven(n):
    if x == 5:
        print(n, '->', 'False') # тупанул конкретно ахахах
                                # потом испралю
    if x == 0:
        print(n, '->', 'True')   
    if x == 4:
        print(n, '->', 'True')     

x = int(input("x = "))

isEven(x)

#4 

def apples(n):
    print("I have " + str(n) + " apples")  

x = input("How many apples do you have?: ")

apples(x)

#5

def getPower(x):
    print('Квадрат числа',x, '=',x**2)
  
x = int(input("x = "))
getPower(x)