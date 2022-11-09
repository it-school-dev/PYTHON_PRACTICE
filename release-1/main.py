def hiFunction(name):
    print(f'Hi, {name}')

def _sum(a, b):
    print(a + b)

def isEven(num):
    print(num % 2 == 0)

def apples(num):
    try:
        kol = int(num)
        if not(kol):
            print("i have nothing")
        elif kol < 0:
            print(f"the number of apples should be more than 0")
        elif kol == 1:
            print(f"i have {kol} apple")
        else:
            print(f"i have {kol} apples")
    except ValueError:
        print("It's wrong type of number")
    

hiFunction('Verona')
_sum(32, 16)
isEven(19)
apples(input("Enter the num of apples: "))