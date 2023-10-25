"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""

def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)        
        half = n/2        
        counts = {num: 0 for num in nums}

        for num in nums:
            counts[num] += 1            
            if counts[num] > half:
                return num
				
# faster + less memory (both pass)
# majority element will always be in the middle of the array because it takes up more than half
def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]