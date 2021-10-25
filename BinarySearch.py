def bin(A , num , low , high):
    if low == high and A[low] == num:
        return low
    elif low==high and A[low] != num:
        return -1
    mid = (low+high)//2
    if A[mid] == num:
        return mid
    elif A[mid] < num:
        return bin(A,num , mid+1 , high)
    elif A[mid] > num:
        return bin(A,num,low , mid)
    return -1
