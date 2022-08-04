
lon1 = [1, 3, 10, 5, 6, 2, 9, 4, 7, 8]

for i in range(len(lon1) - 1):
    Flag = True
    for j in range(len(lon1) - i - 1):
        if lon1[j] > lon1[j + 1]:
            Flag = False
            temp = lon1[j]
            lon1[j] = lon1[j + 1]
            lon1[j + 1] = temp
    if Flag:
        break
