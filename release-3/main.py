def fullName(obj):
    return obj['surname'] + ' ' + obj['name']

def checkForPropertyAndValue(obj, st):
    return obj[st] > 0 if (st in obj and type(obj[st]) == int) else False

print(fullName({'name': 'Harry', 'surname': 'Potter', 'age': 12}))
print(checkForPropertyAndValue({'key': None}, 'key'))