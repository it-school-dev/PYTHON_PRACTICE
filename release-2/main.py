def sorting(arr, direction):   #Иногда эта любовь к генераторам списков даже пугает...
    return [[x for x in sorted(arr)] if direction == 1 else [x for x in sorted(arr, reverse=True)]]

def deepSorting(mas, atr):
    return sorted(list(mas), key=lambda item: item[atr])

print(*sorting([1, 5, 26, 39, 2], -1))
print(deepSorting([{'age': 15, 'height': 140}, {'age': 14, 'height': 150}], 'age'))