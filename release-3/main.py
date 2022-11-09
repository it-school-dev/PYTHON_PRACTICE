def fullName(obj):
    return obj['name'] + ' ' +  obj['surname']


def checkForPropertyAndValue(obj, keyname):
    if obj.get(keyname) == None:
        return False
    elif obj.get(keyname) > 0:
        return True
    else:
        return False
