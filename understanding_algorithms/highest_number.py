def maximum(list):
    if len(list) == 2:
        return list[0] if list [0] > list[1] else list[1]
    sub_max = maximum(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print(maximum([1, 3, 4, 10, 2]))
