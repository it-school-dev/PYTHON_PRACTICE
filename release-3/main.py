def fullName(obj):
    return obj['surname'] + ' ' + obj['name']

def checkForPropertyAndValue(obj, st):
    return obj[st] > 0 if (st in obj and type(obj[st]) == int) else False

def parser(mas):
    res = [{
        'name': el['name'], 
        'age': el['age']
    } for el in mas if el['type'] == 'owner']  #генерируется массив словарей владельцев
    for a in res:
        a.update([[el['type'] + 's', [{
            'name': el['name'],   #Добавляем в каждый словарь владельцев массив миссивов устройств 
            'oc': el['oc']        #с помощью генераторов
        }]] for el in mas if (el['type'] != 'owner' and a['name'] == el['owner'])])
    return res

def createObjFromStr(obj):
    try:
        return obj
    except:
        return "ERROR"

print(fullName({'name': 'Harry', 'surname': 'Potter', 'age': 12}))
print(checkForPropertyAndValue({'key': None}, 'key'))
print(parser([
    {
        'type': 'owner',
        'name': 'Vova',
        'age': 12
    },
    {
        'type': 'computer',
        'name': 'someComputer',
        'oc': 'Mac',
        'owner': 'Vova'
    },
    {
        'type': 'owner',
        'name': 'Verona',
        'age': 27
    },
    {
        'type': 'tablet PC',
        'name': 'someTabletPC',
        'oc': 'ios',
        'owner': 'Verona'
    },
    {
        'type': 'phone',
        'name': 'somePhone',
        'oc': 'ios',
        'owner': 'Vova'
    },
    {
        'type': 'phone',
        'name': 'somePhone',
        'oc': 'android',
        'owner': 'Verona'
    }
]))
print(createObjFromStr("{name: 'Vova', age: 12, type: 'owner'}"))