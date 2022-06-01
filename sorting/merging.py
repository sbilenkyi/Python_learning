def quick_merge(list_1, list_2):
    result = []

    p1 = 0  # pointer onto the first element in the list_1
    p2 = 0  # pointer onto the first element in the list_2

    while p1 < len(list_1) and p2 < len(list_2):  # while one of lists didn't finish
        if list_1[p1] <= list_2[p2]:
            result.append(list_1[p1])
            p1 += 1
        else:
            result.append(list_2[p2])
            p2 += 1

    if p1 < len(list_1):
        result += list_1[p1:]
    if p2 < len(list_2):
        result += list_2[p2:]

    return result
