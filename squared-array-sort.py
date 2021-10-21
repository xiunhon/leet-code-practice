def sortedSquares(nums):
    def merge_2_arr(arr1, arr2):
        result = [None]*(len(arr1)+len(arr2))
        arr1_ptr = 0
        arr2_ptr = 0
        result_ptr = 0
            
        while arr1_ptr < len(arr1) and arr2_ptr < len(arr2):
            if arr1[arr1_ptr]**2 < arr2[arr2_ptr]**2:
                result[result_ptr] = arr1[arr1_ptr]
                arr1_ptr+=1
                result_ptr+=1
            else:
                result[result_ptr] = arr2[arr2_ptr]
                arr2_ptr+=1
                result_ptr+=1
        while arr1_ptr < len(arr1):
            result[result_ptr] = arr1[arr1_ptr]
            arr1_ptr+=1
            result_ptr+=1
        while arr2_ptr < len(arr2):
            result[result_ptr] = arr2[arr2_ptr]
            arr2_ptr+=1
            result_ptr+=1
            
        return result
        
    def merge_sort_helper(nums, start_index, end_index):
        if start_index >= end_index:
            return
        median = (start_index + end_index) // 2
        merge_sort_helper(nums, start_index, median)
        merge_sort_helper(nums,median+1,end_index)
        
        left = nums[start_index:median+1]
        right = nums[median+1:end_index+1]
        
        sorted_subarr = merge_2_arr(left, right)
        
        for i in range(end_index - start_index + 1):
            nums[start_index + i] = sorted_subarr[i]
    
    merge_sort_helper(nums, 0, len(nums)-1)
    for i in range(len(nums)):
        nums[i] = nums[i]**2
    return nums

nums = [-10,-2,0,1,3]
print(sortedSquares(nums))
