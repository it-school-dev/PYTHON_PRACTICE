<<<<<<< HEAD
=======

>>>>>>> 7468ac432ebaabde30d7e5b980a4b6cfc41d31c5
#1
def fullName(obj):
    return obj["surname"] + " " + obj["name"]

print(fullName({
    "name": "Petya",
     "surname": "Proger",
      "age": 14
    }))



def checkForPropertyAndValue(obj, key):
    if key in obj and obj[key] > 0:
        return True
    else:
        return False

<<<<<<< HEAD
# print(checkForPropertyAndValue({"key: 5"}, "key")) #True
print(checkForPropertyAndValue({"key": 5, "ke": 18}, "ke")) #True
# print(checkForPropertyAndValue({"key: -2"}, "key")) #False
=======
print(checkForPropertyAndValue({"key: 5"}, "key"))
>>>>>>> 7468ac432ebaabde30d7e5b980a4b6cfc41d31c5
