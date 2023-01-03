def sum_all_numbers_in_the_list(list):
    if list == []:
        return 0
    else:
        return list[0] + sum_all_numbers_in_the_list(list[1:])

print(sum_all_numbers_in_the_list([4, 3, 2]))
