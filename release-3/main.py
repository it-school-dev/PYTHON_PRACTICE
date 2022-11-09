def fullName(obj):
    return obj['surname'] + ' ' + obj['name']

print(fullName({'name': 'Harry', 'surname': 'Potter', 'age': 12}))