class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map_numbers = {} 

        for i, num in enumerate(nums): # enumerate: gets the index and the item
            complement = target - num
            if complement in hash_map_numbers: # if the complement exists, return both indexes
                hash_map_numbers[complement]
                return [i, hash_map_numbers[complement]]
            else: # else, add the current number and its index to a dict 
                hash_map_numbers[num] = i
