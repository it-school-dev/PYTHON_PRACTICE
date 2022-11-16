# #TASK1
# def fullName(str):
#         return str['surname'] + ' ' + str['name']
# print(fullName({'name': 'Lim', 'surname': 'Bok', 'age': 12}))

#TASK2
def checkForPropertyAndValue(str, x):
        for i in str:
                if i==x and str[i]>0:
                        return 'true'
                else:
                        return 'false'
print(checkForPropertyAndValue({'key': 5}, 'key2'))

#TASK3
# def parser(a):
#         for i in a:
#                 if 'age' in i:
#                         d=i['name']
#                         res=i
#                         a.remove(i)
#         for i in a:
#                 if i['owner']==d:
#                         res[i['type']]=[{'name':i['name'], 'oc':i['oc']}]
#         return res
# print(parser([
#     {
#         'type': 'owner',
#         'name': 'Vova',
#         'age': 12
#     },
#     {
#         'type': 'computer',
#         'name': 'someComputer',
#         'oc': 'Mac',
#         'owner': 'Vova'
#     },
#     {
#         'type': 'phone',
#         'name': 'somePhone',
#         'oc': 'ios',
#         'owner': 'Vova'
#     }
# ]))

#TASK4(?????????????????????????)
# def createObjFromStr(str):
#     try:
#         str = str[1:-1]
#         str = str.replace(',')
#         str = str.replace(',')
#         key_value = str.split(',')
#         dictionary = {}
#         for i in key_value:
#             key, value = i.split(':')
#         dictionary[key] = value
#         return dictionary
#     except:
#         return 'ERROR'
# str1='{name: "Vova", age: 12, type: "owner"}'
# print(createObjFromStr(str1))