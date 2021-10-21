def sortedSquares(nums):
    # helper function that merge 2 sorted arrays together
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

    #find non-negative and negative part of sorted array
    #negative part is already sorted.
    #just need to be reversed and put absolute values into a new array, eg:[-10,,-5,-3]->[3,5,10]
    i = 0
    while i != len(nums):
        if nums[i] >= 0:
            break
        i += 1
    non_negative = nums[i:]
    negative = [None]*(i)
    while i != 0:
        negative[len(negative)-i] = abs(nums[i-1])
        i -= 1

    #use merge_2_arr to merge 2 sorted arrays together
    squared_arr = merge_2_arr(negative,non_negative)
    for i in range(len(squared_arr)):
        squared_arr[i] = squared_arr[i]**2
    return squared_arr

nums = [-10,-2,0,1,3]
print(sortedSquares(nums))
