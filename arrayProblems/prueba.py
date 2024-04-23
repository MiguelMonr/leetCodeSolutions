class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums: 
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        
        res = max(dic, key=lambda i: dic[i])
        return res
    

