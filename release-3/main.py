def fullName(obj):
    return obj['name'] + ' ' + obj['surname']

fullName({"name": 'me', 'height': 170, 'surname': 'best'})

def checkForPropertyAndValue(obj, prop):
    for k, v in obj.items():
        if (prop in obj.keys()) and isinstance(obj[prop], (int,float)) and (obj[prop] > 0):
            log = 'true'
        else:
            log = 'false'
    return log

checkForPropertyAndValue({'key': None}, 'key')

def parser(obj):
    obj_new = {'Name': obj[0]['name'], 'Age': obj[0]['age']}
    for i in range(1,len(obj)):
        try:
            obj_new[obj[i]['type'] + 's']
            obj_new[obj[i]['type'] + 's'].append(dict((k,obj[i][k]) for k in set(obj[i].keys()) - set(['type', 'owner'])))
        except KeyError:
            obj_new[obj[i]['type'] + 's'] = [dict((k,obj[i][k]) for k in set(obj[i].keys()) - set(['type', 'owner']))]
    return obj_new

test_list_1 = [{'type': 'owner','name': 'Vova','age': 12},
{'type': 'computer','name': 'someComputer','oc': 'Mac','owner': 'Vova'},
{'type': 'phone','name': 'somePhone','oc': 'ios','owner': 'Vova'},
{'type': 'console','name': 'PS5','oc': 'PS_OS','owner': 'Vova'},
{'type': 'phone','name': 'somePhone_1','oc': 'ios','owner': 'Vova'}]

parser(test_list_1)

def createObjFromStr(string):
    try :
        string = string.replace('{','')
        string = string.replace('}','')
        string = string.replace(' ', '')
        return dict(substr.split(':') for substr in string.split(','))
    except Exception:
        return('ERROR')

strg = '{name : dima, age : 20, gender : male}'

strg_fail = 1

createObjFromStr(strg_fail)
