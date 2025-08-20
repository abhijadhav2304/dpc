def find_zero_sum_subarrays(arr):
    n = len(arr)
    prefix_sum = 0
    sum_map = {}  # maps prefix_sum -> list of indices
    result = []

    for i in range(n):
        prefix_sum += arr[i]

        
        if prefix_sum == 0:
            result.append((0, i))

       
        if prefix_sum in sum_map:
            for start in sum_map[prefix_sum]:
                result.append((start + 1, i))

        
        if prefix_sum not in sum_map:
            sum_map[prefix_sum] = []
        sum_map[prefix_sum].append(i)

    return result



print(find_zero_sum_subarrays([1, 2, -3, 3, -1, 2]))      
print(find_zero_sum_subarrays([4, -1, -3, 1, 2, -1]))     
print(find_zero_sum_subarrays([1, 2, 3, 4]))              
print(find_zero_sum_subarrays([0, 0, 0]))                 
print(find_zero_sum_subarrays([-3, 1, 2, -3, 4, 0]))     
