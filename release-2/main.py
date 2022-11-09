# функция sorting
# input_string = input("Enter 3 list elements separated by space ")
# list  = input_string.split()

# define_number=int(input("Enter 1 or -1 "))
# if (define_number==1) :
#     list.sort()
#     print(list)
# else:
#   list.sort(reverse=True)
#   print(list)

# функция getNumbers

# list_1 = [ 'words', 1, 156131.131, 'random', 0.000001, 34.158920, 'stackoverflow' ]
# list_2 = [x for x in list_1 if isinstance(x, (int, float)) ]
# print(list_2)

# функция min
# list_1= [1, 5, 34, -100]
# print(min(list_1))

# функция getSet
# used = set()
# list_1 = ['100', '10', '10', '13', '18', '40', '18']
# unique = [x for x in list_1 if x not in used and (used.add(x) or True)]
# print (unique)

# функция findTheMostReapetedEls
# list=[1, 1, 1, 3, 4, 2, 2, 2]
# list_1=[(list.count(x),x) for x in set(list)]
# max_count=max(list_1)[0]
# for ele in list_1:
#    if ele[0]==max_count:
#        print(ele[1])

# функция stack
# def balanced(s):
#     pairs = { "[": "]"}
#     stack = []
#     for c in s:
#         if c in "[":
#             stack.append(c)
#         elif stack and c == pairs[stack[-1]]:
#             stack.pop()
#         else:
#             return False
#     return len(stack) == 0


# test = ("[]",)
# for s in test:
#     print(s, balanced(s))

 # функция checkForBadWord

# phrase = "Hi, Nikita"
# index = phrase.find("Hi")
# if (index !=-1):
#     print(True)
# else:
#     print(False)




