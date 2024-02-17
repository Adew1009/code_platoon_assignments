def binary_search(target, lst, high="first", low=0):
        lst = sorted(lst)
        if high == "first":
             high = len(lst)-1
        mid = (int(low) + int(high))//2
        if low>high:
            return -1
        elif lst[mid] == target:
            return mid
        if lst[mid] > target:
            return binary_search(target, lst, mid-1, low)
        if lst[mid] < target:
            return binary_search(target,lst, high, mid+1)
        return mid
       
 

  
   