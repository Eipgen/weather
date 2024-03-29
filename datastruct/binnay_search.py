def binary_search(data, target, low, high):
    """Return true if target is found in indicated portion of a Python list ,
    a search only considers the portion from data[low] to data[high] inclusive.
    """
    if low > high:
        return False
    else:
        mid = (high + low)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            # recur on the portion left of the middle
            return binary_search(data, target, low, mid-1)
        else:
            #recur on the portion right of the middle
            return binary_search(data, target, mid+1, high)

data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 22
low = 0
high =15
print(binary_search(data, target, low, high)) 