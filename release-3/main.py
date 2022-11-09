#1

def fullName(n, s):
    a = {'name': n, 'surname': s}
    print(a['surname'].title(), a['name'].title())
name = input('Введи имя: ')
surname = input('Введи фамилию: ')
fullName(name, surname)

#2







#3
def parser(a, b, c):  
    list = [a, b, c]
    for i in list:
        if i['type'] == 'owner':
            s = 'name: ' + i['name'] + '\nage: ' + str(i['age'])
            n = i['name']
    for i in list:
        if i['type'] != 'owner' and i['owner'] == n:
            s = s +  '\n' + i['type'] + 's:' + '\n    [\n' + '    name: ' + i['name'] + '\n    oc: ' + i['oc'] + '\n    ]'
    print(s)
x_1 = {'type': 'owner', 'name': 'Vova', 'age': 12}
x_2 = {'type': 'computer','name': 'someComputer','oc': 'Mac','owner': 'Vova'}
x_3 = {'type': 'phone','name': 'somePhone','oc': 'ios','owner': 'Vova'}   
parser(x_1, x_2, x_3)  

#4

def createObjFromStr(string):
    try:
        string = string[1:-1]
        string = string.replace(' ', '')
        string = string.replace("'", "")
        key_value = string.split(',')
        dictionary = {}
        for i in key_value:
            key, value = i.split(':')
            dictionary[key] = value
        return dictionary
    except:
        return 'ERROR'
print(createObjFromStr("{name: 'Vove', age: 12, type: 'owner'}"))