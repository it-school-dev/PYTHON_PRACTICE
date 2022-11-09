def fullName(obj):
    return obj['surname'] + ' ' + obj['name']

def checkForPropertyAndValue(obj, key):
    if key in obj and obj[key] > 0:
        return True
    else:
        return False

# def parser(arr)

# print(fullName({'name': 'Den', 'surname': 'Zai', 'age': 12}))
# print(checkForPropertyAndValue({'key': 5, 'ky': 2}, 'ky'))

# dictionary = {
#     'name': 'Den',
#     'surname': 'Zai',
#     'age': 12
# }

# print(list(dictionary.keys())[0])