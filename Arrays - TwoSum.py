"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

def get_element_counts(l: int) -> dict:
        counts = {elem: 0 for elem in l}
        for elem in l:
            counts[elem] += 1
        return counts

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

def getValueIndexes(nums)
    # empty list for each value
    value_indexes = {num: [] for num in nums}
        
    # store every index for each value (key)
    for index, num in enumerate(nums):
        value_indexes[num].append(index)

    return value_indexes
    
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
                
# two pointers
def twoSum(self, nums: List[int], target: int) -> List[int]:        

    nums_sorted = sorted(nums)
    value_indexes = getValueIndexes(nums)

    left = 0 
    right = len(nums_sorted) - 1
       
    while left < right:
        pair_sum = nums_sorted[left] + nums_sorted[right]
        if pair_sum == target:
            if nums_sorted[left] == nums_sorted[right]:
                return (value_indexes[nums_sorted[left]][0], value_indexes[nums_sorted[left]][1])
            else:
                return (value_indexes[nums_sorted[left]][0], value_indexes[nums_sorted[right]][0])
        elif pair_sum > target:
            right -= 1
        elif pair_sum < target:
             left += 1