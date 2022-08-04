def min_index(lon, s):
    min = s
    for i in range(s + 1, len(lon)):
        if lon[i] < lon[min]:
            min = i
    return min
    
lon = [1, 3, 10, 5, 6, 2, 9, 4, 7, 8]
for i in range(len(lon) - 1):
    min_i = min_index(lon, i)
    if min_i != i:
        lon[min_i], lon[i] = lon[i], lon[min_i]
print(lon)
