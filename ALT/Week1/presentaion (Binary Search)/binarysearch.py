a = list(map(int,input().split()))
n = len(a)
b = list(map(int,input().split()))
m = len(b)

def binarySearch(A, low, high, target):
    mid = int((low+high)/2)
    while low <= high and not(low == high == mid):
        mid = int((low+high)/2)
        if A[mid] == target:
            return mid
        elif A[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1

for i in range(m):
    print(binarySearch(a, 0, n, b[i]), end = ' ')

