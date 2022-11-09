def fullName(obj):
    return 


#1
a = input("write your name. ")
b = input("write your surname. ")
def fullname(name):
    print(name)
fullname(a + ' ' + b)

#4
def createobjfromstr(string):
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
        return 'error!'
print (createobjfromstr("{name: 'Vove', age: 12, type: 'owner'}"))