def sorting(list, flag):    #Как часто стоит делать комиты и пуши   #Доделал
    return sorted(list, reverse=bool(flag+1))   #return - функция, print - подпрограмма?

def deepSorting(list,dic): #Доделал
    return sorted(list,key=lambda d: d[dic])

def getNumbers(list):   #Вопрос Except #Доделал
    for i in list:
        if type(i)!=float:
            list.remove(i)
    return(list)
            
    # listNew=[]
    # for i in list:
    #     try:
    #         listNew.append(float(i))
    #     except ValueError:
    #         print
    # return listNew

def min(list):  #Доделал
    return sorted(list)[0]

def getSet(list): #Обязательно ли обнуление(для поиска максимума/вайла)(Вроде выяснил, что нужно) #Доделал
    for i in list:  #Фор в Питоне не статичен?(В принципе особенности Питона)
        if list.count(i)>1:
            list.remove(i)
    return list #Есть ли какой-то смысл загонять все в одну строку? Или писать лучше построчно

def findTheMostReapetedEls(list): #Доделал
    max=0
    list_new=[]
    for i in list:
        if list.count(i)>max:
            max=list.count(i)
            list_new.clear()
            list_new.append(i)
        elif ((list.count(i)==max)and(i not in list_new)):
            list_new.append(i)
    return list_new

def stack(list): #Вопрос по комментарию насчет [[]][]
    str=''.join(list)
    while str>'':
        if str[0]==']':
            return 'false'
        else:
            str=str.replace('[]','')
    if str=='':
        return 'true'

def checkForBadWord(stroka, slovo):    #Доделал
    return stroka.find(slovo)>=0
        

# print(sorting([1, 5, 2], -1))
print(deepSorting([{'age': 15, 'height': 140}, {'age': 14, 'height': 150}, {'age': 16, 'height': 120}], 'height'))
# print(getNumbers(['d', -1, 3.5, 'null']))
# print(min([1, 5, 34, -100]))
# print(getSet([1, 1, 1, 3, 4, 2, 2]))
# print(findTheMostReapetedEls([1, 1, 1, 3, 4, 2, 2, 2]))
# print(stack([']', '[', ']', '[']))
# print(checkForBadWord('Hi, Nikita', 'Hi'))