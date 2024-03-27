#Time complexity - O(N^2) Space complexity = O(1)
class Solution(object):
    def findDisappearedNumbers(self, nums):
        result = []
        
        for i in range(1, len(nums) + 1):
            found = False
            for num in nums:
                if num == i:
                    found = True
                    break
            if not found:
                result.append(i)
        
        return result

#Time complexity - O(N) Space complexity = O(N)
class Solution:
    def findDisappearedNumbers(self, nums):
        result = []
        num_set = set(nums)
        
        for num in range(1, len(nums) + 1):
            if num not in num_set:
                result.append(num)
        
        return result

#Time complexity - O(N) Space complexity = O(1)
class Solution(object):
    def findDisappearedNumbers(self, nums):
        result = []
        
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
               nums[index] = -nums[index]
        
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        
        return result
        