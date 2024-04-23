class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res= []
        for word in strs:
            aux= list(word)
            res.append(aux)
        return res
    
"""Prueba"""

solution = Solution()

nums= ["Hola", "Adios"]
print("Test 1")
print(solution.groupAnagrams(nums),"\n")