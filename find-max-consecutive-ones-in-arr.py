def findMaxConsecutiveOnes(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #turn array to string
        myStr_arr = ''.join(map(str, nums))
        
        #split string by 0
        ones_arr = myStr_arr.split('0')
        
        #find max element by len, return the length
        max_consecutive = len(max(ones_arr, key = len))
        return max_consecutive
        
print(findMaxConsecutiveOnes([1,1,0,1,1,1,0,1]))
