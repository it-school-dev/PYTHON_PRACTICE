# 1)
def sayHiToAnyone(name):
  return "Hello, it's nice to meet you, " + name

print(sayHiToAnyone("Nikita"))


# 2)
def summation(value, multiplier):
  return value + multiplier

print(summation(10, 12))


# 3)
def isEven(value):
  if value % 2 == 0:
    return True
  else:
    return False

print(isEven(5))


#4
def apples(amount):
    # return f"I have {amount} apples"
    return "I have {} apples".format(amount)

print(apples(7))


# 5)
def getPowerRoot(number):
  return number ** 2

<<<<<<< HEAD
print(getPowerRoot(25))
=======
print(getPowerRoot(25))



>>>>>>> 7468ac432ebaabde30d7e5b980a4b6cfc41d31c5
