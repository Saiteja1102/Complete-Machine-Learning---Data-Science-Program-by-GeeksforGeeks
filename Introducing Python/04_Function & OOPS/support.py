def addition(lst):
    su = 0
    for i in lst:
        su += i
    return su


def maximum(lst):
    large = lst[0]
    for i in range(len(lst)):
        if lst[i] > large:
            large = lst[i]
        else:
            large = large
    return large


def minimum(lst):
    small = lst[0]
    for i in range(len(lst)):
        if lst[i] < small:
            small = lst[i]
        else:
            small = small
    return small

def howBig(lst):
    count = 0
    for i in lst:
        count += 1
    return count