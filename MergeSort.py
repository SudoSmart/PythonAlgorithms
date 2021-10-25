def merge(arr , low , mid , highLen):
    i = 0
    j = mid
    fin = []
    while i<mid and j<highLen:
        if arr[i] <= arr[j]:
            fin.append(arr[i])
            i+=1
        elif arr[i] > arr[j]:
            fin.append(arr[j])
            j+=1

    if i<mid:
        fin.extend(arr[i:mid])
    if j<highLen:
        fin.extend(arr[j:highLen])
    return fin


def mergeSort(arr , low , highestIndex):
    if low==highestIndex:
        return [arr[highestIndex]]
    elif low<highestIndex:
        mid = (low+highestIndex)//2
        A = mergeSort(arr, low ,mid)
        B = mergeSort(arr , mid+1 , highestIndex)
        A.extend(B)
        return merge(A , low , (len(A)+1)//2 , len(A))
    
