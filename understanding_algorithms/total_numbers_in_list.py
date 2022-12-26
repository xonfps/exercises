def total_numbers_in_list(list):
    if list == []:
        return 0
    else:
        return 1 + total_numbers_in_list(list[1:])

print(total_numbers_in_list([1, 5, 6]))