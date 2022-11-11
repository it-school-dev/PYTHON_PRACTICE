def fullName(n, s):
    d = {'name': n, 'surname': s}
    print(d['surname'], d['name'])

name = input()
surname = input()

fullName(name, surname)

#checkForPropertyAndValue
a, b = map(str, input().split(': '))
d = {a: b}

c = input()


if a == c and int(b) > 0:
    print('true')
else:
    print('false')

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

x = {'type': 'owner', 'name': 'Vova', 'age': 12}
y = {'type': 'computer','name': 'someComputer','oc': 'Mac','owner': 'Vova'}
z = {'type': 'phone','name': 'somePhone','oc': 'ios','owner': 'Vova'}   

parser(x, y, z)  

def createObjFromStr(string):
    try:
        string = string[1:-1]
        string = string.replace(' ', '')
        string = string.replace("'", "")
        Keyandvalue = string.split(',')
        dictionary = {}
        for i in Keyandvalue:
            key, value = i.split(':')
            dictionary[key] = value
        return dictionary
    except:
        return 'ERROR'

print(createObjFromStr("{name: 'Vove', age: 12, type: 'owner'}"))