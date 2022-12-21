def search_smaller(arr):
    smaller = arr[0]
    smaller_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smaller:
            smaller = arr[i]
            smaller_index = i
    return smaller_index

def sort_by_selection(arr):
    new_arr = []
    for i in range(len(arr)):
        smaller = search_smaller(arr)
        new_arr.append(arr.pop(smaller))
    return new_arr

print (sort_by_selection([5, 3, 15, 2, 10]))
