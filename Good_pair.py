""" Given an array A and an integer B.
A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B).
Check if any good pair exist or not."""

""" Approach - 
    To optimize code - don't have to check same element (1,2) and (2,1) 
                       skip the (i, j) 
                        ...... to do this =>> (i+1)
                       """

def good_pair(array, k):
    length = len(array)
    for i in range(0, length):
        for j in range(i+1, length):
            if(array[i] + array[j] == k):
                return 1
    return 0

array = list(map(int, input().split()))
k = int(input())
print(good_pair(array, k))