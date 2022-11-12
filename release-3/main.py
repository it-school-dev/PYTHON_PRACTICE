def fullName(obj):
    return obj['name'] + ' ' +  obj['surname']


def checkForPropertyAndValue(obj, keyname):
    if obj.get(keyname) == None:
        return False
    elif obj.get(keyname) > 0:
        return True
    else:
        return False
    
    
def createObjFromStr(s):
    res = {}
    s = s[1:-1]
    s = s.replace(' ', '')
    try:
        for obj in s.split(','):
            key = obj.split(':')[0]
            value = obj.split(':')[1]
            value = value.replace("'", '')
            try:
                res[key] = int(value)
            except:
                res[key] = value
        return res
    except:
        return "ERROR"
