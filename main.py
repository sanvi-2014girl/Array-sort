def arrayTotalsum(a):
    length = len(a)
    if length == 1:
        return a[0]
    return a[0] + arrayTotalsum(a[1:])
a = [26]
print("Array total sum:",arrayTotalsum(a))