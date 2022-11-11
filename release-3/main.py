# 1
def fullName(obj):
    return obj['surname'] + ' ' + obj['name']

# 2
def checkForPropertyAndValue(obj, key):
     if key in obj and obj[key] > 0:
         return True
     else:
         return False
