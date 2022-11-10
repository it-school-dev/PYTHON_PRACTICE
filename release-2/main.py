def sorting(arr, direction):
    if direction == 1:
        direction = False
    else:
        direction = True
    return (arr.sort(reverse = direction))