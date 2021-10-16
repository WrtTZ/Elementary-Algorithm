
def binary_search(l, t):  # l is the array to be searched, must be sorted. t is the target
    begin = 0
    end = len(l) - 1

    while begin <= end:
        middle = (begin + end) // 2
        if l[middle] == t:
            return middle
        elif l[middle] > t:
            end = middle - 1
        elif l[middle] < t:
            begin = middle + 1
