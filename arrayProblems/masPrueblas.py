class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        aux = set(nums)
        longitud= len(nums)
                
        for num in nums:
            auxT= target - num
                            
            if auxT in aux: 
                if len(aux)==1:
                    index= list(range(longitud))
                    lisRes= index
                else:    
                    aux2= nums.index(auxT)
                    lisRes= [ aux2, nums.index(num)]
                
        return lisRes
    
solution = Solution()

nums= [11,7,15,2]
print("Test 1\n")
print(solution.twoSum(nums,9))



nums2= [3,3]
print("Test 2\n")
print(solution.twoSum(nums2,6))


