"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

# works if each number is unique, lack of duplicates in dict stops it working for multiple
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
        Dict [num, index]

        for each num - if desired - num in dict --> return indexes
        value_indexes = {val: idx for idx, val in enumerate(nums)}
o        """                

        for num in nums:
            value_needed = target - num
            if value_indexes[value_needed] != None:                
                return [value_indexes[num], value_indexes[value_needed]]

# works
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # empty list for each value
        value_indexes = {num: [] for num in nums}
        
        # store every index for each value (key)
        for index, num in enumerate(nums):
            value_indexes[num].append(index)        

        for num in nums:
            value_needed = target - num
            if value_needed in value_indexes:
                if num != value_needed:   # two unique values
                    return [value_indexes[num][0], value_indexes[value_needed][0]]                
                elif num == value_needed and len(value_indexes[num]) > 1: # two of same value. Length check needed because target could be = existing value, but value only occurs once 
                    return [value_indexes[num][0], value_indexes[num][1]]
                
