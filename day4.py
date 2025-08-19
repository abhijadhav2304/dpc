def merge_in_place(arr1, arr2):
    import math
    m, n = len(arr1), len(arr2)
    total = m + n
    
    def get(i):
        return arr1[i] if i < m else arr2[i - m]    
    
    def set_val(i, val):
        if i < m:
            arr1[i] = val
        else:
            arr2[i - m] = val
    
    gap = math.ceil(total / 2)
    
    while gap > 0:
        i = 0
        j = gap
        while j < total:
            if get(i) > get(j):
                temp = get(i)
                set_val(i, get(j))
                set_val(j, temp)
            i += 1
            j += 1
        
        if gap == 1:
            break
        gap = math.ceil(gap / 2)
    
    return arr1, arr2



print(merge_in_place([1, 3, 5], [2, 4, 6]))  
print(merge_in_place([10, 12, 14], [1, 3, 5]))
print(merge_in_place([2, 3, 8], [4, 6, 10]))   
print(merge_in_place([1], [2]))                
