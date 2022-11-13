def fullName(obj):
    return obj['surname']+' '+obj['name']

def checkForPropertyAndValue(obj,key):
    return (key in obj)and(obj[key]>0)

def parser(arr):
    own={}
    for i in arr:
        if i['type']=='owner':
            own.update(i)
        else:
            del i['owner']
            own[str(i['type'])+'s']=[]
    for i in arr:
        if i['type']!='owner':
            own[str(i['type'])+'s'].append(i)
            del i['type']
    return own

def createObjFromStr(stroka): #Допустимо ли использовать Eval и Exec
    try:
        return eval(stroka)
    except:
        return "ERROR"

    # obj= eval(stroka)
    # return obj['age']

# print(fullName({'name': 'Lim', 'surname': 'Bok', 'age': 12}))
# print(checkForPropertyAndValue({'key': 1}, 'key2'))
print(parser([
    {
        'type': 'computer',
        'name': 'someComputer',
        'oc': 'Mac',
        'owner': 'Vova'
    },
    {
        'type': 'computer',
        'name': 'newComputer',
        'oc': 'Windows',
        'owner': 'Vova'
    },
    {
        'type': 'phone',
        'name': 'somePhone',
        'oc': 'ios',
        'owner': 'Vova'
    },
    {
        'type': 'owner',
        'name': 'Vova',
        'age': 12
    }
]))
# print(createObjFromStr('''{'name': 'Vova', 'age': 12, 'type': 'owner'}'''))