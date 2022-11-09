def sorting(arr, direction):   #Иногда эта любовь к генераторам списков даже пугает...
    return [[x for x in sorted(arr)] if direction == 1 else [x for x in sorted(arr, reverse=True)]]

print(*sorting([1, 5, 26, 39, 2], -1))