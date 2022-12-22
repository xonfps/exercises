def regressive(i):
    print(i)
    if i <= 1:
        return
    else:
        regressive(i - 1)

print(regressive(10))