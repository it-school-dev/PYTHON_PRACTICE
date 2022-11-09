                                #функция sorting
a = [1,5, 2]
usl = int(input())
if usl == 1:
    a.sort()
    print(a)
elif usl == -1:
    a2 = sorted(a, reverse=True)
    print (a2)



                                    #функция deepSorting
class Employee:
  def __init__(self, age, height):
      self.age = age
      self.height = height
Alex = Employee('15', 140)
Amanda = Employee('14', 150)
L = [Alex, Amanda]
L.sort(key=lambda x: x.height)
print([item.age for item in L])




                                    #функция getNumbers
a = ['d', 1, 3, 'null']
b = []
for i in range(len(a)):
    if type (a[i]) is int:
        b.append(a[i])
        print(b)


                                        #функция min
a = [1, 5, 34, -100]
print(min(a))


                                       #функция getSet
a = [1, 1, 1, 3, 4, 2, 2]
unique_numbers = list(set(a))
print(unique_numbers)


                                       #функция findTheMostReapetedEls
a = [1, 1, 1, 3, 4, 2, 2, 2]
most = None
q_most = 0
for qount in a:
    q = a.count(qount)
    if q > q_most:
        q_most = q
        most = qount
print(most)


                                         #функция stack
def check(string):
    brackets_open = ('(', '[', '{', '<')
    brackets_closed = (')', ']', '}', '>')
    stack = []
    for i in string:
        if i in brackets_open:
            stack.append(i)
        if i in brackets_closed:    
            if len(stack) == 0:
                return False
            index = brackets_closed.index(i)
            open_bracket = brackets_open[index]
            if stack[-1] == open_bracket:
                stack = stack[:-1]  
            else: return False  
    return (not stack)


                                          #функция checkForBadWord
a = str(input())
word = input()
a.find(word)
if word in a:
    print('True')
else:
    print('False')