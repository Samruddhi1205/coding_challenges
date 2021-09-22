'''In an array that is sorted, but rotated, find the position of the given number in O(log n).
eg:
Input array : [3, 10, 20, -3, 2]
Input number : -3
Output : Index position : 3'''

#python code for rotated array search element
def pivotedBinarySearch(a, n, k):
    pivot = findPivot(a, 0, n-1);
    if (pivot == -1):
        return binarySearch(a, 0, n-1, k);

    if (a[pivot] == k):
        return pivot
    if (a[0] <= k):
        return binarySearch(a, 0, pivot-1, k);
    return binarySearch(a, pivot + 1, n-1, k);
 
def findPivot(a, low, high):
    if (high < low):
        return -1
    if (high == low):
        return low
    mid = int((low + high)/2)
    if (mid < high and a[mid] > a[mid + 1]):
        return mid
    if (mid > low and a[mid] < a[mid - 1]):
        return (mid-1)
    if (a[low] >= a[mid]):
        return findPivot(a, low, mid-1)
    return findPivot(a, mid + 1, high)

def binarySearch(a, low, high, k):
    if (high < low):
        return -1
    mid = int((low + high)/2)
    if (k == a[mid]):
        return mid
    if (k> a[mid]):
        return binarySearch(a, (mid + 1), high,k);
    return binarySearch(a, low, (mid -1), k);

n=int(input())
a=[]
for i in range(n):
    x=int(input())
    a.append(x)
k = int(input())
print("Index of the element is : ",pivotedBinarySearch(a, n, k))
