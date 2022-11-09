def sorting(arr, direction):   #Иногда эта любовь к генераторам списков даже пугает...
    return [[x for x in sorted(arr)] if direction == 1 else [x for x in sorted(arr, reverse=True)]]

def deepSorting(mas, atr):
    return sorted(list(mas), key=lambda item: item[atr])

def getNumbers(mas):
    return [x for x in mas if (type(x) == int or type(x) == float)]

def _min(mas):
    return sorted(mas)[0]

print(*sorting([1, 5, 26, 39, 2], -1))
print(deepSorting([{'age': 15, 'height': 140}, {'age': 14, 'height': 150}], 'age'))
print(getNumbers(['d', 1, ['b', 'glfdk'], 3, 0.8]))
print(_min([1, 5, -222, 34, -100]))