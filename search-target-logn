def search(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def index_return_helper(nums, target, start_index, end_index):
            if start_index >= end_index:
                if nums[end_index] == target:
                    return end_index
                else:
                    return -1
            else:
                median = (end_index + start_index) // 2
                if nums[median] < target:
                    return index_return_helper(nums, target, median+1, end_index)
                if nums[median] > target:
                    return index_return_helper(nums, target, start_index, median)
                else:
                    return median
        
        if len(nums) == 1:
            if nums[0] == target:
                return
            else:
                return -1
        else:
            return index_return_helper(nums, target, 0, len(nums)-1)
            
print(search([-1,0,3,5,9,12],9))
