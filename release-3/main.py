#1-

#2-

#3-

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